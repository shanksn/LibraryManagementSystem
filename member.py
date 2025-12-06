"""Member Screen - Library Management System"""
import tkinter as tk
from tkinter import ttk
import mysql.connector
import sys
from datetime import timedelta
from config import db_config  # Import database settings from config.py

user_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1

def get_conn():
    return mysql.connector.connect(**db_config)

def refresh_borrowed():
    for row in borrowed_tree.get_children(): borrowed_tree.delete(row)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT member_id FROM members WHERE user_id=%s", (user_id,))
    member = cur.fetchone()
    if member:
        cur.execute("SELECT book_id, title, author, year, issue_date FROM books WHERE issued_to_member_id=%s AND book_status='Issued'", (member[0],))
        for book in cur.fetchall():
            issue_date_str = 'N/A'
            due_date_str = 'N/A'
            if book[4]:
                issue_date_str = book[4].strftime('%d/%m/%Y')
                due_date = book[4] + timedelta(days=15)
                due_date_str = due_date.strftime('%d/%m/%Y')
            borrowed_tree.insert('', tk.END, values=(book[0], book[1], book[2], book[3], issue_date_str, due_date_str))
    conn.close()

def search_books():
    for row in search_tree.get_children(): search_tree.delete(row)
    conn = get_conn()
    cur = conn.cursor()
    search_term = '%' + search_entry.get() + '%'

    # Get distinct books that have at least one available copy
    cur.execute("SELECT DISTINCT title, author, year FROM books WHERE (title LIKE %s OR author LIKE %s OR year LIKE %s) AND book_status IN ('Returned', 'New') AND record_status='Active'",
                (search_term, search_term, search_term))
    books = cur.fetchall()

    for book in books:
        title, author, year = book[0], book[1], book[2]
        # Count available copies for this book
        cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s AND book_status IN ('Returned', 'New') AND record_status='Active'",
                    (title, author))
        available = cur.fetchone()[0]

        # Only show if there are available copies
        if available > 0:
            search_tree.insert('', tk.END, values=(title, author, year, available))

    conn.close()

root = tk.Tk()
root.title("Library Management System - Member")
root.geometry("800x600")
root.resizable(False, False)

root.update_idletasks()
x = (root.winfo_screenwidth() // 2) - 400
y = (root.winfo_screenheight() // 2) - 300
root.geometry(f'800x600+{x}+{y}')

# Header
header = tk.Frame(root, bg="#4CAF50", height=70)
header.pack(fill=tk.X)
tk.Label(header, text="Member Portal", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white").pack(pady=20)
tk.Button(header, text="Logout", font=("Arial", 10), command=root.destroy).place(x=700, y=20)

# Main container
main = tk.Frame(root, bg="#f5f5f5")
main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# My Borrowed Books section
borrowed_frame = tk.Frame(main, bg="white", relief=tk.RAISED, bd=1)
borrowed_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 5))

tk.Label(borrowed_frame, text="My Borrowed Books", font=("Arial", 14, "bold"), bg="white").pack(pady=10)

cols = ('ID', 'Title', 'Author', 'Year', 'Issue Date', 'Due Date')
borrowed_tree = ttk.Treeview(borrowed_frame, columns=cols, show='headings', height=5)
widths = [50, 200, 150, 80, 100, 100]
for i, col in enumerate(cols):
    borrowed_tree.heading(col, text=col)
    borrowed_tree.column(col, width=widths[i])
borrowed_tree.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

# Search Books section
search_frame = tk.Frame(main, bg="white", relief=tk.RAISED, bd=1)
search_frame.pack(fill=tk.BOTH, expand=True)

tk.Label(search_frame, text="Search Available Books", font=("Arial", 14, "bold"), bg="white").pack(pady=10)

search_bar = tk.Frame(search_frame, bg="white")
search_bar.pack()
tk.Label(search_bar, text="Search:", bg="white").pack(side=tk.LEFT, padx=5)
search_entry = tk.Entry(search_bar, font=("Arial", 11), width=35)
search_entry.pack(side=tk.LEFT, padx=5)
tk.Button(search_bar, text="Search", command=search_books).pack(side=tk.LEFT, padx=5)

search_cols = ('Title', 'Author', 'Year', 'Available Copies')
search_tree = ttk.Treeview(search_frame, columns=search_cols, show='headings', height=8)
search_widths = [280, 200, 80, 110]
for i, col in enumerate(search_cols):
    search_tree.heading(col, text=col)
    search_tree.column(col, width=search_widths[i])
search_tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

tk.Label(search_frame, text="Contact admin to issue books", font=("Arial", 10), bg="white", fg="#666").pack(pady=10)

refresh_borrowed()
search_books()

root.mainloop()
