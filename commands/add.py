import json
import os

NOTES_FILE = "notes/notes.json"

def add(content, tags=""):
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            json.dump([], f)
    
    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)
    
    note_id = len(notes) + 1
    note = {"id": note_id, "content": content, "tags": tags.split(",")}
    notes.append(note)
    
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)
    
    print(f"Note added with ID {note_id}")