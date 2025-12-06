# Admin Screen - Library Management System
# Class XII Computer Science Project

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector
import subprocess
import sys
from datetime import datetime, timedelta
from PIL import Image, ImageTk
from config import db_config

admin_user_id = int(sys.argv[1]) if len(sys.argv) > 1 else None

# Track open windows to prevent duplicates
open_windows = {
    'add_member': None,
    'add_book': None,
    'search_catalog': None,
    'weekly_report': None
}

def get_conn():
    return mysql.connector.connect(**db_config)

def add_user():
    # Check if window is already open
    if open_windows['add_member'] is not None and open_windows['add_member'].poll() is None:
        return
    open_windows['add_member'] = subprocess.Popen([sys.executable, 'add_member.py'])

def add_book():
    # Check if window is already open
    if open_windows['add_book'] is not None and open_windows['add_book'].poll() is None:
        return
    # Pass admin_user_id to add_book.py
    open_windows['add_book'] = subprocess.Popen([sys.executable, 'add_book.py', str(admin_user_id)])

def weekly_report():
    # Check if window is already open
    if open_windows['weekly_report'] is not None and open_windows['weekly_report'].winfo_exists():
        open_windows['weekly_report'].lift()
        return

    win = tk.Toplevel(root)
    win.title("Weekly Report - Last 7 Days")
    win.geometry("800x500")
    open_windows['weekly_report'] = win
    tk.Label(win, text="Weekly Library Report", font=("Arial", 16, "bold")).pack(pady=10)

    conn = get_conn()
    cur = conn.cursor()
    week_ago = datetime.now() - timedelta(days=7)
    cur.execute("SELECT action, book_id, member_id, transaction_date, notes, admin_user_id FROM transactions WHERE transaction_date >= %s ORDER BY transaction_date DESC", (week_ago,))
    transactions = cur.fetchall()

    cols = ('Date', 'Action', 'Book', 'Member', 'Notes')
    tree = ttk.Treeview(win, columns=cols, show='headings', height=18)
    for col in cols:
        tree.heading(col, text=col)
    tree.column('Date', width=100)
    tree.column('Action', width=80)
    tree.column('Book', width=80)
    tree.column('Member', width=120)
    tree.column('Notes', width=360)
    tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    for trans in transactions:
        date_str = trans[3].strftime('%d/%m/%Y') if trans[3] else 'N/A'
        action = trans[0]

        # Determine who to show in Member column based on action
        member_name = 'N/A'
        if action == 'Add' or action == 'Delete':
            # For Add/Delete, show admin username
            if trans[5]:  # admin_user_id
                cur.execute("SELECT username FROM users WHERE user_id = %s", (trans[5],))
                admin = cur.fetchone()
                if admin:
                    member_name = admin[0]
        elif action == 'Return':
            # For Return, show admin username (who processed the return)
            if trans[5]:  # admin_user_id
                cur.execute("SELECT username FROM users WHERE user_id = %s", (trans[5],))
                admin = cur.fetchone()
                if admin:
                    member_name = admin[0]
        else:
            # For Issue, show member username
            if trans[2]:  # member_id
                cur.execute("SELECT username FROM users u JOIN members m ON u.user_id = m.user_id WHERE m.member_id = %s", (trans[2],))
                member = cur.fetchone()
                if member:
                    member_name = member[0]

        tree.insert('', tk.END, values=(date_str, trans[0], trans[1], member_name, trans[4] or ''))
    conn.close()

