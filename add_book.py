# Add Book Form - Library Management System
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import sys
from config import db_config  # Import database settings from config.py

# Get admin_user_id from command line argument
admin_user_id = int(sys.argv[1]) if len(sys.argv) > 1 else None

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
        if copies > 5:
            messagebox.showerror("Error", "Number of copies cannot be more than 5")
            return
    except ValueError:
        messagebox.showerror("Error", "Year and copies must be valid numbers")
        return

    try:
        # Connect to database
        conn = mysql.connector.connect(**db_config)
        cur = conn.cursor()

        # Check if book with same title and author already exists
        cur.execute("SELECT title, author FROM books WHERE title = %s AND author = %s LIMIT 1", (title, author))
        existing_book = cur.fetchone()
        if existing_book:
            messagebox.showerror("Error", f"Book '{title}' by {author} already exists in the library!\nUse a different title or check existing copies.")
            conn.close()
            return

        # Insert each copy of the book
        for i in range(1, copies + 1):
            cur.execute("INSERT INTO books (title, author, isbn, year, copy_number, book_status, record_status) VALUES (%s, %s, %s, %s, %s, 'New', 'Active')",
                       (title, author, isbn, year, i))
            book_id = cur.lastrowid

            # Log transaction
            cur.execute("INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes) VALUES (%s, NULL, %s, 'Add', %s)",
                       (book_id, admin_user_id, f"{title} by {author} (Copy {i})"))

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

# Form fields with right-aligned labels
tk.Label(frame, text="Book Title: *", anchor="e", width=20).grid(row=0, column=0, padx=5, pady=5, sticky="e")
title_entry = tk.Entry(frame, width=30)
title_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Author: *", anchor="e", width=20).grid(row=1, column=0, padx=5, pady=5, sticky="e")
author_entry = tk.Entry(frame, width=30)
author_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="ISBN Number: *", anchor="e", width=20).grid(row=2, column=0, padx=5, pady=5, sticky="e")
isbn_entry = tk.Entry(frame, width=30)
isbn_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Publication Year: *", anchor="e", width=20).grid(row=3, column=0, padx=5, pady=5, sticky="e")
year_entry = tk.Entry(frame, width=30)
year_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame, text="Number of Copies: *", anchor="e", width=20).grid(row=4, column=0, padx=5, pady=5, sticky="e")
copies_entry = tk.Entry(frame, width=30)
copies_entry.grid(row=4, column=1, padx=5, pady=5)

# Buttons - center aligned relative to form fields
button_frame = tk.Frame(frame)
button_frame.grid(row=5, column=0, columnspan=2, pady=10)
tk.Button(button_frame, text="Save", command=save, width=12).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Reset", command=reset, width=12).pack(side=tk.LEFT, padx=5)

root.mainloop()
