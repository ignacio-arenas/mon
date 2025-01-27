import json
import sqlite3
from datetime import datetime

DB_PATH = "db/notes.db"


class Note:
    
    @staticmethod
    def search_notes(content):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Fetch notes from the database
        cursor.execute("""SELECT id, content, tags, created_at FROM notes WHERE content LIKE ?""", (f"%{content}%",))
        notes = cursor.fetchall()

        if not notes:
            print("No notes found!")
        else:
            result: list[Note] = []
            for note in notes:
                result.append(Note(note[0], note[1], note[2], note[3], note[4]))

        conn.close()
    
    @staticmethod
    def list_notes(tag=None):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Fetch notes from the database
        if tag:
            cursor.execute("""
            SELECT id, content, tags, created_at FROM notes
            WHERE tags LIKE ?
            """, (f"%{tag}%",))
        else:
            cursor.execute("""
            SELECT id, content, tags, created_at FROM notes
            """)

        notes = cursor.fetchall()

        if not notes:
            print("No notes found!")
        else:
            result: list[Note] = []
            for note in notes:
                result.append(Note(note[0], note[1], note[2], note[3], note[4]))

        conn.close()
    
    @staticmethod
    def export(file_path):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Fetch all notes from the database
        cursor.execute("SELECT * FROM notes")
        notes = cursor.fetchall()

        # Convert notes to a list of dictionaries
        notes_list = [
            {
                "id": note[0],
                "content": note[1],
                "tags": note[2],
                "created_at": note[3],
                "updated_at": note[4]
            } for note in notes
        ]

        # Write to JSON file
        with open(file_path, "w") as f:
            json.dump(notes_list, f, indent=4)

        print(f"Notes exported to {file_path}")
        conn.close()
    
    def __init__(self, id, content, tags = []):
        self.id = id
        self.content = content
        self.tags = tags
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Insert the new note into the database
        cursor.execute("""
        INSERT INTO notes (content, tags, created_at, updated_at)
        VALUES (?, ?, ?, ?)
        """, (content, tags, datetime.now(), datetime.now()))

        conn.commit()
        conn.close()

    def __str__(self):
        return f"Note: {self.id}, {self.title}, {self.content}, {self.tags}, {self.created_at}, {self.updated_at}"
    