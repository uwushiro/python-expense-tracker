import sqlite3

conn = sqlite3.connect("gastos.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS gastos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    monto REAL,
    categoria TEXT
)
""")

conn.commit()