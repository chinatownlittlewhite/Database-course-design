# 现代学生信息管理系统 (Modern Student Information System)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-ff69b4.svg)](https://streamlit.io/)
[![Database](https://img.shields.io/badge/Database-SQL%20Server-CC2927.svg)](https://www.microsoft.com/en-us/sql-server)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange.svg)]()

## 🌟 项目概览

本项目是一个基于 Streamlit 和 SQL Server 构建的现代化、一体化的学生信息管理系统。旨在解决传统教务管理中数据分散、更新滞后、权限混乱等痛点，为**学生、教师、管理员**三方提供一个高效、安全、便捷的在线平台。

系统通过清晰的角色划分和强大的后台数据库支持，实现了从个人信息维护、在线选课、成绩管理到教务通知、课堂交流的全流程数字化管理。

## ✨ 核心功能

<details>
<summary><b>👨‍🎓 学生端功能</b></summary>

- **个人中心**: 查询与修改个人基本信息（姓名、邮箱、专业等）。
- **选课系统**: 在线浏览课程列表，自由进行选课与退课操作。
- **成绩查询**: 实时查看所有已修课程的成绩。
- **教务通知**: 接收并查阅管理员发布的最新教务通知。
- **课堂互动**: 参与所选课程的在线交流区，与师生互动。

</details>

<details>
<summary><b>👩‍🏫 教师端功能</b></summary>

- **课程管理**: 查看自己所授课程列表及详细的选课学生名单。
- **成绩录入**: 方便地上传、修改和发布学生的课程成绩。
- **个人信息**: 管理个人基本资料。
- **信息获取**: 接收教务通知，参与课程交流。

</details>

<details>
<summary><b>⚙️ 管理员端功能</b></summary>

- **全方位管理**: 集中管理学生、教师和课程的基础信息。
- **信息发布**: 发布、更新和管理全校范围的教务通知。
- **社区监督**: 监管所有课程的交流区，确保和谐的交流环境。

</details>

## 🛠️ 技术栈

- **前端框架**: [Streamlit](https://streamlit.io/)
- **后端语言**: Python
- **数据库**: [SQL Server](https://www.microsoft.com/en-us/sql-server)
- **数据库连接**: `pyodbc` 或 `pymssql`

## 🚀 快速开始

请按照以下步骤在本地环境中部署和运行本系统。

### 1. 先决条件

- 已安装 Python 3.8+
- 已安装并运行 SQL Server 实例
- 已安装 SQL Server 对应的 ODBC 驱动程序

### 2. 克隆仓库

```bash
git clone https://github.com/your-username/student-info-system.git
cd student-info-system
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 数据库设置

1.  在您的 SQL Server 实例中创建一个新的数据库（例如 `StudentDB`）。
2.  执行项目提供的 SQL 脚本（例如 `database_setup.sql`）来创建所有需要的表和初始数据。

### 5. 配置数据库连接

为了安全地管理数据库连接信息，建议使用 Streamlit 的 `secrets.toml`。

1.  在项目根目录创建 `.streamlit` 文件夹。
2.  在其中创建 `secrets.toml` 文件，并填入您的数据库连接信息：

    ```toml
    # .streamlit/secrets.toml

    [database]
    driver = "{ODBC Driver 17 for SQL Server}"
    server = "YOUR_SERVER_NAME_OR_IP"
    database = "StudentDB"
    username = "YOUR_USERNAME"
    password = "YOUR_PASSWORD"
    ```

3.  在您的 Python 代码中，使用 `st.secrets` 来获取连接信息：
    ```python
    import streamlit as st
    import pyodbc

    db_config = st.secrets["database"]
    conn_str = (
        f"DRIVER={db_config['driver']};"
        f"SERVER={db_config['server']};"
        f"DATABASE={db_config['database']};"
        f"UID={db_config['username']};"
        f"PWD={db_config['password']};"
    )
    connection = pyodbc.connect(conn_str)
    ```

### 6. 运行应用

```bash
streamlit run app.py
```

应用将在您的浏览器中自动打开，您可以开始使用了！

## 🎨 系统设计

### 实体关系模型 (E-R Diagram)

系统核心实体包括学生、教师和课程，它们之间通过授课和选修关系连接，构成了整个系统的基础。

![ER图](./img/ER.png)

### 数据库表结构

<details>
<summary><b>点击展开查看详细表结构</b></summary>

#### 教师表 (teachers)
| 字段名 | 数据类型 | 约束 | 描述 |
|---|---|---|---|
| `TeacherID` | INT | PRIMARY KEY | 教师唯一标识 |
| `TeacherName` | NVARCHAR(100) | NOT NULL | 教师姓名 |
| `Email` | NVARCHAR(100) | | 教师邮箱 |
| `Position` | NVARCHAR(50) | | 教师职位 |

---

#### 学生表 (students)
| 字段名 | 数据类型 | 约束 | 描述 |
|---|---|---|---|
| `StudentID` | INT | PRIMARY KEY | 学生唯一标识 |
| `StudentName` | NVARCHAR(100) | NOT NULL | 学生姓名 |
| `Email` | NVARCHAR(100) | | 学生邮箱 |
| `Major` | NVARCHAR(50) | | 学生专业 |
| `Grade` | NVARCHAR(20) | | 学生年级 |

---

#### 课程表 (courses)
| 字段名 | 数据类型 | 约束 | 描述 |
|---|---|---|---|
| `CourseID` | INT | PRIMARY KEY | 课程唯一标识 |
| `CourseName` | NVARCHAR(100) | NOT NULL | 课程名称 |
| `Credits` | INT | | 课程学分 |
| `TeacherID` | INT | FOREIGN KEY | 授课教师ID |

---

#### 选课表 (course_enrollments)
| 字段名 | 数据类型 | 约束 | 描述 |
|---|---|---|---|
| `EnrollmentID` | INT | PRIMARY KEY, IDENTITY(1,1) | 选课记录唯一标识 |
| `StudentID` | INT | FOREIGN KEY | 学生ID |
| `CourseID` | INT | FOREIGN KEY | 课程ID |
| `Grade` | INT | CHECK(Grade >= 0 AND Grade <= 100) | 成绩（0-100） |

---

#### 课堂交流表 (class_interaction)
| 字段名 | 数据类型 | 约束 | 描述 |
|---|---|---|---|
| `InteractionID` | INT | PRIMARY KEY, IDENTITY(1,1) | 自动生成的记录ID |
| `CourseID` | INT | NOT NULL | 班级号 |
| `SpeakerType` | VARCHAR(50) | NOT NULL | 发言人身份 |
| `SpeakerName` | VARCHAR(100) | NOT NULL | 发言人姓名 |
| `Content` | TEXT | NOT NULL | 发言内容 |
| `Timestamp` | DATETIME | DEFAULT GETDATE() | 发言时间 |

---

#### 教务通知表 (academic_notices)
| 字段名 | 数据类型 | 约束 | 描述 |
|---|---|---|---|
| `NotificationID` | INT | PRIMARY KEY, IDENTITY(1,1) | 自动生成的通知ID |
| `Title` | VARCHAR(255) | NOT NULL | 通知标题 |
| `Content` | TEXT | NOT NULL | 通知内容 |
| `Publisher` | VARCHAR(100) | NOT NULL | 发布人 |
| `PublishDate` | DATETIME | DEFAULT GETDATE() | 发布日期 |
| `Status` | VARCHAR(50) | DEFAULT 'Active' | 通知状态（Active/Expired）|

</details>

## 💡 未来展望

- **性能优化**: 对高频查询和大数据表（如成绩表）进行索引优化和分区，提升系统响应速度。
- **功能扩展**: 增加在线作业提交、教学质量评估、课程资源共享等功能。
- **数据分析与可视化**: 集成仪表盘，为管理员提供学生成绩分布、选课热门度等数据洞察。
- **移动端适配**: 进一步优化 Streamlit 界面，提升在移动设备上的用户体验。

## 🤝 贡献

欢迎对本项目提出改进意见和贡献代码！您可以通过提交 **Issue** 或 **Pull Request** 的方式参与进来。

---
