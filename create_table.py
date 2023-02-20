import time
from transaction import Transaction

import psycopg2

conn = psycopg2.connect(
    host="test.dsacademy.kz",
    database="fortesting",
    user="testing",
    password="testing123"
)

def create_table():

    query = """
    CREATE TABLE IF NOT EXISTS transactions_konakbayev(
        id SERIAL PRIMARY KEY,
        description VARCHAR(255) NOT NULL,
        price_kzt INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        amount INTEGER,
        price_usd INTEGER,
        date DATE DEFAULT NOW()
        """

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def insert_transaction(transaction: Transaction):
    query = """
    INSERT INTO transactions_konakbayev(description, price_kzt, quantity, amount)
    VALUES(%s,%s,%s,%s)
    """
    cursor = conn.cursor()
    cursor.execute(query, (transaction.description, transaction.price_kzt, transaction.quantity, transaction.amount))
    conn.commit()


def update_transaction():
    query = "UPDATE transactions_konakbayev SET amount=price_kz * quantity WHERE amount = 0 "
    cursor = conn.cursor
    cursor.execute(query)
    conn.commit()

def update_price_usd():
    query = "UPDATE transactions_konakbayev SET price_usd = amount * 460 WHERE price_usd = 0 "
    cursor = conn.cursor
    cursor.execute()
    conn.commit()