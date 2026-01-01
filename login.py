# Import libraries
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess
import sys
from PIL import Image, ImageTk
from config import db_config

def login(event=None):
    # Get input values
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    # Validate input
    if not username or not password:
        messagebox.showerror("Error", "Enter username and password")
        return

    # Database connection
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Query user credentials
    query = """SELECT user_id, full_name, user_type, status
               FROM users WHERE username=%s AND password=%s"""
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.close()

    # Process login result
    if result:
        if result[3] == 'active':
            user_id = result[0]
            user_name = result[1]
            user_type = result[2]

            messagebox.showinfo("Success", f"Welcome, {user_name}!")
            root.destroy()

            # Launch appropriate portal
            if user_type == 'admin':
                subprocess.Popen([sys.executable, 'admin.py', str(user_id)])
            else:
                subprocess.Popen([sys.executable, 'member.py', str(user_id)])
        else:
            messagebox.showerror("Error",
                "Account is inactive. Contact administrator.")
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Main window setup
root = tk.Tk()
root.title("Library Management System")
root.geometry("800x600")
root.resizable(False, False)

# Background image
bg_image = Image.open("images/library.jpeg").resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
canvas.create_image(0, 0, image=bg_photo, anchor=tk.NW)

# Login frame
frame = tk.Frame(canvas, bg="white", relief=tk.RAISED, bd=2)
canvas.create_window(400, 300, window=frame, width=350, height=280)

# Title
tk.Label(frame, text="Library Management System",
         font=("Arial", 16, "bold"), bg="white", fg="#2196F3").pack(pady=15)

# Username
tk.Label(frame, text="Username", font=("Arial", 11, "bold"),
         bg="white", fg="#333").pack(pady=5)
username_entry = tk.Entry(frame, font=("Arial", 11), width=25)
username_entry.pack(pady=5)

# Password
tk.Label(frame, text="Password", font=("Arial", 11, "bold"),
         bg="white", fg="#333").pack(pady=5)
password_entry = tk.Entry(frame, font=("Arial", 11), width=25, show="*")
password_entry.pack(pady=5)

# Login button
tk.Button(frame, text="Login", font=("Arial", 11, "bold"),
          width=15, command=login).pack(pady=15)

# Enter key binding
password_entry.bind('<Return>', login)

# Run application
root.mainloop()
