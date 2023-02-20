"""
task create new table transactions_konakbayev with the following columns:
- id (int, primary key)
- description(varchar)
- price_kzt (int)
- quantity (int)
- amount (int)
- price_usd (int)
- date (timestamp)

Services:
1) Create a new transaction every minute
2) Read all transactions from database and multiply price by quantity
3) Read all transactions from database and multiply amount by price_usd
"""

import psycopg2

conn = psycopg2.connect(
    host="test.dsacademy.kz",
    database="fortesting",
    user="testing",
    password="testing123"
)

if __name__ == "__main__":
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions_konakbayev")
    transactions = cursor.fetchall()
    print(transactions)