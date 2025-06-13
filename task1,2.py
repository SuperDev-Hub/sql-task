import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Satya",
    database="alephys"
)
cursor = conn.cursor()

'''
employees_data= [
(1, 'Manikanta', 'HR', 'Manager', 2056, '2020-06-01', 75000, None),
(2, 'Suresh', 'HR', 'Recruiter', 2057, '2021-07-03', 50000, 3000),
(3, 'Siddhu', 'IT', 'Developer', 2058, '2019-03-14', 80000, None),
(4, 'Danny', 'Analyst', 'Developer', 2059, '2019-06-18', 70000, 6000),
(5, 'Anushka', 'IT', 'Analyst', 2060, '2025-12-23', 90000, None),
(6, 'Ravi', 'Finance', 'Accountant', 2061, '2022-01-15', 60000, None),
(7, 'Priya', 'Finance', 'Manager', 2062, '2020-05-20', 95000, None),
(8, 'Kiran', 'IT', 'Developer', 2063, '2018-11-30', 85000, None),
(9, 'Sita', 'HR', 'Recruiter', 2064, '2021-08-10', 52000, 2500),
(10, 'Rahul', 'Finance', 'Analyst', 2065, '2023-02-25', 70000, None),
(11, 'Nisha', 'IT', 'Developer', 2066, '2024-03-05', 80000, 0),
(12, 'Arjun', 'HR', 'Manager', 2067, '2019-09-12', 78000, 0),
(13, 'Lakshmi', 'Finance', 'Accountant', 2068, '2022-04-18', 62000, None),
(14, 'Vikram', 'IT', 'Analyst', 2069, '2020-10-22', 72000, None),
(15, 'Geeta', 'HR', 'Recruiter', 2070, '2021-11-30', 54000, 2800),
(16, 'Ajay', 'Finance', 'Manager', 2071, '2023-01-10', 98000, None),
(17, 'Riya', 'IT', 'Developer', 2072, '2018-07-15', 83000, None),
(18, 'Suresh Kumar', 'HR', 'Recruiter', 2073, '2020-02-28', 51000, 3200),
(19, 'Anil', 'Finance', 'Analyst', 2074, '2021-05-05', 68000, None),
(20, 'Deepa', 'IT', 'Developer', 2075, '2022-08-20', 90000, None)
]


cursor.executemany("""
INSERT INTO employees (emp_id, emp_name, department, job_name, manager_id, hire_date, salary, commission)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""", employees_data)
conn.commit()
'''

print("\n Second highest salary:")
cursor.execute("""
SELECT MAX(salary) FROM employees 
WHERE salary < (SELECT MAX(salary) FROM employees)
""")
print(cursor.fetchone()[0])


cursor.execute("""
SELECT emp_name, department, salary
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department = e.department
)
ORDER BY department, salary DESC
""")

results = cursor.fetchall()
print("\nEmployees earning more than the average salary in their department:")
for name, dept, salary in results:
    print(f"{name} ({dept}) - ₹{salary}")

cursor.close()
conn.close()
