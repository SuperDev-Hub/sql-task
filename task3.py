import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Satya",
    database="alephys"
)
cursor = conn.cursor()


sales_data = [
    (1, "2023-01-01", 1000.86),
    (2, "2023-01-02", 23470),
    (3, "2023-01-02", 23450),
    (4, "2023-11-04", 500.85),
    (5, "2023-02-11", 25),
    (6, "2023-01-24", 3000),
    (7, "2023-07-07", 1200),
    (8, "2023-11-25", 1800),
    (9, "2023-01-09", 22070),
    (10, "2023-01-10", 800),
    (11, "2023-01-11", 2700),
    (12, "2023-01-06", 3200),
    (13, "2023-01-13", 11.12),
    (14, "2023-01-11", 16554),
    (15, "2023-01-15", 2100.56),
    (16, "2023-07-11", 19000),
    (17, "2023-01-17", 1300),
    (18, "2023-02-18", 1400.89),
    (19, "2023-07-27", 1700),
    (20, "2023-11-20", 1900),
    (21, "2023-01-21", 2300),
    (22, "2023-01-16", 52000),
    (23, "2023-02-23", 150),
    (24, "2023-01-17", 78),
    (25, "2023-01-25", 36700.56),
    (26, "2023-01-05", 3100),
    (27, "2023-01-27", 3300.45),
    (28, "2023-02-05", 300),
    (29, "2023-01-29", 45000),
    (30, "2023-01-02", 3890)
]

# Insert data using executemany
cursor.executemany("INSERT IGNORE INTO sales VALUES (%s, %s, %s)", sales_data)
conn.commit()


print("\n Running total of sales amount by date:")
cursor.execute("""
SELECT 
    s1.date,
    s1.amount,
    (
        SELECT SUM(s2.amount)
        FROM sales s2
        WHERE s2.date <= s1.date
    ) AS running_total
FROM sales s1
ORDER BY s1.date
""")

for date, amount, running_total in cursor.fetchall():
    print(f"{date} - ₹{float(amount):,.2f} - Running Total: ₹{float(running_total):,.2f}")


cursor.close()
conn.close()
