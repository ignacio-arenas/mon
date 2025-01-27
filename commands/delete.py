import json

NOTES_FILE = "notes/notes.json"

def delete(note_id):
    try:
        with open(NOTES_FILE, "r") as f:
            notes = json.load(f)
        
        notes = [note for note in notes if note["id"] != note_id]
        
        with open(NOTES_FILE, "w") as f:
            json.dump(notes, f, indent=4)
        
        print(f"Note with ID {note_id} deleted.")
    except FileNotFoundError:
        print("No notes found.")