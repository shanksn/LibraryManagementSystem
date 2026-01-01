# Add Book - Library Management System

import tkinter as tk
from tkinter import messagebox
import mysql.connector
import sys
from config import db_config

admin_user_id = int(sys.argv[1]) if len(sys.argv) > 1 else None

def save():
    title = title_entry.get().strip()
    author = author_entry.get().strip()
    isbn = isbn_entry.get().strip()
    year = year_entry.get().strip()
    copies = copies_entry.get().strip()

    if not all([title, author, isbn, year, copies]):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        year = int(year)
        copies = int(copies)
        if copies < 1:
            messagebox.showerror("Error",
                "Number of copies must be at least 1")
            return
        if copies > 5:
            messagebox.showerror("Error",
                "Number of copies cannot be more than 5")
            return
    except ValueError:
        messagebox.showerror("Error",
            "Year and copies must be valid numbers")
        return

    try:
        conn = mysql.connector.connect(**db_config)
        cur = conn.cursor()

        cur.execute("""SELECT title, author FROM books
                     WHERE title = %s AND author = %s LIMIT 1""",
                  (title, author))
        existing_book = cur.fetchone()
        if existing_book:
            messagebox.showerror("Error",
                f"Book '{title}' by {author} already exists!\n"
                f"Use a different title or check existing copies.")
            conn.close()
            return

        for i in range(1, copies + 1):
            query = """INSERT INTO books
                       (title, author, isbn, year, copy_number,
                        book_status, record_status)
                       VALUES (%s, %s, %s, %s, %s, 'New', 'Active')"""
            cur.execute(query, (title, author, isbn, year, i))
            book_id = cur.lastrowid

            query = """INSERT INTO transactions
                       (book_id, member_id, admin_user_id, action, notes)
                       VALUES (%s, NULL, %s, 'Add', %s)"""
            cur.execute(query, (book_id, admin_user_id,
                              f"{title} by {author} (Copy {i})"))

        conn.commit()
        conn.close()

        copy_text = "y" if copies == 1 else "ies"
        messagebox.showinfo("Success",
            f"{copies} cop{copy_text} of '{title}' added successfully!")
        reset()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add book:\n{e}")

def reset():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    isbn_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    copies_entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Add Book")
root.geometry("800x600")
root.resizable(False, False)

# Form
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="Book Title: *", anchor="e",
        width=20).grid(row=0, column=0, padx=5, pady=5, sticky="e")
title_entry = tk.Entry(frame, width=30)
title_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Author: *", anchor="e",
        width=20).grid(row=1, column=0, padx=5, pady=5, sticky="e")
author_entry = tk.Entry(frame, width=30)
author_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="ISBN Number: *", anchor="e",
        width=20).grid(row=2, column=0, padx=5, pady=5, sticky="e")
isbn_entry = tk.Entry(frame, width=30)
isbn_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Publication Year: *", anchor="e",
        width=20).grid(row=3, column=0, padx=5, pady=5, sticky="e")
year_entry = tk.Entry(frame, width=30)
year_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame, text="Number of Copies: *", anchor="e",
        width=20).grid(row=4, column=0, padx=5, pady=5, sticky="e")
copies_entry = tk.Entry(frame, width=30)
copies_entry.grid(row=4, column=1, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(frame)
button_frame.grid(row=5, column=0, columnspan=2, pady=10)
tk.Button(button_frame, text="Save", command=save,
         width=12).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Reset", command=reset,
         width=12).pack(side=tk.LEFT, padx=5)

root.mainloop()
