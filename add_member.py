# Add Member Screen - Library Management System
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from config import db_config  # Import database settings from config.py

# Save new member to database
def save():
    # Get all field values
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    name = name_entry.get().strip()
    address = address_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()

    # Check required fields
    if not username or not password or not name:
        messagebox.showerror("Error", "Username, Password and Name are required")
        return

    try:
        # Connect to database
        conn = mysql.connector.connect(**db_config)
        cur = conn.cursor()

        # Check if username already exists
        cur.execute("SELECT username FROM users WHERE username = %s", (username,))
        if cur.fetchone():
            messagebox.showerror("Error", f"Username '{username}' already exists!\nPlease choose a different username.")
            conn.close()
            return

        # Insert into users table
        cur.execute("INSERT INTO users (username, password, full_name, user_type, status) VALUES (%s, %s, %s, 'member', 'active')",
                   (username, password, name))
        user_id = cur.lastrowid

        # Insert into members table
        cur.execute("INSERT INTO members (user_id, name, address, email, phone) VALUES (%s, %s, %s, %s, %s)",
                   (user_id, name, address, email, phone))
        member_id = cur.lastrowid

        # Save to database
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"Member added successfully!\nMember ID: {member_id}")
        reset()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add member:\n{e}")

# Clear all entry fields
def reset():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Add Member")
root.geometry("800x600")
root.resizable(False, False)

# Create form in center
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Form fields
tk.Label(frame, text="Username: *").grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Password: *").grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Full Name: *").grid(row=2, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Address:").grid(row=3, column=0, padx=5, pady=5)
address_entry = tk.Entry(frame)
address_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame, text="Email:").grid(row=4, column=0, padx=5, pady=5)
email_entry = tk.Entry(frame)
email_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(frame, text="Phone:").grid(row=5, column=0, padx=5, pady=5)
phone_entry = tk.Entry(frame)
phone_entry.grid(row=5, column=1, padx=5, pady=5)

# Buttons
tk.Button(frame, text="Save", command=save).grid(row=6, column=0, pady=10)
tk.Button(frame, text="Reset", command=reset).grid(row=6, column=1, pady=10)

root.mainloop()
