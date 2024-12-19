-- 教师表
CREATE TABLE teachers (
    TeacherID INT PRIMARY KEY,
    TeacherName NVARCHAR(100),
    Email NVARCHAR(100),
    Position NVARCHAR(50)
);

-- 学生表
CREATE TABLE students (
    StudentID INT PRIMARY KEY,
    StudentName NVARCHAR(100),
    Email NVARCHAR(100),
    Major NVARCHAR(50),
    Grade NVARCHAR(20)
);

-- 课程表
CREATE TABLE courses (
    CourseID INT PRIMARY KEY,
    CourseName NVARCHAR(100),
    Credits INT,
    TeacherID INT,
    FOREIGN KEY (TeacherID) REFERENCES teachers(TeacherID)
);

-- 选课表
CREATE TABLE course_enrollments (
    EnrollmentID INT PRIMARY KEY IDENTITY(1,1),
    StudentID INT,
    CourseID INT,
    Grade INT CHECK (Grade >= 0 AND Grade <= 100),
    FOREIGN KEY (StudentID) REFERENCES students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES courses(CourseID)
);
-- 预选课表
CREATE TABLE pre_select_course (
    EnrollmentID INT PRIMARY KEY IDENTITY(1,1),
    StudentID INT,
    CourseID INT,
    FOREIGN KEY (StudentID) REFERENCES students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES courses(CourseID))

CREATE TABLE apprise (
    StudentID INT,
    CourseID INT,
	Grade INT CHECK (Grade >= 0 AND Grade <= 100),
    FOREIGN KEY (StudentID) REFERENCES students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES courses(CourseID))


INSERT INTO teachers (TeacherID, TeacherName, Email, Position)
VALUES
    (001,'李刚', 'ligang@jxnu.edu.cn', '教授'),
    (002,'王丽', 'wangli@jxnu.edu.cn', '讲师'),
    (003,'赵勇', 'zhaoyong@jxnu.edu.cn', '副教授'),
    (004,'孙婷', 'sunting@jxnu.edu.cn', '讲师'),
    (005,'陈杰', 'chenjie@jxnu.edu.cn', '教授');



-- 插入课程数据
INSERT INTO courses (CourseID, CourseName, Credits, TeacherID)
VALUES
    (001,'数据结构', 4, 1),  -- 李刚教授
    (002,'算法分析与设计', 3, 2),  -- 王丽讲师
    (003,'操作系统', 4, 3),  -- 赵勇副教授
    (004,'计算机网络', 3, 4),  -- 孙婷讲师
    (005,'数据库系统', 3, 5);  -- 陈杰教授
