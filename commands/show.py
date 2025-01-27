import json

NOTES_FILE = "notes/notes.json"

def list_all(tag=None):
    try:
        with open(NOTES_FILE, "r") as f:
            notes = json.load(f)
        
        for note in notes:
            if tag and tag not in note["tags"]:
                continue
            print(f"ID: {note['id']} | Tags: {', '.join(note['tags'])}")
            print(f"  {note['content']}")
            print("-" * 40)
    except FileNotFoundError:
        print("No notes found. Add a note first!")