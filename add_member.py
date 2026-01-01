# Add User - Library Management System

import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from config import db_config

def save():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    name = name_entry.get().strip()
    user_type = user_type_var.get()
    address = address_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()

    if not username or not password or not name:
        messagebox.showerror("Error",
            "Username, Password and Full Name are required fields")
        return

    try:
        conn = mysql.connector.connect(**db_config)
        cur = conn.cursor()

        cur.execute("SELECT username FROM users WHERE username = %s",
                  (username,))
        if cur.fetchone():
            messagebox.showerror("Error",
                f"Username '{username}' already exists!\n"
                f"Please choose a different username.")
            conn.close()
            return

        query = """INSERT INTO users
                   (username, password, full_name, user_type, status)
                   VALUES (%s, %s, %s, %s, 'active')"""
        cur.execute(query, (username, password, name, user_type.lower()))
        user_id = cur.lastrowid

        if user_type.lower() == 'member':
            query = """INSERT INTO members
                       (user_id, name, address, email, phone)
                       VALUES (%s, %s, %s, %s, %s)"""
            cur.execute(query, (user_id, name, address, email, phone))
            member_id = cur.lastrowid
            success_msg = f"Member added successfully!\nMember ID: {member_id}"
        else:
            success_msg = f"Admin user '{username}' added successfully!"

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", success_msg)
        reset()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add user:\n{e}")

def reset():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    user_type_var.set("Member")
    address_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Add User")
root.geometry("800x600")
root.resizable(False, False)

# Form
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="Username: *", anchor="e",
        width=15).grid(row=0, column=0, padx=5, pady=5, sticky="e")
username_entry = tk.Entry(frame, width=25)
username_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Password: *", anchor="e",
        width=15).grid(row=1, column=0, padx=5, pady=5, sticky="e")
password_entry = tk.Entry(frame, show="*", width=25)
password_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Full Name: *", anchor="e",
        width=15).grid(row=2, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(frame, width=25)
name_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="User Type:", anchor="e",
        width=15).grid(row=3, column=0, padx=5, pady=5, sticky="e")
user_type_var = tk.StringVar(value="Member")
user_type_dropdown = ttk.Combobox(frame, textvariable=user_type_var,
    values=["Member", "Admin"], state="readonly", width=22)
user_type_dropdown.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame, text="Address:", anchor="e",
        width=15).grid(row=4, column=0, padx=5, pady=5, sticky="e")
address_entry = tk.Entry(frame, width=25)
address_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(frame, text="Email:", anchor="e",
        width=15).grid(row=5, column=0, padx=5, pady=5, sticky="e")
email_entry = tk.Entry(frame, width=25)
email_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(frame, text="Phone:", anchor="e",
        width=15).grid(row=6, column=0, padx=5, pady=5, sticky="e")
phone_entry = tk.Entry(frame, width=25)
phone_entry.grid(row=6, column=1, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(frame)
button_frame.grid(row=7, column=0, columnspan=2, pady=10)
tk.Button(button_frame, text="Save", command=save,
         width=12).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Reset", command=reset,
         width=12).pack(side=tk.LEFT, padx=5)

root.mainloop()
