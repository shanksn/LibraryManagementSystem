"""Admin Screen - Library Management System"""
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector
import subprocess
import sys
from datetime import datetime, timedelta
from config import db_config  # Import database settings from config.py

# Get admin user_id from command line
admin_user_id = int(sys.argv[1]) if len(sys.argv) > 1 else None

def get_conn():
    return mysql.connector.connect(**db_config)

def add_user():
    subprocess.Popen([sys.executable, 'add_member.py'])

def add_book():
    subprocess.Popen([sys.executable, 'add_book.py'])

def search_catalog():
    win = tk.Toplevel(root)
    win.title("Search Catalog")
    win.geometry("900x500")

    search_frame = tk.Frame(win)
    search_frame.pack(pady=5)

    tk.Label(search_frame, text="Search:", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
    search_entry = tk.Entry(search_frame, font=("Arial", 11), width=30)
    search_entry.pack(side=tk.LEFT, padx=5)

    tk.Label(search_frame, text="Filter:", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
    filter_var = tk.StringVar(value="Active")
    filter_dropdown = tk.OptionMenu(search_frame, filter_var, "All", "Active", "Deleted")
    filter_dropdown.config(font=("Arial", 10))
    filter_dropdown.pack(side=tk.LEFT, padx=5)

    cols = ('Title', 'Author', 'Year', 'Total Copies', 'Available', 'Borrowers')
    tree = ttk.Treeview(win, columns=cols, show='headings', height=15)
    widths = [250, 200, 80, 100, 100, 150]
    for i, col in enumerate(cols):
        tree.heading(col, text=col)
        tree.column(col, width=widths[i])
    tree.pack(pady=10, fill=tk.BOTH, expand=True)

    def show_copies(event):
        sel = tree.selection()
        if not sel: return
        item_values = tree.item(sel[0])['values']
        title = item_values[0]
        author = item_values[1]

        popup = tk.Toplevel(win)
        popup.title(f"{title} - All Copies")
        popup.geometry("700x400")

        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT book_id, copy_number, book_status, issued_to_member_id, issue_date FROM books WHERE title=%s AND author=%s", (title, author))
        copies = cur.fetchall()

        copy_cols = ('Book ID', 'Copy#', 'Status', 'Issued To', 'Issue Date', 'Due Date')
        copy_tree = ttk.Treeview(popup, columns=copy_cols, show='headings', height=12)
        copy_widths = [70, 60, 80, 150, 100, 100]
        for i, col in enumerate(copy_cols):
            copy_tree.heading(col, text=col)
            copy_tree.column(col, width=copy_widths[i])
        copy_tree.pack(pady=10, fill=tk.BOTH, expand=True)

        for copy in copies:
            issued_to = 'N/A'
            issue_date_str = 'N/A'
            due_date_str = 'N/A'

            if copy[3]:
                cur.execute("SELECT name FROM members WHERE member_id = %s", (copy[3],))
                member = cur.fetchone()
                if member:
                    issued_to = member[0]

            if copy[4]:
                issue_date_str = copy[4].strftime('%d/%m/%Y')
                due_date = copy[4] + timedelta(days=15)
                due_date_str = due_date.strftime('%d/%m/%Y')

            copy_tree.insert('', tk.END, values=(copy[0], copy[1], copy[2], issued_to, issue_date_str, due_date_str))
        conn.close()

        def return_from_popup():
            sel_copy = copy_tree.selection()
            if not sel_copy:
                messagebox.showwarning("Warning", "Select a copy first")
                return
            book_id = copy_tree.item(sel_copy[0])['values'][0]
            status = copy_tree.item(sel_copy[0])['values'][2]

            if status != 'Issued':
                messagebox.showerror("Error", "This copy is not issued")
                return

            conn = get_conn()
            cur = conn.cursor()
            cur.execute("SELECT issued_to_member_id, title, author FROM books WHERE book_id=%s", (book_id,))
            book_data = cur.fetchone()
            cur.execute("UPDATE books SET book_status='Returned', issued_to_member_id=NULL, issue_date=NULL WHERE book_id=%s", (book_id,))
            cur.execute("INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes) VALUES (%s, %s, %s, 'Return', %s)",
                       (book_id, book_data[0], admin_user_id, f"{book_data[1]} by {book_data[2]}"))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Book returned successfully!")
            popup.destroy()
            search()

        tk.Button(popup, text="Return Selected Copy", command=return_from_popup, font=("Arial", 11, "bold"), width=20).pack(pady=10)

    tree.bind('<Double-1>', show_copies)

    def search():
        for row in tree.get_children(): tree.delete(row)
        conn = get_conn()
        cur = conn.cursor()
        search_term = '%' + search_entry.get() + '%'
        filter_status = filter_var.get()

        if filter_status == "All":
            cur.execute("SELECT DISTINCT title, author, year, record_status FROM books WHERE title LIKE %s OR author LIKE %s", (search_term, search_term))
        else:
            cur.execute("SELECT DISTINCT title, author, year, record_status FROM books WHERE (title LIKE %s OR author LIKE %s) AND record_status=%s", (search_term, search_term, filter_status))
        books = cur.fetchall()

        for book in books:
            title, author, year, rec_status = book[0], book[1], book[2], book[3]

            if filter_status == "All":
                cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s", (title, author))
                total = cur.fetchone()[0]
                cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s AND book_status IN ('Returned', 'New') AND record_status='Active'", (title, author))
                available = cur.fetchone()[0]
                cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s AND book_status='Issued'", (title, author))
                issued_count = cur.fetchone()[0]
            else:
                cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s AND record_status=%s", (title, author, filter_status))
                total = cur.fetchone()[0]
                cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s AND book_status IN ('Returned', 'New') AND record_status=%s", (title, author, filter_status))
                available = cur.fetchone()[0]
                cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s AND book_status='Issued' AND record_status=%s", (title, author, filter_status))
                issued_count = cur.fetchone()[0]

            borrowers_text = f"{issued_count} borrower(s)" if issued_count > 0 else "None"
            if issued_count > 0:
                borrowers_text += " (Double-click)"

            status_suffix = f" [{rec_status}]" if filter_status == "All" and rec_status == "Deleted" else ""
            tree.insert('', tk.END, values=(book[0] + status_suffix, book[1], book[2], total, available, borrowers_text))
        conn.close()

    def issue_book():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Warning", "Select a book first")
            return

        item_values = tree.item(sel[0])['values']
        title = item_values[0].replace(" [Deleted]", "")  # Remove status suffix if present
        author = item_values[1]
        available = item_values[4]

        # Check if book is deleted
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT record_status FROM books WHERE title=%s AND author=%s LIMIT 1", (title, author))
        book_rec = cur.fetchone()
        if book_rec and book_rec[0] == 'Deleted':
            conn.close()
            messagebox.showerror("Error", "Cannot issue deleted books")
            return

        if available == 0:
            conn.close()
            messagebox.showerror("Error", "No copies available for this book")
            return

        member_username = simpledialog.askstring("Issue Book", "Enter member username:")
        if member_username:
            cur.execute("SELECT user_id FROM users WHERE username = %s AND user_type = 'member'", (member_username,))
            user = cur.fetchone()
            if user:
                cur.execute("SELECT member_id FROM members WHERE user_id = %s", (user[0],))
                member = cur.fetchone()
                if member:
                    cur.execute("SELECT book_id FROM books WHERE title=%s AND author=%s AND book_status IN ('Returned', 'New') AND record_status='Active' LIMIT 1", (title, author))
                    available_book = cur.fetchone()
                    if available_book:
                        book_id = available_book[0]
                        issue_date = datetime.now().date()
                        cur.execute("UPDATE books SET book_status='Issued', issued_to_member_id=%s, issue_date=%s WHERE book_id=%s",
                                   (member[0], issue_date, book_id))
                        cur.execute("INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes) VALUES (%s, %s, %s, 'Issue', %s)",
                                   (book_id, member[0], admin_user_id, f"{title} by {author}"))
                        conn.commit()
                        due_date = issue_date + timedelta(days=15)
                        issue_date_formatted = issue_date.strftime('%d/%m/%Y')
                        due_date_formatted = due_date.strftime('%d/%m/%Y')
                        messagebox.showinfo("Success", f"Book issued!\nIssue Date: {issue_date_formatted}\nDue Date: {due_date_formatted}")
                        search()
                    else:
                        messagebox.showerror("Error", "No available copy found")
                else:
                    messagebox.showerror("Error", "Member details not found")
            else:
                messagebox.showerror("Error", "Member username not found")
            conn.close()

    def delete_book():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Warning", "Select a book first")
            return

        item_values = tree.item(sel[0])['values']
        title = item_values[0]
        author = item_values[1]

        confirm = messagebox.askyesno("Delete Book", f"Do you want to delete '{title}' by {author}?\n\nThis will mark all copies as deleted.")
        if confirm:
            conn = get_conn()
            cur = conn.cursor()
            cur.execute("UPDATE books SET record_status='Deleted' WHERE title=%s AND author=%s", (title, author))
            cur.execute("SELECT book_id FROM books WHERE title=%s AND author=%s LIMIT 1", (title, author))
            book = cur.fetchone()
            if book:
                cur.execute("INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes) VALUES (%s, NULL, %s, 'Delete', %s)",
                           (book[0], admin_user_id, f"{title} by {author}"))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Book deleted successfully!")
            search()

    button_frame = tk.Frame(win)
    button_frame.pack(pady=10)
    tk.Button(button_frame, text="Search", command=search, font=("Arial", 11, "bold"), width=15).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Issue Book", command=issue_book, font=("Arial", 11, "bold"), width=15).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Delete Book", command=delete_book, font=("Arial", 11, "bold"), width=15).pack(side=tk.LEFT, padx=5)
    search()

root = tk.Tk()
root.title("Library Management System - Admin")
root.geometry("800x600")
root.resizable(False, False)

root.update_idletasks()
x = (root.winfo_screenwidth() // 2) - 400
y = (root.winfo_screenheight() // 2) - 300
root.geometry(f'800x600+{x}+{y}')

header = tk.Frame(root, bg="#2196F3", height=80)
header.pack(fill=tk.X)
tk.Label(header, text="Admin Dashboard", font=("Arial", 18, "bold"), bg="#2196F3", fg="white").place(x=280, y=25)
tk.Button(header, text="Logout", font=("Arial", 10), command=root.destroy).place(x=700, y=25)

content = tk.Frame(root, bg="#f5f5f5")
content.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)

buttons = [("Add Member", add_user), ("Add Book", add_book), ("Search Catalog", search_catalog)]
for i, (text, cmd) in enumerate(buttons):
    tk.Button(content, text=text, font=("Arial", 12, "bold"), width=20, height=2, command=cmd).grid(row=i//2, column=i%2, padx=20, pady=20)

root.mainloop()
