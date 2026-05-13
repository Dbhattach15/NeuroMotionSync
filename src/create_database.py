import sqlite3

conn = sqlite3.connect("../data/motion_data.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS motion_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    laptop_timestamp REAL,
    source TEXT,
    trial INTEGER,
    condition TEXT,
    sensor TEXT,
    x REAL,
    y REAL,
    z REAL
)
""")

conn.commit()
conn.close()

print("Database created.")

