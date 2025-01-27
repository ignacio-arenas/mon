import os
import sqlite3

DB_PATH = "db/notes.db"

def initialize_database():
    # Ensure the database directory exists
    os.makedirs("db", exist_ok=True)

    # Create the database file and table if not already present
    if not os.path.exists(DB_PATH):
        print("Initializing database...")
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create the notes table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            tags TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        conn.close()
        print(f"Database initialized at {DB_PATH}")
    else:
        print("Database already exists.")
