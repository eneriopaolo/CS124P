from prompt_toolkit import prompt
import json
import os

# Define the JSON file path
file_path = 'notes.json'
term_size = os.get_terminal_size()

# Load existing data from the JSON file, if it exists
def load_notes():
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return {}

# Save the note data to JSON file
def save_notes(data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Checks whether title already exists for user
def title_exists(username, title):
    data = load_notes()
    return any(note["title"] == title for note in data.get(username, []))

# Adds new note for user
def add_note(username, title, text):
    data = load_notes()
    if username not in data:
        data[username] = []
    # Append note as a dictionary with title and text
    data[username].append({"title": title, "text": text})
    save_notes(data)
    return True

# Updates note with new text for user 
def update_note(username, title):
    data = load_notes()
    for note in data.get(username, []):
        if note["title"] == title:
            # Allow editing the title and text dynamically
            while True:
                new_title = prompt("Edit title: ", default=note["title"])
                if new_title != note["title"] and title_exists(username, new_title):
                    print(f"A note with the title '{new_title}' already exists. Please choose a different title.")
                    print('-' * term_size.columns)
                    continue
                break
            new_text = prompt("Edit note text: ", default=note["text"])
            note["title"] = new_title
            note["text"] = new_text
            save_notes(data)
            return True
    return False

# Deletes unwanted note for user
def delete_note(username, title):
    data = load_notes()
    if username in data:
        notes = data[username]
        # Remove the note with the matching title
        data[username] = [note for note in notes if note["title"] != title]
        save_notes(data)
        return True
    return False

# View note titles for a specific user
def view_note_titles(username):
    data = load_notes()
    if username in data:
        return [note["title"] for note in data[username]]
    return []

# Get a specific note's content by title
def view_note_content(username, title):
    data = load_notes()
    for note in data.get(username, []):
        if note["title"] == title:
            return note["text"]
    return None

# Main function to interact with the user
def noteApp(username):
    while True:
        print('=' * term_size.columns)
        action = input(f"Menu: \n[1] Add Note \n[2] View Notes \n[3] Update Note \n[4] Delete Notes \n[5] Quit\n{('-' * term_size.columns)}\nChoose an action: ")
        print('=' * term_size.columns)

        # Add Note
        if action == "1":
            while True:
                title = input("Enter the note title: ")
                if title_exists(username, title):
                    print(f"A note with the title '{title}' already exists. Please choose a different title.")
                    print('-' * term_size.columns)
                    continue
                break
            print('-' * term_size.columns)
            text = input("Enter the note text: ")
            print('-' * term_size.columns)
            add_note(username, title, text)
            print("Note added successfully!")

        # View Note
        elif action == "2":
            titles = view_note_titles(username)
            if titles:
                print("Available titles:")
                for i, title in enumerate(titles, start=1):
                    print(f"{i}. {title}")
                print('-' * term_size.columns)
                choice = input("Enter the title number to view the note: ")
                print('=' * term_size.columns)
                if choice.isdigit() and 1 <= int(choice) <= len(titles):
                    selected_title = titles[int(choice) - 1]
                    content = view_note_content(username, selected_title)
                    print(f"Title: {selected_title}\nNote: {content}")
                else:
                    print("Invalid selection.")
            else:
                print("No notes found for this user.")

        # Update Note
        elif action == "3":
            titles = view_note_titles(username)
            if titles:
                print("Available titles:")
                for i, title in enumerate(titles, start=1):
                    print(f"{i}. {title}")
                print('-' * term_size.columns)
                choice = input("Enter the title number to edit the note: ")
                print('=' * term_size.columns)

                if choice.isdigit() and 1 <= int(choice) <= len(titles):
                    selected_title = titles[int(choice) - 1]
                    if update_note(username, selected_title):
                        print("Note updated successfully!")
                    else:
                        print("Error updating note.")
                else:
                    print("Invalid selection.")
            else:
                print("No notes found for this user.")

        elif action == "4":
            titles = view_note_titles(username)
            if titles:
                print("Available titles:")
                for i, title in enumerate(titles, start=1):
                    print(f"{i}. {title}")
                print('-' * term_size.columns)
                choice = input("Enter the title number to delete the note: ")
                print('=' * term_size.columns)
                if choice.isdigit() and 1 <= int(choice) <= len(titles):
                    selected_title = titles[int(choice) - 1]
                    if delete_note(username, selected_title):
                        print("Note deleted successfully!")
                    else:
                        print("Error deleting note.")
                else:
                    print("Invalid selection.")
            else:
                print("No notes found for this user.")

        elif action == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please try again.")