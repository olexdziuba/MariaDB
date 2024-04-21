import mysql.connector

# Запит інформації для підключення
host = input('Введіть хост: ')
user = input("Введіть ім'я користувача: ")
password = input('Введіть пароль: ')

# Спроба підключення до MariaDB
try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    print("Підключення до бази даних успішне")
except mysql.connector.Error as err:
    print(f"Помилка підключення: {err}")
    exit(1)

# Створення бази даних
def create_database():
    cursor = conn.cursor()
    create_database_query = "CREATE DATABASE IF NOT EXISTS ABC;"
    cursor.execute(create_database_query)
    print("База даних ABC створена")

# Створення таблиць
def create_table(create_table_query, table_name):
    cursor = conn.cursor()
    cursor.execute(create_table_query)
    print(f"Таблиця {table_name} створена")

create_database()  # Виклик функції для створення бази даних

# Закриття підключення та повторне підключення до створеної бази даних
conn.close()
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database='ABC'  
)

# Створення таблиць
create_table_query_employes = """
CREATE TABLE IF NOT EXISTS employes (
    emp_no INT(11) NOT NULL AUTO_INCREMENT,
    dateNaissance DATE NOT NULL,
    prenom VARCHAR(14) NOT NULL,
    nom VARCHAR(16) NOT NULL,
    sexe ENUM('M', 'F') NOT NULL,
    dateEmbauche DATE NOT NULL,
    PRIMARY KEY (emp_no)
) ENGINE=InnoDB;
"""
create_table(create_table_query_employes, "employes")

create_table_query_departments = """
CREATE TABLE IF NOT EXISTS departments (
    dept_no CHAR(4) NOT NULL,
    deptNom VARCHAR(40) NOT NULL,
    PRIMARY KEY (dept_no),
    UNIQUE KEY deptNom (deptNom)
) ENGINE=InnoDB;
"""
create_table(create_table_query_departments, "departments")

create_table_query_salaries = """
CREATE TABLE IF NOT EXISTS salaries (
    emp_no INT(11) NOT NULL,
    salaire INT(11) NOT NULL,
    de_la_date DATE NOT NULL,
    a_la_date DATE NOT NULL,
    PRIMARY KEY (emp_no, de_la_date),
    KEY emp_no (emp_no),
    CONSTRAINT salaries_ibfk_1 FOREIGN KEY (emp_no) 
        REFERENCES employes (emp_no) ON DELETE CASCADE
) ENGINE=InnoDB;
"""
create_table(create_table_query_salaries, "salaries")

create_table_query_dept_emp = """
CREATE TABLE IF NOT EXISTS dept_emp (
    emp_no INT(11) NOT NULL,
    dept_no CHAR(4) NOT NULL,
    de_la_date DATE NOT NULL,
    a_la_date DATE NOT NULL,
    PRIMARY KEY (emp_no, dept_no),
    KEY emp_no (emp_no),
    KEY dept_no (dept_no),
    CONSTRAINT dept_emp_ibfk_1 FOREIGN KEY (emp_no) 
        REFERENCES employes (emp_no) ON DELETE CASCADE,
    CONSTRAINT dept_emp_ibfk_2 FOREIGN KEY (dept_no) 
        REFERENCES departments (dept_no) ON DELETE CASCADE
) ENGINE=InnoDB;
"""
create_table(create_table_query_dept_emp, "dept_emp")

create_table_query_dept_manager = """
CREATE TABLE IF NOT EXISTS dept_manager (
    emp_no INT(11) NOT NULL,
    dept_no CHAR(4) NOT NULL,
    de_la_date DATE NOT NULL,
    a_la_date DATE NOT NULL,
    PRIMARY KEY (emp_no, dept_no),
    KEY emp_no (emp_no),
    KEY dept_no (dept_no),
    CONSTRAINT dept_manager_ibfk_1 FOREIGN KEY (emp_no) 
        REFERENCES employes (emp_no) ON DELETE CASCADE,
    CONSTRAINT dept_manager_ibfk_2 FOREIGN KEY (dept_no) 
        REFERENCES departments (dept_no) ON DELETE CASCADE
) ENGINE=InnoDB;
"""
create_table(create_table_query_dept_manager, "dept_manager")

create_table_query_titres = """
CREATE TABLE IF NOT EXISTS titres (
    emp_no INT(11) NOT NULL,
    titre VARCHAR(50) NOT NULL,
    de_la_date DATE NOT NULL,
    a_la_date DATE DEFAULT NULL,
    PRIMARY KEY (emp_no, titre, de_la_date),
    KEY emp_no (emp_no),
    CONSTRAINT titres_ibfk_1 FOREIGN KEY (emp_no) 
        REFERENCES employes (emp_no) ON DELETE CASCADE
) ENGINE=InnoDB;
"""
create_table(create_table_query_titres, "titres")

# Закриття підключення
conn.close()
