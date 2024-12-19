import time
from datetime import datetime
import warnings
from utils.login_fc import *
from utils.root_fc import *
from utils.teacher_fc import *
from utils.student_fc import *
import numpy as np
st.set_page_config(page_title="SQL Server 学生管理系统", layout="wide")
# 忽略所有的 UserWarning
warnings.filterwarnings('ignore', category=UserWarning)
import streamlit as st
# from utils.function import *
# Streamlit 页面设置
st.title("SQL Server 学生管理系统")
if 'user_roles' not in st.session_state:
    st.session_state.user_roles = load_user_roles()
# 用户登录界面
if st.session_state.user_roles['login'] == ['0']:
    # 选择登录角色
    st.sidebar.title("用户登录")
    permission = st.sidebar.radio("选择登录角色", ["root", "teacher", "student"])
    if permission == 'student':
        st.session_state.student_id = st.text_input("学生学号", placeholder="输入学生ID")
    elif permission == 'teacher':
        st.session_state.teacher_id = st.text_input("教师ID", placeholder="输入教师ID")
    else:
        username = st.text_input("用户名", placeholder="输入用户名")
    password = st.text_input("密码", type="password", placeholder="输入密码")

    if st.button("连接"):
        conn_tmp = connect_to_database("root", st.session_state.user_roles['password_root'][0])
        if permission == 'student':
            password_student = get_student_password(conn_tmp, st.session_state.student_id)
            if password_student['Password'][0] == password:
                st.session_state.conn = connect_to_database("student", st.session_state.user_roles['password_student'][0])
                st.success("连接成功")
                st.session_state.login_time = time.time()
                st.session_state.user_roles['login'] = ['1']
                save_user_roles(st.session_state.user_roles)
                st.session_state.permission = permission
            else:
                st.warning("账号或密码错误！")
        elif permission == 'teacher':
            password_teacher = get_teacher_password(conn_tmp, st.session_state.teacher_id)
            if password_teacher['Password'][0] == password:
                st.session_state.conn = connect_to_database("teacher", st.session_state.user_roles['password_teacher'][0])
                st.success("连接成功")
                st.session_state.login_time = time.time()
                st.session_state.user_roles['login'] = ['1']
                save_user_roles(st.session_state.user_roles)
                st.session_state.permission = permission
            else:
                st.warning("账号或密码错误！")
        else:
            if password == st.session_state.user_roles['password_root'][0]:
                st.session_state.conn = connect_to_database("root", st.session_state.user_roles['password_root'][0])
                st.success("连接成功")
                st.session_state.login_time = time.time()
                st.session_state.user_roles['login'] = ['1']
                save_user_roles(st.session_state.user_roles)
                st.session_state.permission = permission
            else:
                st.warning("账号或密码错误！")