-- 插入更多学生数据
INSERT INTO students (StudentID, StudentName, Email, Major, Grade)
VALUES
    (20240006, '陈宇', 'chenyu@jxnu.edu.cn', '计算机科学与技术', '2024'),
    (20240007, '刘凯', 'liukai@jxnu.edu.cn', '数学与应用数学', '2024'),
    (20240008, '张浩', 'zhanghao@jxnu.edu.cn', '软件工程', '2024'),
    (20240009, '李娜', 'lina@jxnu.edu.cn', '电子信息工程', '2024'),
    (20240010, '赵强', 'zhaoqiang@jxnu.edu.cn', '机械工程', '2024'),
    (20240011, '黄雪', 'huangxue@jxnu.edu.cn', '会计学', '2024'),
    (20240012, '王芳', 'wangfang@jxnu.edu.cn', '土木工程', '2024'),
    (20240013, '孙志', 'suzhi@jxnu.edu.cn', '材料科学与工程', '2024'),
    (20240014, '周晨', 'zhoucheng@jxnu.edu.cn', '电子信息工程', '2024'),
    (20240015, '张翔', 'zhangxiang@jxnu.edu.cn', '计算机科学与技术', '2024'),
    (20240016, '李超', 'lichao@jxnu.edu.cn', '国际经济与贸易', '2024'),
    (20240017, '王晨', 'wangchen@jxnu.edu.cn', '化学工程', '2024'),
    (20240018, '陈梅', 'chenmei@jxnu.edu.cn', '金融学', '2024'),
    (20240019, '李娜', 'lina2024@jxnu.edu.cn', '信息管理与信息系统', '2024'),
    (20240020, '刘刚', 'liugang@jxnu.edu.cn', '土木工程', '2024'),
    (20240021, '赵凯', 'zhaokai@jxnu.edu.cn', '生物工程', '2024'),
    (20240022, '王波', 'wangbo@jxnu.edu.cn', '通信工程', '2024'),
    (20240023, '周颖', 'zhouying@jxnu.edu.cn', '新闻传播学', '2024'),
    (20240024, '孙林', 'sunlin@jxnu.edu.cn', '环境工程', '2024'),
    (20240025, '张敏', 'zhangmin@jxnu.edu.cn', '统计学', '2024'),
    (20240026, '王宏', 'wanghong@jxnu.edu.cn', '艺术设计', '2024'),
    (20240027, '李亮', 'liliang@jxnu.edu.cn', '人力资源管理', '2024'),
    (20240028, '赵丽', 'zhaoli@jxnu.edu.cn', '机械工程', '2024'),
    (20240029, '陈鑫', 'chenxin@jxnu.edu.cn', '市场营销', '2024'),
    (20240030, '黄丽', 'huangli@jxnu.edu.cn', '法学', '2024');
-- 插入选课数据（每个学生选修多门课程）
INSERT INTO course_enrollments (StudentID, CourseID, Grade)
VALUES
    (20240006, 1, 85),  -- 陈宇选修数据结构，成绩85
    (20240006, 2, 78),  -- 陈宇选修算法分析与设计，成绩78
    (20240007, 1, 92),  -- 刘凯选修数据结构，成绩92
    (20240007, 3, 88),  -- 刘凯选修操作系统，成绩88
    (20240008, 1, 75),  -- 张浩选修数据结构，成绩75
    (20240008, 4, 80),  -- 张浩选修计算机网络，成绩80
    (20240009, 2, 90),  -- 李娜选修算法分析与设计，成绩90
    (20240009, 5, 85),  -- 李娜选修数据库系统，成绩85
    (20240010, 3, 80),  -- 赵强选修操作系统，成绩80
    (20240010, 4, 87),  -- 赵强选修计算机网络，成绩87
    (20240011, 5, 91),  -- 黄雪选修数据库系统，成绩91
    (20240011, 2, 86),  -- 黄雪选修算法分析与设计，成绩86
    (20240012, 3, 82),  -- 王芳选修操作系统，成绩82
    (20240012, 4, 79),  -- 王芳选修计算机网络，成绩79
    (20240013, 1, 89),  -- 孙志选修数据结构，成绩89
    (20240013, 2, 84),  -- 孙志选修算法分析与设计，成绩84
    (20240014, 5, 94),  -- 周晨选修数据库系统，成绩94
    (20240014, 3, 78),  -- 周晨选修操作系统，成绩78
    (20240015, 4, 80),  -- 张翔选修计算机网络，成绩80
    (20240015, 1, 91),  -- 张翔选修数据结构，成绩91
    (20240016, 2, 88),  -- 李超选修算法分析与设计，成绩88
    (20240016, 5, 83),  -- 李超选修数据库系统，成绩83
    (20240017, 1, 90),  -- 王晨选修数据结构，成绩90
    (20240017, 4, 85),  -- 王晨选修计算机网络，成绩85
    (20240018, 3, 86),  -- 陈梅选修操作系统，成绩86
    (20240018, 5, 92),  -- 陈梅选修数据库系统，成绩92
    (20240019, 2, 78),  -- 李娜选修算法分析与设计，成绩78
    (20240019, 4, 95),  -- 李娜选修计算机网络，成绩95
    (20240020, 1, 93),  -- 刘刚选修数据结构，成绩93
    (20240020, 3, 82),  -- 刘刚选修操作系统，成绩82
    (20240021, 2, 80),  -- 赵凯选修算法分析与设计，成绩80
    (20240021, 4, 77),  -- 赵凯选修计算机网络，成绩77
    (20240022, 1, 88),  -- 王波选修数据结构，成绩88
    (20240022, 5, 84),  -- 王波选修数据库系统，成绩84
    (20240023, 3, 91),  -- 周颖选修操作系统，成绩91
    (20240023, 2, 89),  -- 周颖选修算法分析与设计，成绩89
    (20240024, 4, 93),  -- 孙林选修计算机网络，成绩93
    (20240024, 1, 85),  -- 孙林选修数据结构，成绩85
    (20240025, 2, 92),  -- 张敏选修算法分析与设计，成绩92
    (20240025, 5, 80),  -- 张敏选修数据库系统，成绩80
    (20240026, 1, 80),  -- 王宏选修数据结构，成绩80
    (20240026, 4, 77),  -- 王宏选修计算机网络，成绩77
    (20240027, 3, 93),  -- 李亮选修操作系统，成绩93
    (20240027, 2, 85),  -- 李亮选修算法分析与设计，成绩85
    (20240028, 5, 87),  -- 赵丽选修数据库系统，成绩87
    (20240028, 4, 91),  -- 赵丽选修计算机网络，成绩91
    (20240029, 1, 83),  -- 陈鑫选修数据结构，成绩83
    (20240029, 3, 88),  -- 陈鑫选修操作系统，成绩88
    (20240030, 2, 95);  -- 黄丽选修算法分析与设计，成绩95

