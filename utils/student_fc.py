import pandas as pd

def get_course(conn):
    query = "SELECT * FROM courses"
    return pd.read_sql(query, conn)

def update_students(conn, students):
    for index, row in students.iterrows():
        update_query = """
        UPDATE students
        SET StudentName = ?, Email = ?, Major = ?, Grade = ?, sex = ?
        WHERE StudentID = ?
        """
        with conn.cursor() as cursor:
            cursor.execute(update_query, row['StudentName'], row['Email'], row['Major'], row['Grade'], row['sex'],row['StudentID'])
        conn.commit()

def Student_send_message(conn, course, student_id, message):
    query = f"INSERT INTO class_interaction (CourseID, SpeakerType, SpeakerName, Content) VALUES ((SELECT CourseID FROM courses WHERE CourseName = '{course}'), '学生', (SELECT StudentName FROM students WHERE StudentID = '{student_id}'), '{message}')"
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()

def get_students_data(conn, student_id):
    query = f"SELECT * FROM students WHERE StudentID = {student_id}"
    return pd.read_sql(query, conn)

def update_students_data(conn, data):
    for index, row in data.iterrows():
        update_query = """
        UPDATE students
        SET StudentName = ?, Email = ?, Major = ?, Grade = ?, sex = ?
        WHERE StudentID = ?
        """
        with conn.cursor() as cursor:
            cursor.execute(update_query, row['StudentName'], row['Email'], row['Major'], row['Grade'], row['sex'], row['StudentID'])
            conn.commit()

def get_student_course(conn, student):
    query = f"SELECT s.StudentID, s.StudentName, c.CourseName, ce.Grade FROM students s JOIN course_enrollments ce ON s.StudentID = ce.StudentID JOIN courses c ON ce.CourseID = c.CourseID WHERE s.StudentID = '{student}';"
    return pd.read_sql(query, conn)

def get_student_review(conn, student_id):
    query = f"SELECT c.CourseName, r.Grade FROM apprise r JOIN courses c ON r.CourseID = c.CourseID WHERE r.StudentID = '{student_id}';"
    return pd.read_sql(query, conn)

def Student_review(conn, course, student_id, grade, update):
    if update == False:
        query = f"INSERT INTO apprise (CourseID, StudentID, Grade) VALUES ((SELECT CourseID FROM courses WHERE CourseName = '{course}'), '{student_id}', '{grade}')"
    else:
        query = f"UPDATE apprise SET Grade = '{grade}' WHERE CourseID = (SELECT CourseID FROM courses WHERE CourseName = '{course}') AND StudentID = '{student_id}'"
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()

def get_student_pre_course(conn, student_id):
    query = f"SELECT c.CourseName, c.Credits FROM pre_select_course ce JOIN courses c ON ce.CourseID = c.CourseID WHERE ce.StudentID = '{student_id}';"
    return pd.read_sql(query, conn)

def Student_pre_course(conn, course, student_id):
    query = f"INSERT INTO pre_select_course (CourseID, StudentID) VALUES ((SELECT CourseID FROM courses WHERE CourseName = '{course}'), '{student_id}')"
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()

def Student_delete_pre_course(conn, course, student_id):
    query = f"DELETE FROM pre_select_course WHERE CourseID = (SELECT CourseID FROM courses WHERE CourseName = '{course}') AND StudentID = '{student_id}'"
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()