def search_catalog():
    # Check if window is already open
    if open_windows['search_catalog'] is not None and open_windows['search_catalog'].winfo_exists():
        open_windows['search_catalog'].lift()
        return

    win = tk.Toplevel(root)
    win.title("Search Catalog")
    win.geometry("900x500")

    # Set window icon
    try:
        icon_image = tk.PhotoImage(file='search_catalog.png')
        win.iconphoto(False, icon_image)
    except:
        pass  # If icon file not found, continue without it

    open_windows['search_catalog'] = win

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

    cols = ('Title', 'Author', 'Year', 'Total', 'Available', 'Action')
    tree = ttk.Treeview(win, columns=cols, show='headings', height=15)
    widths = [250, 200, 60, 80, 80, 180]
    for i, col in enumerate(cols):
        tree.heading(col, text=col)
        tree.column(col, width=widths[i])
    tree.pack(pady=10, fill=tk.BOTH, expand=True)

    # Track popup window to prevent duplicates
    popup_window = None

    def search():
        for row in tree.get_children(): tree.delete(row)
        conn = get_conn()
        cur = conn.cursor()
        search_term = '%' + search_entry.get() + '%'
        filter_status = filter_var.get()

        if filter_status == "All":
            cur.execute("SELECT DISTINCT title, author, year, record_status FROM books WHERE title LIKE %s OR author LIKE %s OR year LIKE %s", (search_term, search_term, search_term))
        else:
            cur.execute("SELECT DISTINCT title, author, year, record_status FROM books WHERE (title LIKE %s OR author LIKE %s OR year LIKE %s) AND record_status=%s", (search_term, search_term, search_term, filter_status))
        books = cur.fetchall()

        for book in books:
            title, author, rec_status = book[0], book[1], book[3]
            if filter_status == "All":
                cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s", (title, author))
                total = cur.fetchone()[0]
                cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s AND book_status IN ('Returned', 'New') AND record_status='Active'", (title, author))
                available = cur.fetchone()[0]
            else:
                cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s AND record_status=%s", (title, author, filter_status))
                total = cur.fetchone()[0]
                if filter_status == "Deleted":
                    # For deleted books, show 0 available
                    available = 0
                else:
                    cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s AND book_status IN ('Returned', 'New') AND record_status=%s", (title, author, filter_status))
                    available = cur.fetchone()[0]

            status_suffix = f" [{rec_status}]" if filter_status == "All" and rec_status == "Deleted" else ""
            # Set action text based on record status
            if rec_status == "Deleted":
                action_text = "Deleted Book"
            elif filter_status == "Deleted":
                action_text = "Deleted Book"
            else:
                action_text = "Double-click to view copies"
            tree.insert('', tk.END, values=(book[0] + status_suffix, book[1], book[2], total, available, action_text))
        conn.close()

    def show_copies(_):
        nonlocal popup_window

        # Prevent duplicate windows - close existing popup if open
        if popup_window and popup_window.winfo_exists():
            popup_window.destroy()

        sel = tree.selection()
        if not sel: return
        item_values = tree.item(sel[0])['values']

        # Don't allow double-click on deleted books
        if item_values[5] == "Deleted Book":
            return

        title = item_values[0].replace(" [Deleted]", "")
        author = item_values[1]

        popup = tk.Toplevel(win)
        popup.title(f"{title} - All Copies")
        popup.geometry("900x500")
        popup_window = popup  # Track this window

        tk.Label(popup, text=f"{title} by {author}", font=("Arial", 14, "bold"), pady=10).pack()

        copy_cols = ('Book ID', 'Copy#', 'Status', 'Issued To', 'Issue Date', 'Due Date')
        copy_tree = ttk.Treeview(popup, columns=copy_cols, show='headings', height=12)
        copy_widths = [80, 70, 90, 200, 120, 120]
        for i, col in enumerate(copy_cols):
            copy_tree.heading(col, text=col)
            copy_tree.column(col, width=copy_widths[i])
        copy_tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        def refresh_copies():
            # Clear existing rows
            for row in copy_tree.get_children():
                copy_tree.delete(row)

            # Reload copy data from database
            conn = get_conn()
            cur = conn.cursor()
            cur.execute("SELECT book_id, copy_number, book_status, issued_to_member_id, issue_date, record_status FROM books WHERE title=%s AND author=%s", (title, author))
            copies = cur.fetchall()

            for copy in copies:
                issued_to = 'N/A'
                issue_date_str = 'N/A'
                due_date_str = 'N/A'
                # Check if book is deleted
                book_status = copy[2] if copy[5] == 'Active' else 'Deleted'
                # Only show member info if book is currently issued
                if copy[3]:
                    cur.execute("SELECT name, username FROM members m JOIN users u ON m.user_id = u.user_id WHERE member_id = %s", (copy[3],))
                    member = cur.fetchone()
                    if member:
                        issued_to = f"{member[0]} ({member[1]})"
                if copy[4]:
                    issue_date_str = copy[4].strftime('%d/%m/%Y')
                    due_date = copy[4] + timedelta(days=15)
                    due_date_str = due_date.strftime('%d/%m/%Y')
                copy_tree.insert('', tk.END, values=(copy[0], copy[1], book_status, issued_to, issue_date_str, due_date_str))
            conn.close()

        # Load initial data
        refresh_copies()

        def return_selected():
            sel_copy = copy_tree.selection()
            if not sel_copy:
                messagebox.showwarning("Warning", "Select a copy to return")
                return
            book_id = copy_tree.item(sel_copy[0])['values'][0]
            status = copy_tree.item(sel_copy[0])['values'][2]
            if status != 'Issued':
                messagebox.showerror("Error", "This copy is not issued")
                return
            conn = get_conn()
            cur = conn.cursor()
            cur.execute("SELECT issued_to_member_id FROM books WHERE book_id=%s", (book_id,))
            member_id = cur.fetchone()[0]
            cur.execute("UPDATE books SET book_status='Returned', issued_to_member_id=NULL, issue_date=NULL WHERE book_id=%s", (book_id,))
            cur.execute("INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes) VALUES (%s, %s, %s, 'Return', %s)", (book_id, member_id, admin_user_id, f"{title} by {author}"))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Book returned!")
            refresh_copies()  # Refresh the list instead of closing popup
            search()  # Update main catalog

        button_frame = tk.Frame(popup)
        button_frame.pack(side=tk.BOTTOM, pady=15)
        tk.Button(button_frame, text="Return Selected Copy", command=return_selected, font=("Arial", 11, "bold"), width=25).pack()

    tree.bind('<Double-1>', show_copies)

    def issue_book():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Warning", "Select a book first")
            return

        item_values = tree.item(sel[0])['values']
        title = item_values[0].replace(" [Deleted]", "")
        author = item_values[1]
        available = item_values[4]

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
            messagebox.showerror("Error", "No copies available")
            return

        member_username = simpledialog.askstring("Issue Book", "Enter member username:")
        if member_username:
            cur.execute("SELECT user_id FROM users WHERE username = %s AND user_type = 'member'", (member_username,))
            user = cur.fetchone()
            if user:
                cur.execute("SELECT member_id FROM members WHERE user_id = %s", (user[0],))
                member = cur.fetchone()
                if member:
                    # Check if member already has 3 books (borrowing limit)
                    cur.execute("SELECT COUNT(*) FROM books WHERE issued_to_member_id = %s AND book_status = 'Issued'", (member[0],))
                    current_books = cur.fetchone()[0]
                    if current_books >= 3:
                        conn.close()
                        messagebox.showerror("Error", f"Member '{member_username}' already has 3 books issued.\nMaximum borrowing limit reached.")
                        return

                    cur.execute("SELECT book_id FROM books WHERE title=%s AND author=%s AND book_status IN ('Returned', 'New') AND record_status='Active' LIMIT 1", (title, author))
                    available_book = cur.fetchone()
                    if available_book:
                        book_id = available_book[0]
                        issue_date = datetime.now().date()
                        cur.execute("UPDATE books SET book_status='Issued', issued_to_member_id=%s, issue_date=%s WHERE book_id=%s", (member[0], issue_date, book_id))
                        cur.execute("INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes) VALUES (%s, %s, %s, 'Issue', %s)", (book_id, member[0], admin_user_id, f"{title} by {author}"))
                        conn.commit()
                        due_date = issue_date + timedelta(days=15)
                        messagebox.showinfo("Success", f"Book issued!\nIssue: {issue_date.strftime('%d/%m/%Y')}\nDue: {due_date.strftime('%d/%m/%Y')}")
                        search()
                    else:
                        messagebox.showerror("Error", "No available copy found")
                else:
                    messagebox.showerror("Error", "Member not found")
            else:
                messagebox.showerror("Error", "Username not found")
            conn.close()

    def delete_book():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Warning", "Select a book first")
            return

        item_values = tree.item(sel[0])['values']
        title = item_values[0].replace(" [Deleted]", "")
        author = item_values[1]

        conn = get_conn()
        cur = conn.cursor()

        # Check if any copy of this book is currently issued
        cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s AND book_status='Issued'", (title, author))
        issued_count = cur.fetchone()[0]

        if issued_count > 0:
            conn.close()
            messagebox.showerror("Error", f"Cannot delete '{title}' by {author}.\n\n{issued_count} cop{'y is' if issued_count == 1 else 'ies are'} currently issued to members.\nPlease return all copies before deleting.")
            return

        confirm = messagebox.askyesno("Delete Book", f"Delete '{title}' by {author}?\n\nAll copies will be marked deleted.")
        if confirm:
            cur.execute("UPDATE books SET record_status='Deleted' WHERE title=%s AND author=%s", (title, author))
            cur.execute("SELECT book_id FROM books WHERE title=%s AND author=%s LIMIT 1", (title, author))
            book = cur.fetchone()
            if book:
                cur.execute("INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes) VALUES (%s, NULL, %s, 'Delete', %s)", (book[0], admin_user_id, f"{title} by {author}"))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Book deleted!")
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