INSERT INTO apprise(StudentID, CourseID, Grade)
VALUES
    (20240006, 1, 85),  -- 陈宇选修数据结构，成绩85
    (20240006, 2, 78),  -- 陈宇选修算法分析与设计，成绩78
    (20240007, 1, 92),  -- 刘凯选修数据结构，成绩92
    (20240007, 3, 88),  -- 刘凯选修操作系统，成绩88
    (20240008, 1, 75),  -- 张浩选修数据结构，成绩75
    (20240008, 4, 80),  -- 张浩选修计算机网络，成绩80
    (20240009, 2, 90),  -- 李娜选修算法分析与设计，成绩90
    (20240009, 5, 85),  -- 李娜选修数据库系统，成绩85
    (20240010, 3, 80),  -- 赵强选修操作系统，成绩80
    (20240010, 4, 87),  -- 赵强选修计算机网络，成绩87
    (20240011, 5, 91),  -- 黄雪选修数据库系统，成绩91
    (20240011, 2, 86),  -- 黄雪选修算法分析与设计，成绩86
    (20240012, 3, 82),  -- 王芳选修操作系统，成绩82
    (20240012, 4, 79),  -- 王芳选修计算机网络，成绩79
    (20240013, 1, 89),  -- 孙志选修数据结构，成绩89
    (20240013, 2, 84),  -- 孙志选修算法分析与设计，成绩84
    (20240014, 5, 94),  -- 周晨选修数据库系统，成绩94
    (20240014, 3, 78),  -- 周晨选修操作系统，成绩78
    (20240015, 4, 80),  -- 张翔选修计算机网络，成绩80
    (20240015, 1, 91),  -- 张翔选修数据结构，成绩91
    (20240016, 2, 88),  -- 李超选修算法分析与设计，成绩88
    (20240016, 5, 83),  -- 李超选修数据库系统，成绩83
    (20240017, 1, 90),  -- 王晨选修数据结构，成绩90
    (20240017, 4, 85),  -- 王晨选修计算机网络，成绩85
    (20240018, 3, 86),  -- 陈梅选修操作系统，成绩86
    (20240018, 5, 92),  -- 陈梅选修数据库系统，成绩92
    (20240019, 2, 78),  -- 李娜选修算法分析与设计，成绩78
    (20240019, 4, 95),  -- 李娜选修计算机网络，成绩95
    (20240020, 1, 93),  -- 刘刚选修数据结构，成绩93
    (20240020, 3, 82),  -- 刘刚选修操作系统，成绩82
    (20240021, 2, 80),  -- 赵凯选修算法分析与设计，成绩80
    (20240021, 4, 77),  -- 赵凯选修计算机网络，成绩77
    (20240022, 1, 88),  -- 王波选修数据结构，成绩88
    (20240022, 5, 84),  -- 王波选修数据库系统，成绩84
    (20240023, 3, 91),  -- 周颖选修操作系统，成绩91
    (20240023, 2, 89),  -- 周颖选修算法分析与设计，成绩89
    (20240024, 4, 93),  -- 孙林选修计算机网络，成绩93
    (20240024, 1, 85),  -- 孙林选修数据结构，成绩85
    (20240025, 2, 92),  -- 张敏选修算法分析与设计，成绩92
    (20240025, 5, 80),  -- 张敏选修数据库系统，成绩80
    (20240026, 1, 80),  -- 王宏选修数据结构，成绩80
    (20240026, 4, 77),  -- 王宏选修计算机网络，成绩77
    (20240027, 3, 93),  -- 李亮选修操作系统，成绩93
    (20240027, 2, 85),  -- 李亮选修算法分析与设计，成绩85
    (20240028, 5, 87),  -- 赵丽选修数据库系统，成绩87
    (20240028, 4, 91),  -- 赵丽选修计算机网络，成绩91
    (20240029, 1, 83),  -- 陈鑫选修数据结构，成绩83
    (20240029, 3, 88),  -- 陈鑫选修操作系统，成绩88
    (20240030, 2, 95);  -- 黄丽选修算法分析与设计，成绩95

