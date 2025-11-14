# Import required libraries
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess
import sys
from PIL import Image, ImageTk

# Database connection settings
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'invasion',
    'database': 'library_management_system'
}

# Login function
def login():
    # Get username and password from entry fields
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    # Check if fields are empty
    if not username or not password:
        messagebox.showerror("Error", "Enter username and password")
        return

    # Connect to database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Check if user exists in database
    cursor.execute("SELECT user_id, full_name, user_type, status FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    conn.close()

    # If user found and account is active
    if result and result[3] == 'active':
        user_id = result[0]
        user_name = result[1]
        user_type = result[2]

        messagebox.showinfo("Success", f"Welcome, {user_name}!")
        root.destroy()

        # Open admin or member screen based on user type
        if user_type == 'admin':
            subprocess.Popen([sys.executable, 'admin.py', str(user_id)])
        else:
            subprocess.Popen([sys.executable, 'member.py', str(user_id)])
    else:
        messagebox.showerror("Error", "Invalid credentials")

# Create main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("800x600")
root.resizable(False, False)

# Load and display background image
bg_image = Image.open("library.jpeg").resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
canvas.create_image(0, 0, image=bg_photo, anchor=tk.NW)

# Create white login box in center
frame = tk.Frame(canvas, bg="white")
canvas.create_window(400, 300, window=frame, width=350, height=250)

# Add title
tk.Label(frame, text="Library Management System", font=("Arial", 16, "bold"), bg="white").pack(pady=15)

# Username field
tk.Label(frame, text="Username", font=("Arial", 10), bg="white").pack(pady=5)
username_entry = tk.Entry(frame, font=("Arial", 11), width=25)
username_entry.pack(pady=5)

# Password field
tk.Label(frame, text="Password", font=("Arial", 10), bg="white").pack(pady=5)
password_entry = tk.Entry(frame, font=("Arial", 11), width=25, show="*")
password_entry.pack(pady=5)

# Login button
tk.Button(frame, text="Login", font=("Arial", 11, "bold"), width=15, command=login).pack(pady=15)

# Allow Enter key to login
password_entry.bind('<Return>', lambda e: login())

# Start the application
root.mainloop()
