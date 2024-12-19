import pandas as pd


def get_teachers(conn):
    # 从数据库获取教师信息
    query = "SELECT * FROM teachers"
    return pd.read_sql(query, conn)

def add_teacher(conn, teacher_id, name, email, position, sex):
    # 向数据库添加教师
    query = f"INSERT INTO teachers (TeacherID, TeacherName, Email, Position, Sex) VALUES ({teacher_id}, '{name}', '{email}', '{position}', '{sex}')"
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()

def update_teachers(conn, teachers):
    for index, row in teachers.iterrows():
        update_query = """
        UPDATE teachers
        SET TeacherName = ?, Email = ?, Position = ?, Sex = ?
        WHERE TeacherID = ?
        """
        with conn.cursor() as cursor:
            cursor.execute(update_query, row['TeacherName'], row['Email'], row['Position'], row['sex'], row['TeacherID'])
        conn.commit()
def delete_teacher(conn, name):
    # 删除教师信息
    query = f"DELETE FROM teachers WHERE TeacherName = '{name}'"
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()

def find_teacher_class(conn, teacher):
    query = f"SELECT s.StudentID, s.StudentName, c.CourseName, ce.Grade FROM teachers t JOIN courses c ON t.TeacherID = c.TeacherID JOIN course_enrollments ce ON c.CourseID = ce.CourseID JOIN students s ON ce.StudentID = s.StudentID WHERE t.TeacherName = '{teacher}';"
    return pd.read_sql(query, conn)

def get_students(conn):
    # 从数据库获取学生信息
    query = "SELECT * FROM students"
    return pd.read_sql(query, conn)

def get_academic_notices(conn):
    query = "SELECT * FROM academic_notices"
    return pd.read_sql(query, conn)

def send_academic_notice(conn, title, content, identity, start_time, end_time):
    query = f"INSERT INTO academic_notices (Title, Content, Publisher, EffectiveDate, ExpirationDate) VALUES ('{title}', '{content}', '{identity}', '{start_time}', '{end_time}')"
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()

def delete_academic_notice(conn, Title):
    query = f"DELETE FROM academic_notices WHERE Title = '{Title}'"
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()

# def get_course_statistics(conn):
#     query = """
#     SELECT c.CourseName, t.TeacherName,
#            COUNT(sc.StudentID) AS selected_count,
#            COUNT(sc.StudentID) * 100.0 / (SELECT COUNT(*) FROM students) AS selection_percentage
#     FROM courses c
#     LEFT JOIN course_enrollments sc ON c.CourseID = sc.CourseID
#     LEFT JOIN teachers t ON c.TeacherID = t.TeacherID
#     GROUP BY c.CourseName, t.TeacherName
#     ORDER BY selection_percentage DESC;
#     """
#     return pd.read_sql(query, conn)

def get_course_statistics(conn):
    query = "SELECT * FROM CourseStatistics;"
    return pd.read_sql(query, conn)


# def get_grade_statistics(conn):
#     query = """
#     SELECT c.CourseName,
#            AVG(g.Grade) AS avg_grade,
#            MAX(g.Grade) AS max_grade,
#            MIN(g.Grade) AS min_grade,
#            COUNT(G.StudentID) AS student_count
#     FROM courses c
#     LEFT JOIN course_enrollments g ON c.CourseID = g.CourseID
#     GROUP BY c.CourseName
#     ORDER BY avg_grade DESC;
#     """
#
#     return pd.read_sql(query, conn)

def get_grade_statistics(conn):
    query = "SELECT * FROM GradeStatistics;"
    return pd.read_sql(query, conn)


def get_message_course(conn, course_name):
    query = f"SELECT ci.SpeakerType, ci.SpeakerName, ci.Content, ci.Timestamp FROM courses c JOIN class_interaction ci ON c.CourseID = ci.CourseID WHERE c.CourseName = '{course_name}' ORDER BY ci.Timestamp;"
    return pd.read_sql(query, conn)

def get_courses_grade(conn):
    query = """
    SELECT
    c.CourseName,
    COUNT(r.StudentID) AS review_count,
    AVG(r.Grade) AS average_score,
    COUNT(r.StudentID) * 100.0 / (SELECT COUNT(*) FROM course_enrollments ce WHERE ce.CourseID = c.CourseID) AS review_percentage
    FROM courses c
    LEFT JOIN apprise r ON c.CourseID = r.CourseID
    GROUP BY c.CourseID, c.CourseName
    ORDER BY review_percentage DESC;
    """
    return pd.read_sql(query, conn)

def get_precourse_statistics(conn):
    query = """
    SELECT c.CourseName, t.TeacherName, 
           COUNT(sc.StudentID) AS selected_count,
           COUNT(sc.StudentID) * 100.0 / (SELECT COUNT(*) FROM students) AS selection_percentage
    FROM courses c
    LEFT JOIN pre_select_course sc ON c.CourseID = sc.CourseID
    LEFT JOIN teachers t ON c.TeacherID = t.TeacherID
    GROUP BY c.CourseName, t.TeacherName
    ORDER BY selection_percentage DESC;
    """
    return pd.read_sql(query, conn)

def change_password(conn, username, new_password):
    query = f"ALTER LOGIN {username} WITH PASSWORD = '{new_password}'"
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()

def add_student(conn, student_id, name, email, major, grade, sex):
    # 向数据库添加学生
    query = f"INSERT INTO students (StudentID, StudentName, Email, Major, Grade, Sex) VALUES ({student_id}, '{name}', '{email}', '{major}', {grade}, '{sex}')"
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()

def delete_student(conn, name):
    # 删除学生信息
    query = f"DELETE FROM students WHERE StudentName = '{name}'"
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()

def find_student_course(conn, student):
    query = f"SELECT s.StudentID, s.StudentName, c.CourseName, ce.Grade FROM students s JOIN course_enrollments ce ON s.StudentID = ce.StudentID JOIN courses c ON ce.CourseID = c.CourseID WHERE s.StudentName = '{student}';"
    return pd.read_sql(query, conn)