import pandas as pd
import pyodbc
import streamlit as st
# 读取用户角色数据
def load_user_roles():
    try:
        with open("./utils/user_roles.txt", 'r') as file:
            lines = file.readlines()
            user_roles = {}
            for line in lines:
                if line.strip():  # 确保跳过空行
                    role, permissions = line.strip().split(':')
                    user_roles[role] = permissions.split(',')
            if user_roles['login'] == ['1']:
                user_roles['login'] = ['0']
            user_roles['start_time'][0] = float(user_roles['start_time'][0].strip("[']"))
            user_roles['end_time'][0] = float(user_roles['end_time'][0].strip("[']"))
            return user_roles
    except FileNotFoundError:
        user_roles = {'root': ['root'], 'teacher': ['teacher'], 'student': ['student'], 'login': 0, 'start_time': 0, 'end_time': 0, 'password_root': "123456", 'password_teacher': "123456", 'password_student': "123456"}
        save_user_roles(user_roles)  # 如果文件不存在，创建默认用户角色
        return user_roles

# 保存用户角色数据到文件
def save_user_roles(user_roles):
    with open("./utils/user_roles.txt", 'w') as file:
        for role, permissions in user_roles.items():
            # 将权限列表转换为字符串
            if role != 'start_time' and role != 'end_time':
                permissions_str = ','.join(permissions) if isinstance(permissions, list) else str(permissions)
            else:
                permissions_str = permissions
            file.write(f"{role}:{permissions_str}\n")

# 定义连接函数
def connect_to_database(username, password):
    """
    根据用户提供的凭据连接 SQL Server 数据库。
    """
    try:
        connection_string = (
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER=localhost;DATABASE=demo;UID={username};PWD={password};TrustServerCertificate=yes"
        )
        connection = pyodbc.connect(connection_string)
        return connection
    except pyodbc.Error as e:
        st.error(f"连接失败: {e}")
        return None

def get_student_password(conn, StudentID):
    query = f"SELECT Password FROM student_passwords WHERE StudentID = {StudentID}"
    return pd.read_sql(query, conn)

def get_teacher_password(conn, TeacherID):
    query = f"SELECT Password FROM teacher_passwords WHERE TeacherID = {TeacherID}"
    return pd.read_sql(query, conn)