INSERT INTO pre_select_course(StudentID, CourseID)
VALUES
    (20240006, 1),  -- 陈宇选修数据结构
    (20240006, 2),  -- 陈宇选修算法分析与设计
    (20240007, 1),  -- 刘凯选修数据结构
    (20240007, 3),  -- 刘凯选修操作系统
    (20240008, 1),  -- 张浩选修数据结构
    (20240008, 4),  -- 张浩选修计算机网络
    (20240009, 2),  -- 李娜选修算法分析与设计
    (20240009, 5),  -- 李娜选修数据库系统
    (20240010, 3),  -- 赵强选修操作系统
    (20240010, 4),  -- 赵强选修计算机网络
    (20240011, 5),  -- 黄雪选修数据库系统
    (20240011, 2),  -- 黄雪选修算法分析与设计
    (20240012, 3),  -- 王芳选修操作系统
    (20240012, 4),  -- 王芳选修计算机网络
    (20240013, 1),  -- 孙志选修数据结构
    (20240013, 2),  -- 孙志选修算法分析与设计
    (20240014, 5),  -- 周晨选修数据库系统
    (20240014, 3),  -- 周晨选修操作系统
    (20240015, 4),  -- 张翔选修计算机网络
    (20240015, 1),  -- 张翔选修数据结构
    (20240016, 2),  -- 李超选修算法分析与设计
    (20240016, 5),  -- 李超选修数据库系统
    (20240017, 1),  -- 王晨选修数据结构
    (20240017, 4),  -- 王晨选修计算机网络
    (20240018, 3),  -- 陈梅选修操作系统
    (20240018, 5),  -- 陈梅选修数据库系统
    (20240019, 2),  -- 李娜选修算法分析与设计
    (20240019, 4),  -- 李娜选修计算机网络
    (20240020, 1),  -- 刘刚选修数据结构
    (20240020, 3),  -- 刘刚选修操作系统
    (20240021, 2),  -- 赵凯选修算法分析与设计
    (20240021, 4),  -- 赵凯选修计算机网络
    (20240022, 1),  -- 王波选修数据结构
    (20240022, 5),  -- 王波选修数据库系统
    (20240023, 3),  -- 周颖选修操作系统
    (20240023, 2),  -- 周颖选修算法分析与设计
    (20240024, 4),  -- 孙林选修计算机网络
    (20240024, 1),  -- 孙林选修数据结构
    (20240025, 2),  -- 张敏选修算法分析与设计
    (20240025, 5),  -- 张敏选修数据库系统
    (20240026, 1),  -- 王宏选修数据结构
    (20240026, 4),  -- 王宏选修计算机网络
    (20240027, 3),  -- 李亮选修操作系统
    (20240027, 2),  -- 李亮选修算法分析与设计
    (20240028, 5),  -- 赵丽选修数据库系统
    (20240028, 4),  -- 赵丽选修计算机网络
    (20240029, 1),  -- 陈鑫选修数据结构
    (20240029, 3),  -- 陈鑫选修操作系统
    (20240030, 2);  -- 黄丽选修算法分析与设计


