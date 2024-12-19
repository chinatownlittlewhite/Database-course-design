import pandas as pd


def get_teachers_data(conn, teacher_id):
    query = f"SELECT * FROM teachers WHERE TeacherID = {teacher_id}"
    return pd.read_sql(query, conn)

def update_teachers_data(conn, data):
    for index, row in data.iterrows():
        update_query = """
        UPDATE teachers
        SET TeacherName = ?, Email = ?, Position = ?, sex = ?
        WHERE TeacherID = ?
        """
        with conn.cursor() as cursor:
            cursor.execute(update_query, row['TeacherName'], row['Email'], row['Position'], row['sex'], row['TeacherID'])
            conn.commit()

def get_teacher_class(conn, teacher_id):
    query = f"SELECT s.StudentID, s.StudentName, s.Major FROM students s JOIN course_enrollments ce ON s.StudentID = ce.StudentID JOIN courses c ON ce.CourseID = c.CourseID WHERE c.TeacherID = {teacher_id}"
    return pd.read_sql(query, conn)

def get_class_grade(conn, teacher_id):
    query = f"SELECT s.StudentID, s.StudentName, s.Major, ce.Grade FROM students s JOIN course_enrollments ce ON s.StudentID = ce.StudentID JOIN courses c ON ce.CourseID = c.CourseID WHERE c.TeacherID = {teacher_id}"
    return pd.read_sql(query, conn)

def update_grade(conn, data, teacher_id):
    for index, row in data.iterrows():
        update_query = """
        UPDATE course_enrollments
        SET Grade = ?
        WHERE StudentID = ? AND CourseID = (SELECT CourseID FROM courses WHERE TeacherID = ?)
        """
        with conn.cursor() as cursor:
            cursor.execute(update_query, row['Grade'], row['StudentID'], teacher_id)
            conn.commit()

def get_message(conn, teacher_id):
    query = f"SELECT ci.SpeakerType, ci.SpeakerName, ci.Content, ci.Timestamp FROM teachers t JOIN courses c ON t.TeacherID = c.TeacherID JOIN class_interaction ci ON c.CourseID = ci.CourseID WHERE t.TeacherID = {teacher_id} ORDER BY ci.Timestamp;"
    return pd.read_sql(query, conn)

def delete_message_class(conn, message, name):
    query = f"DELETE FROM class_interaction WHERE CAST(Content AS VARCHAR(MAX)) LIKE '{message}' AND SpeakerName = '{name}'"
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()

def Teacher_send_message(conn, teacher_id, message):
    query = f"INSERT INTO class_interaction (CourseID, SpeakerType, SpeakerName, Content) VALUES ((SELECT CourseID FROM courses WHERE TeacherID = '{teacher_id}'), '教师', (SELECT TeacherName FROM teachers WHERE TeacherID = '{teacher_id}'), '{message}')"
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()