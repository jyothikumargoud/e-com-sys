import sqlite3
import pandas as pd

DB_NAME = "ecommerce.db"

def create_database():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CCREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price REAL,
    description TEXT,
    reviews INTEGER,
    rating INTEGER,
    category TEXT
)
    """)

    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect(DB_NAME)

    df = pd.read_csv("data/cleaned_products.csv")

    df.to_sql("products", conn, if_exists="replace", index=False)

    conn.close()

if __name__ == "__main__":
    create_database()
    insert_data()