CREATE TABLE student_passwords (
    StudentID INT PRIMARY KEY,  -- 学号
    Password VARCHAR(255)       -- 密码
);

INSERT INTO student_passwords (StudentID, Password)
SELECT StudentID, CAST(StudentID AS VARCHAR(255)) AS Password
FROM students;

CREATE TABLE teacher_passwords (
    TeacherID INT PRIMARY KEY,  -- 教师ID
    Password VARCHAR(255)       -- 密码
);



INSERT INTO teacher_passwords (TeacherID, Password)
SELECT TeacherID, '123456' AS Password
FROM teachers;


CREATE TRIGGER trg_delete_student
ON students
AFTER DELETE
AS
BEGIN
    -- 删除学生的选课记录
    DELETE FROM course_enrollments
    WHERE StudentID IN (SELECT StudentID FROM deleted);
    
    DELETE FROM apprise
    WHERE StudentID IN (SELECT StudentID FROM deleted);

	DELETE FROM pre_select_course
    WHERE StudentID IN (SELECT StudentID FROM deleted);

	DELETE FROM student_passwords
    WHERE StudentID IN (SELECT StudentID FROM deleted);
END;

CREATE TRIGGER trg_delete_teacher
ON teachers
AFTER DELETE
AS
BEGIN
    DELETE FROM courses
    WHERE TeacherID IN (SELECT TeacherID FROM deleted);

	DELETE FROM teacher_passwords
    WHERE TeacherID IN (SELECT TeacherID FROM deleted);
    
    DELETE FROM apprise
    WHERE CourseID IN (SELECT CourseID FROM courses
    WHERE TeacherID IN (SELECT TeacherID FROM deleted));

    DELETE FROM pre_select_course
    WHERE CourseID IN (SELECT CourseID FROM courses
    WHERE TeacherID IN (SELECT TeacherID FROM deleted));
END;
-- 为 students 表添加 sex 列
ALTER TABLE students
ADD sex CHAR(1);

-- 为 teachers 表添加 sex 列
ALTER TABLE teachers
ADD sex CHAR(1);
-- 更新 students 表中的 sex 列为随机性别
UPDATE students
SET sex = CASE 
             WHEN ABS(CHECKSUM(NEWID())) % 2 = 0 THEN 'M' -- 随机生成 M 或 F
             ELSE 'F'
           END;

-- 更新 teachers 表中的 sex 列为随机性别
UPDATE teachers
SET sex = CASE 
             WHEN ABS(CHECKSUM(NEWID())) % 2 = 0 THEN 'M' -- 随机生成 M 或 F
             ELSE 'F'
           END;


