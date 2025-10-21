import tkinter as tk
from tkinter import ttk
import mysql.connector

# MySQL connection config - replace with real values
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'invasion',
    'database': 'library_management_system',
}

def get_connection():
    return mysql.connector.connect(**db_config)

def search():
    for row in tree.get_children(): tree.delete(row)
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT title, author, year FROM books WHERE title LIKE %s", ('%' + entry.get() + '%',))
    for (t,a,y) in cur.fetchall(): tree.insert("", "end", values=(t,a,y))
    con.close()

root = tk.Tk(); root.title("Book Search"); root.geometry("500x300")
tk.Label(root, text="Search Book:").pack()
entry = tk.Entry(root, width=40); entry.pack()
tk.Button(root, text="Search", command=search).pack(pady=5)

cols = ("Title", "Author", "Year")
tree = ttk.Treeview(root, columns=cols, show="headings")
for c in cols: tree.heading(c, text=c); tree.column(c, width=150)
tree.pack(pady=10, fill="both", expand=True)
root.mainloop()
