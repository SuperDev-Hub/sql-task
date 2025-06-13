import mysql.connector

# Step 1: Connect database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Satya"
)

cursor = conn.cursor()

# Step 2: Create and use the database
cursor.execute("CREATE DATABASE alephys")
cursor.execute("USE alephys")

# Step 3: Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    department VARCHAR(50),
    job_name VARCHAR(50),
    manager_id INT,
    hire_date DATE,
    salary DECIMAL(10,2),
    commission DECIMAL(10,2)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT PRIMARY KEY,
    date DATE NOT NULL,
    amount DECIMAL(12,2) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    col1 VARCHAR(50) NOT NULL,
    col2 VARCHAR(50) NOT NULL,
    transaction_date DATE,
    amount DECIMAL(12,2)
)
""")