# Load and display admin icon next to heading
try:
    admin_icon_img = Image.open("images/admin_portal.png").resize((40, 40))
    admin_icon_photo = ImageTk.PhotoImage(admin_icon_img)
    tk.Label(header, image=admin_icon_photo, bg="#2196F3").place(x=230, y=20)
    # Keep reference to prevent garbage collection
    header.admin_icon = admin_icon_photo
except:
    pass  # If icon not found, continue without it

tk.Label(header, text="Admin Dashboard", font=("Arial", 18, "bold"), bg="#2196F3", fg="white").place(x=280, y=25)
tk.Button(header, text="Logout", font=("Arial", 10), command=root.destroy).place(x=700, y=25)

content = tk.Frame(root, bg="#f5f5f5")
content.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)

button_container = tk.Frame(content, bg="#f5f5f5")
button_container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Load button icons
button_icons = {}
icon_files = {
    "Add Member": "images/add_member.png",
    "Add Book": "images/add_books.png",
    "Search Catalog": "images/search_catalog.png",
    "Weekly Reports": "images/weekly_report.png"
}

for name, file in icon_files.items():
    try:
        img = Image.open(file).resize((30, 30))
        button_icons[name] = ImageTk.PhotoImage(img)
    except:
        button_icons[name] = None

buttons = [("Add Member", add_user), ("Add Book", add_book), ("Search Catalog", search_catalog), ("Weekly Reports", weekly_report)]
for i, (text, cmd) in enumerate(buttons):
    btn_frame = tk.Frame(button_container, bg="#f5f5f5")
    btn_frame.grid(row=i//2, column=i%2, padx=20, pady=20)

    # Add icon if available
    if button_icons.get(text):
        tk.Label(btn_frame, image=button_icons[text], bg="#f5f5f5").pack(side=tk.TOP, pady=5)

    tk.Button(btn_frame, text=text, font=("Arial", 12, "bold"), width=20, height=2, command=cmd).pack(side=tk.TOP)

# Keep references to prevent garbage collection
root.button_icons = button_icons

root.mainloop()
