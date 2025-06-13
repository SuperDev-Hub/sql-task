import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Satya",
    database="alephys"
)

cursor = conn.cursor()
transactions_data = [
    ("Marketing", "Ad Spend", "2023-01-01", 1200.75),
    ("Marketing", "Ad Spend", "2023-01-03", 845.40),
    ("Sales", "Client Lunch", "2023-01-03", 457.20),
    ("Marketing", "Ad Spend", "2023-01-04", 709.95),
    ("Sales", "Client Lunch", "2023-01-05", 325.80),
    ("IT", "Software Purchase", "2023-01-06", 1499.99),
    ("HR", "Training", "2023-01-06", 980.50),
    ("IT", "Hardware Upgrade", "2023-01-07", 2000.00),
    ("Finance", "Audit Fees", "2023-01-07", 612.35),
    ("HR", "Training", "2023-01-08", 765.25)
]
cursor.executemany("""
    INSERT INTO transactions (col1, col2, transaction_date, amount)
    VALUES (%s, %s, %s, %s)
""", transactions_data)



print("\nDuplicate combinations in transactions (col1, col2):")
cursor.execute("""
SELECT col1, col2, COUNT(*) as count
FROM transactions
GROUP BY col1, col2
HAVING count > 1
""")
for row in cursor.fetchall():
    print(row)