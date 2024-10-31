import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import notepad_modifed

# Create the main window
login_root = tk.Tk()
login_root.title("Login / Sign Up")
login_root.geometry("400x300")

if not os.path.exists("users.json"):
    with open("users.json", "w") as f:
        json.dump({}, f)

# Function to handle signup
def signup():
    username = username_entry.get()
    password = password_entry.get()
    
    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter both username and password.")
        return
    
    # Check if user already exists
    if os.path.exists(f"{username}_notes.json"):
        messagebox.showwarning("Signup Error", "User already exists.")
        return
    
    # Save user credentials and create empty notes file
    with open("users.json", "r") as f:
        users = json.load(f)
        
    users[username] = password
    with open("users.json", "w") as f:
        json.dump(users, f)

    with open(f"{username}_notes.json", "w") as f:
        json.dump({}, f)
    
    messagebox.showinfo("Signup Successful", "Account created! Please log in.")
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Load user credentials
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}
    
    # Check if username and password match
    if username in users and users[username] == password:
        login_root.destroy()  # Close login window
        open_notes_app(username)  # Open notes app with the user's data
    else:
        messagebox.showerror("Login Error", "Invalid username or password.")

# Open Notes App
def open_notes_app(username):
    notepad_modifed.run_notes_app(username)

# UI elements for login/signup
username_label = ttk.Label(login_root, text="Username:")
username_label.pack(pady=5)
username_entry = ttk.Entry(login_root)
username_entry.pack(pady=5)

password_label = ttk.Label(login_root, text="Password:")
password_label.pack(pady=5)
password_entry = ttk.Entry(login_root, show="*")
password_entry.pack(pady=5)

login_button = ttk.Button(login_root, text="Login", command=login)
login_button.pack(pady=10)

signup_button = ttk.Button(login_root, text="Sign Up", command=signup)
signup_button.pack(pady=10)

login_root.mainloop()

