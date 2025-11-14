# Add Book Form - Library Management System
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from config import db_config  # Import database settings from config.py

# Save new book to database
def save():
    # Get all field values
    title = title_entry.get().strip()
    author = author_entry.get().strip()
    isbn = isbn_entry.get().strip()
    year = year_entry.get().strip()
    copies = copies_entry.get().strip()

    # Check if all fields are filled
    if not all([title, author, isbn, year, copies]):
        messagebox.showerror("Error", "All fields are required!")
        return

    # Validate year and copies are numbers
    try:
        year = int(year)
        copies = int(copies)
        if copies < 1:
            messagebox.showerror("Error", "Number of copies must be at least 1")
            return
    except ValueError:
        messagebox.showerror("Error", "Year and copies must be valid numbers")
        return

    try:
        # Connect to database
        conn = mysql.connector.connect(**db_config)
        cur = conn.cursor()

        # Insert each copy of the book
        for i in range(1, copies + 1):
            cur.execute("INSERT INTO books (title, author, isbn, year, copy_number, book_status, record_status) VALUES (%s, %s, %s, %s, %s, 'New', 'Active')",
                       (title, author, isbn, year, i))
            book_id = cur.lastrowid

            # Log transaction
            cur.execute("INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes) VALUES (%s, NULL, NULL, 'Add', %s)",
                       (book_id, f"{title} by {author} (Copy {i})"))

        # Save to database
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"{copies} cop{'y' if copies == 1 else 'ies'} of '{title}' added successfully!")
        reset()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add book:\n{e}")

# Clear all entry fields
def reset():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    isbn_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    copies_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Add Book")
root.geometry("800x600")
root.resizable(False, False)

# Create form in center
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Form fields
tk.Label(frame, text="Book Title:").grid(row=0, column=0, padx=5, pady=5)
title_entry = tk.Entry(frame)
title_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Author:").grid(row=1, column=0, padx=5, pady=5)
author_entry = tk.Entry(frame)
author_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="ISBN Number:").grid(row=2, column=0, padx=5, pady=5)
isbn_entry = tk.Entry(frame)
isbn_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Publication Year:").grid(row=3, column=0, padx=5, pady=5)
year_entry = tk.Entry(frame)
year_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame, text="Number of Copies:").grid(row=4, column=0, padx=5, pady=5)
copies_entry = tk.Entry(frame)
copies_entry.grid(row=4, column=1, padx=5, pady=5)

# Buttons
tk.Button(frame, text="Save", command=save).grid(row=5, column=0, pady=10)
tk.Button(frame, text="Reset", command=reset).grid(row=5, column=1, pady=10)

root.mainloop()