CREATE TABLE class_interaction (
    InteractionID INT IDENTITY(1,1) PRIMARY KEY,  -- 自动生成的记录ID
    CourseID INT NOT NULL,  -- 班级号
    SpeakerType VARCHAR(50) NOT NULL,  -- 发言人身份
    SpeakerName VARCHAR(100) NOT NULL,  -- 发言人姓名
    Content TEXT NOT NULL,  -- 发言内容
    Timestamp DATETIME DEFAULT GETDATE()  -- 发言时间，默认为当前时间
);

INSERT INTO class_interaction (CourseID, SpeakerType, SpeakerName, Content)
VALUES
    (1, '学生', '陈康', '请问下次考试的范围是什么？'),
    (1, '教师', '李刚', '下次考试将包括第一章到第三章的内容'),
    (1, '学生', '陈康', '老师，关于课后的作业有什么要求吗？'),
    (1, '教师', '李刚', '课后作业需要提交一篇关于数据库的实验报告，具体要求已发布在课堂通知上'),
	(2, '学生', '陈康', '请问下次考试的范围是什么？'),
    (2, '教师', '王丽', '下次考试将包括第一章到第三章的内容'),
    (2, '学生', '陈康', '老师，关于课后的作业有什么要求吗？'),
    (2, '教师', '王丽', '课后作业需要提交一篇关于数据库的实验报告，具体要求已发布在课堂通知上'),
	(3, '学生', '陈康', '请问下次考试的范围是什么？'),
    (3, '教师', '赵勇', '下次考试将包括第一章到第三章的内容'),
    (3, '学生', '陈康', '老师，关于课后的作业有什么要求吗？'),
    (3, '教师', '赵勇', '课后作业需要提交一篇关于数据库的实验报告，具体要求已发布在课堂通知上'),
	(4, '学生', '陈康', '请问下次考试的范围是什么？'),
    (4, '教师', '孙婷', '下次考试将包括第一章到第三章的内容'),
    (4, '学生', '陈康', '老师，关于课后的作业有什么要求吗？'),
    (4, '教师', '孙婷', '课后作业需要提交一篇关于数据库的实验报告，具体要求已发布在课堂通知上'),
	(5, '学生', '陈康', '请问下次考试的范围是什么？'),
    (5, '教师', '陈杰', '下次考试将包括第一章到第三章的内容'),
    (5, '学生', '陈康', '老师，关于课后的作业有什么要求吗？'),
    (5, '教师', '陈杰', '课后作业需要提交一篇关于数据库的实验报告，具体要求已发布在课堂通知上');

drop table class_interaction

CREATE TABLE academic_notices (
    NotificationID INT IDENTITY(1,1) PRIMARY KEY,  -- 自动生成的通知ID
    Title VARCHAR(255) NOT NULL,  -- 通知标题
    Content TEXT NOT NULL,  -- 通知内容
    Publisher VARCHAR(100) NOT NULL,  -- 发布人（如：教务处、领导等）
    PublishDate DATETIME DEFAULT GETDATE(),  -- 发布日期，默认为当前时间
    EffectiveDate DATETIME,  -- 生效日期
    ExpirationDate DATETIME,  -- 到期日期
    Status VARCHAR(50) DEFAULT 'Active'  -- 状态，表示通知是否有效（'Active' 或 'Expired'）
);


INSERT INTO academic_notices (Title, Content, Publisher, EffectiveDate, ExpirationDate)
VALUES
    ('期末考试安排', '各位同学，期末考试安排已发布，请查收并提前准备。', '教务处', '2024-12-15', '2025-1-20'),
    ('课堂纪律提醒', '请同学们遵守课堂纪律，不得在课堂上使用手机。', '黄书记', '2024-12-01', '2025-06-30'),
    ('学期结束通知', '本学期的所有课程将于2024年1月15日结束，请及时完成课程任务。', '教务处', '2024-12-01', '2024-1-25');


DELETE FROM class_interaction WHERE CAST(Content AS VARCHAR(MAX)) like 'dsda'