# 创建菜单
if st.session_state.user_roles['login'] == ['1']:
    if st.session_state.permission == 'root':
        menu = st.sidebar.radio(
            "管理员模式", [
                "教师管理 👨‍🏫",
                "学生管理 👩‍🎓",
                "教务通知 📢",
                "课程统计 📊",
                "班级交流区 💬",
                "课程评价与预选课程 📅",
                "修改密码 🔑"
            ]
        )
        if menu == "教师管理 👨‍🏫":
            st.subheader("教师管理 👨‍🏫")
            teachers = get_teachers(st.session_state.conn)
            column_config = {
                "TeacherID": {"label": "教师ID"},
                "TeacherName": {"label": "教师"},
                "Email": {"label": "邮箱"},
                "Position": {"label": "职位"},
                "sex": {"label": "性别"},
            }
            edited = st.data_editor(
                teachers,
                width=1400,
                height=300,
                column_config=column_config,
                num_rows="dynamic",
            )
            if st.button("更新教师数据"):
                update_teachers(st.session_state.conn, edited)
                st.success("教师数据更新成功！")

            # 添加新教师
            col = st.columns(5)
            new_teacher_id = col[0].text_input("添加新教师ID")
            new_teacher_name = col[1].text_input("添加新教师姓名")
            new_teacher_email = col[2].text_input("添加新教师邮箱")
            new_teacher_position = col[3].text_input("添加新教师职位")
            new_teacher_sex = col[4].text_input("添加新教师性别")

            if st.button("添加教师"):
                if new_teacher_id and new_teacher_name and new_teacher_email and new_teacher_position and new_teacher_sex:
                    add_teacher(st.session_state.conn, new_teacher_id, new_teacher_name, new_teacher_email, new_teacher_position, new_teacher_sex)
                    st.success("教师添加成功！")
                else:
                    st.warning("请输入教师信息")
            # 删除选中的教师
            selected_teacher = st.selectbox("选择教师", teachers["TeacherName"])
            if st.button("删除选中教师"):
                if selected_teacher:
                    delete_teacher(st.session_state.conn, selected_teacher)
                    st.success("教师删除成功！")
                else:
                    st.warning("请选择要删除的教师")
            if st.button("查询选中教师班级"):
                class_ = find_teacher_class(st.session_state.conn, selected_teacher)
                # st.data_editor(
                #     class_,
                #     width=800,
                #     height=300,
                #     num_rows="dynamic",
                # )
                st.table(class_)
            # 学生管理
        elif menu == "学生管理 👩‍🎓":
            st.subheader("学生管理 👩‍🎓")
            # 获取学生数据
            students = get_students(st.session_state.conn)
            # 编辑学生数据
            column_config = {
                "StudentID": {"label": "学生ID"},
                "StudentName": {"label": "学生"},
                "Email": {"label": "邮箱"},
                "Major": {"label": "专业"},
                "Grade": {"label": "年级"},
                "sex": {"label": "性别"},
            }
            edited = st.data_editor(
                students,
                width=1400,
                height=300,
                column_config=column_config,
                num_rows="dynamic",
            )

            if st.button("更新学生数据"):
                update_students(st.session_state.conn, edited)
                st.success("学生数据更新成功！")

            # 添加新学生
            col1 = st.columns(3)
            col2 = st.columns(3)
            new_student_id = col1[0].text_input("添加新学生ID")
            new_student_name = col1[1].text_input("添加新学生姓名")
            new_student_email = col1[2].text_input("添加新学生邮箱")
            new_student_major = col2[0].text_input("添加新学生专业")
            new_student_grade = col2[1].text_input("添加新学生年级")
            new_student_sex = col2[2].text_input("添加新学生性别")

            if st.button("添加学生"):
                if new_student_id and new_student_name and new_student_email and new_student_major and new_student_grade and new_student_sex:
                    add_student(st.session_state.conn, new_student_id, new_student_name, new_student_email,
                                new_student_major, new_student_grade,new_student_sex)
                    st.success("学生添加成功！")
                else:
                    st.warning("请输入学生信息")

            # 删除选中的学生
            selected_student = st.selectbox("选择学生", students["StudentName"])
            if st.button("删除学生"):
                if selected_student:
                    delete_student(st.session_state.conn, selected_student)
                    st.success("学生删除成功！")
                else:
                    st.warning("请选择要删除的学生")
            if st.button("查询选中学生课程"):
                course = find_student_course(st.session_state.conn, selected_student)
                st.table(course)
        elif menu == "教务通知 📢":
            st.subheader("教务通知 📢")
            message_list = get_academic_notices(st.session_state.conn)
            message_list = message_list.rename(columns={
                'NotificationID': 'ID',
                'Title': '通知标题',
                'Content': '通知内容',
                'Publisher': '发布人',
                'PublishDate': '发布时间',
                'EffectiveDate': '生效日期',
                'ExpirationDate': '到期日期',
                'Status': '状态'
            })
            st.dataframe(message_list.iloc[:, 1:], width=1400, height=300)
            col = st.columns(4)
            message_title = col[0].text_input("通知标题")
            identity = col[1].text_input("发布人")
            start_time = col[2].date_input("通知起始日期")
            end_time = col[3].date_input("通知结束日期")
            message = st.text_area("通知内容")
            if st.button("发送通知"):
                send_academic_notice(st.session_state.conn, message_title, message, identity, start_time, end_time)
                st.success("通知发送成功！")
            del_message_id = st.selectbox("选择要删除的通知", message_list["通知标题"])
            if st.button("删除通知"):
                delete_academic_notice(st.session_state.conn, del_message_id)
                st.success("通知删除成功！")
        elif menu == "课程统计 📊":
            st.subheader("课程统计 📊")
            course_stats = get_course_statistics(st.session_state.conn)
            column_config = {
                "CourseName": {"label": "课程名"},
                "TeacherName": {"label": "教师"},
                "selected_count": {"label": "选课人数"},
                "selection_percentage": st.column_config.ProgressColumn(
                    "选课比例",
                    min_value=0,
                    max_value=100,
                    format="%d%%",
                ),
            }
            st.data_editor(
                course_stats,
                width=1400,
                height=300,
                column_config=column_config,
                num_rows="dynamic",
            )
            st.subheader("成绩统计")
            column_config = {
                "CourseName": {"label": "课程名"},
                "avg_grade": {"label": "平均成绩"},
                "max_grade": {"label": "最高分"},
                "min_grade": {"label": "最低分"},
                "student_count": {"label": "学生人数"},
            }
            grade_stats = get_grade_statistics(st.session_state.conn)
            st.data_editor(
                grade_stats,
                width=1400,
                height=300,
                column_config=column_config,
                num_rows="dynamic",
            )
        elif menu == "班级交流区 💬":
            st.subheader("班级交流区 💬")
            course_name = st.selectbox("选择课程", get_course_statistics(st.session_state.conn)["CourseName"])
            message_list = get_message_course(st.session_state.conn, course_name)
            message_list = message_list.rename(columns={
                'SpeakerType': '身份',
                'SpeakerName': '发言人',
                'Content': '内容',
                'Timestamp': '发布时间',
            })
            st.table(message_list)
        elif menu == "课程评价与预选课程 📅":
            st.subheader("课程评价与预选课程 📅")
            st.subheader("设定系统开放时间")
            col_start = st.columns(2)
            date_start = col_start[0].date_input("选择起始日期")
            time_start = col_start[1].time_input("选择起始时间")
            start_datetime = datetime.combine(date_start, time_start)
            start_timestamp = start_datetime.timestamp()
            col_end = st.columns(2)
            date_end = col_end[0].date_input("选择结束日期")
            time_end = col_end[1].time_input("选择结束时间")
            end_datetime = datetime.combine(date_end, time_end)
            end_timestamp = end_datetime.timestamp()
            if st.button("更新开放时间"):
                st.session_state.user_roles['start_time'][0] = start_timestamp
                st.session_state.user_roles['end_time'][0] = end_timestamp
                save_user_roles(st.session_state.user_roles)
                st.success("开放时间更新成功")
            st.subheader("课程评价")
            start = datetime.fromtimestamp(float(st.session_state.user_roles['start_time'][0]))
            end = datetime.fromtimestamp(float(st.session_state.user_roles['end_time'][0]))
            if datetime.now() < start:
                st.warning("系统还未开放")
            elif start <= datetime.now():
                column_config = {
                    "CourseName": {"label": "课程名"},
                    "review_count": {"label": "评价人数"},
                    "average_score": {"label": "平均评分"},
                    "review_percentage": st.column_config.ProgressColumn(
                        "完成比例",
                        min_value=0,
                        max_value=100,
                        format="%d%%",
                    ),
                }
                courses_grade = get_courses_grade(st.session_state.conn)
                st.data_editor(
                    courses_grade,
                    width=1400,
                    height=300,
                    column_config=column_config,
                    num_rows="dynamic",
                )
            st.subheader("预选情况")
            if datetime.now() < start:
                st.warning("系统还未开放")
            elif start <= datetime.now():
                column_config = {
                    "CourseName": {"label": "课程名"},
                    "TeacherName": {"label": "教师"},
                    "selected_count": {"label": "选课人数"},
                    "selection_percentage": st.column_config.ProgressColumn(
                        "选课比例",
                        min_value=0,
                        max_value=100,
                        format="%d%%",
                    ),
                }
                pre_course_stats = get_precourse_statistics(st.session_state.conn)
                st.data_editor(
                    pre_course_stats,
                    width=1400,
                    height=300,
                    column_config=column_config,
                    num_rows="dynamic",
                )
            if datetime.now() > end:
                st.write("教评与选课已完成")
        elif menu == "修改密码 🔑":
            st.subheader("修改密码 🔑")
            new_password = st.text_input("新密码", type="password")
            if st.button("修改密码"):
                if new_password and new_password != st.session_state.user_roles['password_root'][0]:
                    change_password(st.session_state.conn, st.session_state.username, new_password)
                    st.session_state.user_roles['password_root'][0] = new_password
                    save_user_roles(st.session_state.user_roles)
                    st.success("密码修改成功！")
                elif new_password == st.session_state.user_roles['password_root'][0]:
                    st.warning("新密码不能与旧密码相同！")
                else:
                    st.warning("请输入新密码！")
        if st.button("退出登录 🔒"):
            st.session_state.user_roles['login'] = ['0']
            save_user_roles(st.session_state.user_roles)
            st.experimental_rerun()
    elif st.session_state.permission == 'teacher':
        menu = st.sidebar.radio("教师模式", ["信息查询 🧐", "成绩录入 ✍️", "班级交流区 💬", "教务通知 📢","修改密码 🔑"])
        if menu == "信息查询 🧐":
            # 获取教师信息
            st.subheader("教师信息 🧐")
            data = get_teachers_data(st.session_state.conn, st.session_state.teacher_id)
            config = {
                "TeacherID": {"label": "教师ID"},
                "TeacherName": {"label": "教师"},
                "Email": {"label": "邮箱"},
                "Position": {"label": "职位"},
                "sex": {"label": "性别"},
            }
            edited = st.data_editor(
                data,
                width=1400,
                height=100,
                column_config=config,
                num_rows="dynamic",
            )
            if st.button("更新信息"):
                update_teachers_data(st.session_state.conn, edited)
                st.success("信息更新成功！")
            st.subheader("班级信息")
            class_ = get_teacher_class(st.session_state.conn, st.session_state.teacher_id)
            config = {
                "StudentID": {"label": "学号"},
                "StudentName": {"label": "姓名"},
                "Major": {"label": "专业"},
            }
            st.data_editor(
                class_,
                width=1400,
                height=300,
                column_config=config,
                num_rows="dynamic",
            )
        elif menu == "成绩录入 ✍️":
            st.subheader("成绩录入 ✍️")
            class_ = get_class_grade(st.session_state.conn, st.session_state.teacher_id)
            column_config = {
                "StudentID": {"label": "学生ID"},
                "CourseName": {"label": "课程名"},
                "StudentName": {"label": "学生"},
                "Major": {"label": "专业"},
                "Grade": {"label": "成绩"},
            }
            edited = st.data_editor(
                class_,
                width=1400,
                height=300,
                column_config=column_config,
                disabled=["CourseName", "StudentName", "Major"],
                num_rows="dynamic",
            )
            if st.button("录入成绩"):
                update_grade(st.session_state.conn, edited, st.session_state.teacher_id)
                st.success("成绩录入成功！")
        elif menu == "班级交流区 💬":
            st.subheader("班级交流区 💬")
            message_list = get_message(st.session_state.conn, st.session_state.teacher_id)
            message_list = message_list.rename(columns={
                'SpeakerType': '身份',
                'SpeakerName': '发言人',
                'Content': '内容',
                'Timestamp': '发布时间',
            })
            st.table(message_list)
            message = st.text_area("输入消息")
            if st.button("发送消息"):
                Teacher_send_message(st.session_state.conn, st.session_state.teacher_id, message)
                st.success("消息发送成功！")
            message_delete = st.selectbox("选择要撤回的消息", message_list[message_list['发言人'] == get_teachers_data(st.session_state.conn,st.session_state.teacher_id)['TeacherName'][0]]['内容'])
            if st.button("撤回消息"):
                delete_message_class(st.session_state.conn, message_delete, get_teachers_data(st.session_state.conn,st.session_state.teacher_id)['TeacherName'][0])
                st.success("消息撤回成功！")
        elif menu == "教务通知 📢":
            st.subheader("教务通知 📢")
            message_list = get_academic_notices(st.session_state.conn)
            message_list = message_list.rename(columns={
                'NotificationID': 'ID',
                'Title': '通知标题',
                'Content': '通知内容',
                'Publisher': '发布人',
                'PublishDate': '发布时间',
                'EffectiveDate': '生效日期',
                'ExpirationDate': '到期日期',
                'Status': '状态'
            })
            st.dataframe(message_list, width=1400, height=300)
        elif menu == "修改密码 🔑":
            st.subheader("修改密码 🔑")
            new_password = st.text_input("新密码", type="password")
            if st.button("修改密码"):
                if new_password and new_password != st.session_state.user_roles['password_teacher'][0]:
                    change_password(st.session_state.conn, st.session_state.teacher_id, new_password)
                    st.session_state.user_roles['password_teacher'][0] = new_password
                    save_user_roles(st.session_state.user_roles)
                    st.success("密码修改成功！")
                elif new_password == st.session_state.user_roles['password_teacher'][0]:
                    st.warning("新密码不能与旧密码相同！")
                else:
                    st.warning("请输入新密码！")
        if st.button("退出登录 🔒"):
            st.session_state.user_roles['login'] = ['0']
            save_user_roles(st.session_state.user_roles)
            st.experimental_rerun()
    elif st.session_state.permission == 'student':
        menu = st.sidebar.radio("学生模式", ["信息查询 🧐", "教学评价与课程预选 📚", "班级交流区 💬", "教务通知 📢", "修改密码 🔑"])
        if menu == "信息查询 🧐":
            st.subheader("信息查询 🧐")
            data = get_students_data(st.session_state.conn, st.session_state.student_id)
            config = {
                "StudentID": {"label": "学生ID"},
                "StudentName": {"label": "学生"},
                "Email": {"label": "邮箱"},
                "Major": {"label": "专业"},
                "Grade": {"label": "年级"},
                "sex": {"label": "性别"},
            }
            edited = st.data_editor(
                data,
                width=1400,
                height=100,
                column_config=config,
                num_rows="dynamic",
            )
            if st.button("更新信息"):
                update_students_data(st.session_state.conn, edited)
                st.success("信息更新成功！")
            st.subheader("课程信息")
            course = get_student_course(st.session_state.conn, st.session_state.student_id)
            course = course.rename(columns={
                "StudentID": "学号",
                "StudentName": "姓名",
                "CourseName": "课程名",
                "Grade": "成绩",
            })
            st.table(course)
        elif menu == "教学评价与课程预选 📚":
            st.subheader("教学评价与课程预选 📚")
            if time.time() < float(st.session_state.user_roles['start_time'][0]):
                st.warning("系统还未开放")
            elif float(st.session_state.user_roles['start_time'][0]) <= time.time() and time.time() <= float(st.session_state.user_roles['end_time'][0]):
                st.subheader("教学评价")
                table = get_student_review(st.session_state.conn, st.session_state.student_id)
                table = table.rename(columns={
                    "CourseName": "课程名",
                    "Grade": "评分",
                })
                st.table(table)
                course = get_student_course(st.session_state.conn, st.session_state.student_id)
                course_name = st.selectbox("选择课程", course["CourseName"])
                grade = st.number_input("请输入课程评分", min_value=0, max_value=100)
                if st.button("提交评价"):
                    # 查看是否已经评价
                    if course_name in table["课程名"].values:
                        Student_review(st.session_state.conn, course_name, st.session_state.student_id, grade, update=True)
                        st.success("更新评价成功！")
                    else:
                        Student_review(st.session_state.conn, course_name, st.session_state.student_id, grade, update=False)
                        st.success("评价成功！")
                st.subheader("课程预选")
                st.write("课程预选时间为", datetime.fromtimestamp(float(st.session_state.user_roles['start_time'][0])).strftime("%Y-%m-%d %H:%M:%S"),
                         "至", datetime.fromtimestamp(float(st.session_state.user_roles['end_time'][0])).strftime("%Y-%m-%d %H:%M:%S"))
                data = get_student_pre_course(st.session_state.conn, st.session_state.student_id)
                st.write("课程列表")
                course_list = get_course(st.session_state.conn)
                course_list = course_list.rename(columns={
                    "CourseID": "课程ID",
                    "CourseName": "课程名",
                    "Credits": "学分",
                    "TeacherID": "教师ID",
                })
                st.table(course_list)
                st.write("已选课程")
                data = data.rename(columns={
                    "CourseName": "课程名",
                    "Credits": "学分",
                })
                st.table(data)
                st.write("学分上限为10分")
                st.write("已选学分为", get_student_pre_course(st.session_state.conn, st.session_state.student_id)["Credits"].sum())
                course = get_course(st.session_state.conn)
                course_name = st.selectbox("选择课程", course["CourseName"])
                if st.button("预选课程"):
                    if course_name in data["课程名"].values:
                        st.warning("已经预选过该课程！")
                    else:
                        # 学分是否超过限制
                        if data["学分"].sum() + course[course["CourseName"] == course_name]["Credits"].values[0] > 10:
                            st.warning("学分超过10分上限！")
                        else:
                            Student_pre_course(st.session_state.conn, course_name, st.session_state.student_id)
                            st.success("课程预选成功！")
                course_delete = st.selectbox("选择要删除的课程", get_student_pre_course(st.session_state.conn, st.session_state.student_id)["CourseName"])
                if st.button("删除课程"):
                    Student_delete_pre_course(st.session_state.conn, course_delete, st.session_state.student_id)
                    st.success("课程删除成功！")
            else:
                st.write("教评与选课已结束")
        elif menu == "班级交流区 💬":
            st.subheader("班级交流区 💬")
            course = st.selectbox("选择课程", get_student_course(st.session_state.conn, st.session_state.student_id)["CourseName"])
            message_list = get_message_course(st.session_state.conn, course)
            message_list = message_list.rename(columns={
                'SpeakerType': '身份',
                'SpeakerName': '发言人',
                'Content': '内容',
                'Timestamp': '发布时间',
            })
            st.table(message_list)
            message = st.text_area("输入消息")
            if st.button("发送消息"):
                Student_send_message(st.session_state.conn, course, st.session_state.student_id, message)
                st.success("消息发送成功！")
            message_delete = st.selectbox("选择要撤回的消息", message_list[message_list['发言人'] == get_students_data(st.session_state.conn, st.session_state.student_id)['StudentName'][0]]['内容'])
            if st.button("撤回消息"):
                delete_message_class(st.session_state.conn, message_delete, get_students_data(st.session_state.conn, st.session_state.student_id)['StudentName'][0])
                st.success("消息撤回成功！")
        elif menu == "教务通知 📢":
            st.subheader("教务通知 📢")
            message_list = get_academic_notices(st.session_state.conn)
            message_list = message_list.rename(columns={
                'NotificationID': 'ID',
                'Title': '通知标题',
                'Content': '通知内容',
                'Publisher': '发布人',
                'PublishDate': '发布时间',
                'EffectiveDate': '生效日期',
                'ExpirationDate': '到期日期',
                'Status': '状态'
            })
            st.dataframe(message_list, width=1400, height=300)
        elif menu == '修改密码 🔑':
            st.subheader("修改密码 🔑")
            new_password = st.text_input("新密码", type="password")
            if st.button("修改密码"):
                if new_password and new_password != st.session_state.user_roles['password_student'][0]:
                    change_password(st.session_state.conn, st.session_state.student_id, new_password)
                    st.session_state.user_roles['password_student'][0] = new_password
                    save_user_roles(st.session_state.user_roles)
                    st.success("密码修改成功！")
                elif new_password == st.session_state.user_roles['password_student'][0]:
                    st.warning("新密码不能与旧密码相同！")
                else:
                    st.warning("请输入新密码！")
        if st.button("退出登录 🔒"):
            st.session_state.user_roles['login'] = ['0']
            save_user_roles(st.session_state.user_roles)
            st.experimental_rerun()
