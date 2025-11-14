# admin.py - Python Logic Explanation

**File**: `admin.py`
**Purpose**: Admin dashboard for managing library operations - add members/books, search catalog, issue/return books, view reports

---

## Overview

This file provides the complete admin interface for the library management system. Admins can manage the entire book catalog, issue and return books, add new members and books, delete books, and generate weekly reports.

---

## Import Statements

```python
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector
import subprocess
import sys
from datetime import datetime, timedelta
from config import db_config
```

- **tkinter**: For GUI components
- **ttk**: Themed tkinter widgets (Treeview for tables)
- **messagebox**: For popup dialogs
- **simpledialog**: For asking user input in popup
- **mysql.connector**: Database connectivity
- **subprocess**: To launch add_member.py and add_book.py
- **sys**: To receive user_id from command line
- **datetime/timedelta**: For date calculations (due dates, weekly reports)
- **config**: Database credentials

---

## Global Variables

```python
admin_user_id = int(sys.argv[1]) if len(sys.argv) > 1 else None
```
- Receives admin's user_id from command line (passed by login.py)
- Used to track which admin performed actions in transactions table

---

## Helper Functions

### 1. `get_conn()` - Database Connection
```python
def get_conn():
    return mysql.connector.connect(**db_config)
```
- Returns a new database connection
- Used throughout the file for all database operations
- `**db_config` unpacks dictionary from config.py

### 2. `add_user()` - Launch Add Member Form
```python
def add_user():
    subprocess.Popen([sys.executable, 'add_member.py'])
```
- Opens add_member.py in a new process
- `sys.executable` ensures correct Python interpreter is used
- Allows admin to add new library members

### 3. `add_book()` - Launch Add Book Form
```python
def add_book():
    subprocess.Popen([sys.executable, 'add_book.py'])
```
- Opens add_book.py in a new process
- Form for adding new books with ISBN, author, copies, etc.

---

## Main Functions

### 4. `weekly_report()` - Generate Weekly Report

#### Purpose
Displays all library transactions from the last 7 days.

#### Logic Flow
```python
def weekly_report():
    # Create popup window
    win = tk.Toplevel(root)
    win.title("Weekly Report - Last 7 Days")
    win.geometry("800x500")
```
- `Toplevel` creates a new window on top of main window
- 800x500 pixels for displaying report table

#### Date Calculation
```python
week_ago = datetime.now() - timedelta(days=7)
```
- Gets current date/time
- Subtracts 7 days to get starting date
- `timedelta(days=7)` represents 7-day duration

#### Database Query
```python
cur.execute("SELECT action, book_id, member_id, transaction_date, notes FROM transactions WHERE transaction_date >= %s ORDER BY transaction_date DESC", (week_ago,))
transactions = cur.fetchall()
```
- Retrieves all transactions from last 7 days
- `ORDER BY transaction_date DESC` shows newest first
- Returns list of tuples

#### Display in Table
```python
cols = ('Date', 'Action', 'Book', 'Member ID', 'Notes')
tree = ttk.Treeview(win, columns=cols, show='headings', height=18)
```
- `Treeview` widget displays tabular data
- `show='headings'` hides default first column

#### Format Dates
```python
for trans in transactions:
    date_str = trans[3].strftime('%d/%m/%Y') if trans[3] else 'N/A'
    tree.insert('', tk.END, values=(date_str, trans[0], trans[1], trans[2] or 'N/A', trans[4] or ''))
```
- Loops through each transaction
- `strftime('%d/%m/%Y')` formats date as dd/mm/yyyy (Indian format)
- `trans[2] or 'N/A'` shows N/A if member_id is NULL (for delete actions)

---

### 5. `search_catalog()` - Main Catalog Search Interface

This is the most complex function with nested functions for better code organization.

#### Create Search Window
```python
def search_catalog():
    win = tk.Toplevel(root)
    win.title("Search Catalog")
    win.geometry("900x500")
```

#### Search Controls
```python
search_entry = tk.Entry(search_frame, font=("Arial", 11), width=30)
filter_var = tk.StringVar(value="Active")
filter_dropdown = tk.OptionMenu(search_frame, filter_var, "All", "Active", "Deleted")
```
- `search_entry`: Text field for searching books by title/author
- `filter_var`: StringVar to track dropdown selection
- `OptionMenu`: Dropdown with three options (All/Active/Deleted)

#### Catalog Table
```python
cols = ('Title', 'Author', 'Year', 'Total', 'Available', 'Action')
tree = ttk.Treeview(win, columns=cols, show='headings', height=15)
widths = [250, 200, 60, 80, 80, 180]
for i, col in enumerate(cols):
    tree.heading(col, text=col)
    tree.column(col, width=widths[i])
```
- Defines 6 columns for book information
- Sets specific width for each column
- `enumerate()` gives index and value in loop

---

#### Nested Function: `show_copies(_)` - View Book Copies Popup

##### Purpose
Shows all copies of a selected book with borrower details.

##### Get Selected Book
```python
sel = tree.selection()
if not sel: return
item_values = tree.item(sel[0])['values']
title = item_values[0].replace(" [Deleted]", "")
author = item_values[1]
```
- `tree.selection()` gets selected row
- `tree.item()` retrieves row data
- Removes "[Deleted]" suffix if present

##### Create Popup Window
```python
popup = tk.Toplevel(win)
popup.title(f"{title} - All Copies")
popup.geometry("900x500")
tk.Label(popup, text=f"{title} by {author}", font=("Arial", 14, "bold"), pady=10).pack()
```
- New popup window for copy details
- f-string for dynamic title

##### Query All Copies
```python
cur.execute("SELECT book_id, copy_number, book_status, issued_to_member_id, issue_date FROM books WHERE title=%s AND author=%s", (title, author))
copies = cur.fetchall()
```
- Gets all copies of selected book
- Each book can have multiple copies (Copy 1, Copy 2, etc.)

##### Display Copy Details
```python
for copy in copies:
    issued_to = 'Available'
    issue_date_str = 'N/A'
    due_date_str = 'N/A'

    if copy[3]:  # If issued_to_member_id exists
        cur.execute("SELECT name, username FROM members m JOIN users u ON m.user_id = u.user_id WHERE member_id = %s", (copy[3],))
        member = cur.fetchone()
        if member:
            issued_to = f"{member[0]} ({member[1]})"
```
- For each copy, check if it's issued
- **SQL JOIN**: Combines members and users tables to get name and username
- Displays "Name (username)" if issued, "Available" if not

##### Calculate Due Date
```python
if copy[4]:  # If issue_date exists
    issue_date_str = copy[4].strftime('%d/%m/%Y')
    due_date = copy[4] + timedelta(days=15)
    due_date_str = due_date.strftime('%d/%m/%Y')
```
- Due date = Issue date + 15 days
- `timedelta(days=15)` adds 15 days to date

---

##### Nested Function: `return_selected()` - Return Book from Popup

```python
def return_selected():
    sel_copy = copy_tree.selection()
    if not sel_copy:
        messagebox.showwarning("Warning", "Select a copy to return")
        return
    book_id = copy_tree.item(sel_copy[0])['values'][0]
    status = copy_tree.item(sel_copy[0])['values'][2]
```
- Gets selected copy from popup table
- Validates that a copy is selected
- Extracts book_id and status

##### Validate Copy Status
```python
if status != 'Issued':
    messagebox.showerror("Error", "This copy is not issued")
    return
```
- Can only return books that are currently issued

##### Update Database
```python
conn = get_conn()
cur = conn.cursor()
cur.execute("SELECT issued_to_member_id FROM books WHERE book_id=%s", (book_id,))
member_id = cur.fetchone()[0]
cur.execute("UPDATE books SET book_status='Returned', issued_to_member_id=NULL, issue_date=NULL WHERE book_id=%s", (book_id,))
```
- Gets member_id before clearing it
- Updates book status to 'Returned'
- Clears member_id and issue_date

##### Log Transaction
```python
cur.execute("INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes) VALUES (%s, %s, %s, 'Return', %s)", (book_id, member_id, admin_user_id, f"{title} by {author}"))
conn.commit()
```
- Records return action in transactions table
- Includes admin_user_id to track who processed return
- `commit()` saves changes to database

##### Refresh Display
```python
messagebox.showinfo("Success", "Book returned!")
popup.destroy()
search()
```
- Shows success message
- Closes popup window
- Refreshes catalog to show updated availability

---

#### Nested Function: `search()` - Perform Catalog Search

##### Clear Previous Results
```python
for row in tree.get_children():
    tree.delete(row)
```
- Removes all rows from table before new search

##### Build Search Query
```python
search_term = '%' + search_entry.get() + '%'
filter_status = filter_var.get()
```
- Adds `%` wildcards for SQL LIKE query
- `%term%` matches any string containing "term"

##### Execute Query Based on Filter
```python
if filter_status == "All":
    cur.execute("SELECT DISTINCT title, author, year, record_status FROM books WHERE title LIKE %s OR author LIKE %s", (search_term, search_term))
else:
    cur.execute("SELECT DISTINCT title, author, year, record_status FROM books WHERE (title LIKE %s OR author LIKE %s) AND record_status=%s", (search_term, search_term, filter_status))
```
- `DISTINCT` avoids duplicate entries (since multiple copies exist)
- Searches both title and author fields
- Applies record_status filter if not "All"

##### Count Copies
```python
for book in books:
    title, author, rec_status = book[0], book[1], book[3]

    if filter_status == "All":
        cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s", (title, author))
        total = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM books WHERE title=%s AND author=%s AND book_status IN ('Returned', 'New') AND record_status='Active'", (title, author))
        available = cur.fetchone()[0]
```
- For each unique book, counts total copies
- Counts available copies (status = 'Returned' or 'New')
- `COUNT(*)` SQL function returns number of rows

##### Display Results
```python
status_suffix = f" [{rec_status}]" if filter_status == "All" and rec_status == "Deleted" else ""
action_text = "Double-click to view copies"
tree.insert('', tk.END, values=(book[0] + status_suffix, book[1], book[2], total, available, action_text))
```
- Adds "[Deleted]" tag for deleted books when showing all
- Inserts row into table
- `tk.END` adds to end of list

---

#### Nested Function: `issue_book()` - Issue Book to Member

##### Get Selected Book
```python
sel = tree.selection()
if not sel:
    messagebox.showwarning("Warning", "Select a book first")
    return
item_values = tree.item(sel[0])['values']
title = item_values[0].replace(" [Deleted]", "")
author = item_values[1]
available = item_values[4]
```

##### Validate Book Status
```python
cur.execute("SELECT record_status FROM books WHERE title=%s AND author=%s LIMIT 1", (title, author))
book_rec = cur.fetchone()
if book_rec and book_rec[0] == 'Deleted':
    conn.close()
    messagebox.showerror("Error", "Cannot issue deleted books")
    return
```
- Cannot issue deleted books
- `LIMIT 1` returns only first result

##### Check Availability
```python
if available == 0:
    conn.close()
    messagebox.showerror("Error", "No copies available")
    return
```

##### Get Member Username
```python
member_username = simpledialog.askstring("Issue Book", "Enter member username:")
```
- `askstring()` shows popup dialog for text input

##### Lookup Member
```python
cur.execute("SELECT user_id FROM users WHERE username = %s AND user_type = 'member'", (member_username,))
user = cur.fetchone()
if user:
    cur.execute("SELECT member_id FROM members WHERE user_id = %s", (user[0],))
    member = cur.fetchone()
```
- Two-step lookup: users table → members table
- Validates username belongs to a member (not admin)

##### Find Available Copy
```python
cur.execute("SELECT book_id FROM books WHERE title=%s AND author=%s AND book_status IN ('Returned', 'New') AND record_status='Active' LIMIT 1", (title, author))
available_book = cur.fetchone()
```
- Finds first available copy
- This is how multiple copies work: searches for any copy with status 'Returned' or 'New'

##### Issue Book
```python
if available_book:
    book_id = available_book[0]
    issue_date = datetime.now().date()
    cur.execute("UPDATE books SET book_status='Issued', issued_to_member_id=%s, issue_date=%s WHERE book_id=%s", (member[0], issue_date, book_id))
```
- Updates specific copy with member_id and current date
- `.date()` extracts just the date part (no time)

##### Log Transaction
```python
cur.execute("INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes) VALUES (%s, %s, %s, 'Issue', %s)", (book_id, member[0], admin_user_id, f"{title} by {author}"))
conn.commit()
```
- Records issue action with admin tracking

##### Calculate and Display Due Date
```python
due_date = issue_date + timedelta(days=15)
messagebox.showinfo("Success", f"Book issued!\nIssue: {issue_date.strftime('%d/%m/%Y')}\nDue: {due_date.strftime('%d/%m/%Y')}")
search()
```
- Shows formatted dates in popup
- Refreshes catalog

---

#### Nested Function: `delete_book()` - Soft Delete Book

##### Get Selection
```python
sel = tree.selection()
if not sel:
    messagebox.showwarning("Warning", "Select a book first")
    return
item_values = tree.item(sel[0])['values']
title = item_values[0]
author = item_values[1]
```

##### Confirm Deletion
```python
confirm = messagebox.askyesno("Delete Book", f"Delete '{title}' by {author}?\n\nAll copies will be marked deleted.")
```
- `askyesno()` shows Yes/No dialog
- Returns True if user clicks Yes

##### Perform Soft Delete
```python
if confirm:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE books SET record_status='Deleted' WHERE title=%s AND author=%s", (title, author))
```
- Doesn't actually delete rows (DELETE FROM...)
- Sets record_status to 'Deleted' (soft delete)
- Preserves transaction history

##### Log Deletion
```python
cur.execute("SELECT book_id FROM books WHERE title=%s AND author=%s LIMIT 1", (title, author))
book = cur.fetchone()
if book:
    cur.execute("INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes) VALUES (%s, NULL, %s, 'Delete', %s)", (book[0], admin_user_id, f"{title} by {author}"))
```
- Records deletion with admin_user_id
- member_id is NULL for delete actions

---

#### Button Frame and Event Binding

```python
button_frame = tk.Frame(win)
button_frame.pack(pady=10)
tk.Button(button_frame, text="Search", command=search, font=("Arial", 11, "bold"), width=15).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Issue Book", command=issue_book, font=("Arial", 11, "bold"), width=15).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Delete Book", command=delete_book, font=("Arial", 11, "bold"), width=15).pack(side=tk.LEFT, padx=5)
```
- Three buttons at bottom of window
- `side=tk.LEFT` arranges horizontally

```python
tree.bind('<Double-1>', show_copies)
```
- Binds double-click event to show_copies function
- `<Double-1>` = double left-click

```python
search()
```
- Calls search immediately to show all books when window opens

---

## Main Window Setup

### Create Root Window
```python
root = tk.Tk()
root.title("Library Management System - Admin")
root.geometry("800x600")
root.resizable(False, False)
```

### Center Window on Screen
```python
root.update_idletasks()
x = (root.winfo_screenwidth() // 2) - 400
y = (root.winfo_screenheight() // 2) - 300
root.geometry(f'800x600+{x}+{y}')
```
- `winfo_screenwidth()` gets monitor width
- `//` is integer division
- Calculates position to center 800x600 window
- `+{x}+{y}` syntax sets window position

### Header Section
```python
header = tk.Frame(root, bg="#2196F3", height=80)
header.pack(fill=tk.X)
tk.Label(header, text="Admin Dashboard", font=("Arial", 18, "bold"), bg="#2196F3", fg="white").place(x=280, y=25)
tk.Button(header, text="Logout", font=("Arial", 10), command=root.destroy).place(x=700, y=25)
```
- Blue header bar (#2196F3 = Material Design Blue)
- `fill=tk.X` stretches horizontally
- `.place()` uses absolute positioning
- Logout button destroys window

### Main Content Area
```python
content = tk.Frame(root, bg="#f5f5f5")
content.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)

button_container = tk.Frame(content, bg="#f5f5f5")
button_container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
```
- Light gray background (#f5f5f5)
- `expand=True` makes frame fill available space
- `relx=0.5, rely=0.5` centers container (50% from left, 50% from top)

### Dashboard Buttons
```python
buttons = [("Add Member", add_user), ("Add Book", add_book), ("Search Catalog", search_catalog), ("Weekly Reports", weekly_report)]
for i, (text, cmd) in enumerate(buttons):
    tk.Button(button_container, text=text, font=("Arial", 12, "bold"), width=20, height=2, command=cmd).grid(row=i//2, column=i%2, padx=20, pady=20)
```
- List of tuples (button text, function to call)
- `enumerate()` gives index i
- `i//2` calculates row (0,0,1,1 → 0,0,1,1)
- `i%2` calculates column (0,1,0,1)
- Creates 2x2 grid of buttons

### Start Event Loop
```python
root.mainloop()
```

---

## CBSE Class XII Concepts Demonstrated

1. **Functions and Nested Functions**: Organizing code logically
2. **Database Operations**: INSERT, UPDATE, SELECT with parameterized queries
3. **GUI Programming**: Advanced tkinter with multiple windows
4. **Event Handling**: Button clicks, double-clicks, Enter key
5. **Date/Time Operations**: datetime, timedelta, strftime()
6. **String Operations**: f-strings, concatenation, .replace()
7. **List Comprehension**: Loop iterations
8. **SQL Joins**: Combining members and users tables
9. **Aggregate Functions**: COUNT() in SQL
10. **Data Validation**: Input checks before database operations

---

## Database Tables Used

1. **users**: username, password, user_type, status
2. **members**: member_id, user_id, name
3. **books**: book_id, title, author, isbn, year, copy_number, book_status, record_status, issued_to_member_id, issue_date
4. **transactions**: transaction_id, book_id, member_id, admin_user_id, action, transaction_date, notes

---

## Key Features

- ✅ Search books with filters (All/Active/Deleted)
- ✅ View all copies of a book with borrower details
- ✅ Issue books to members
- ✅ Return books from popup window
- ✅ Soft delete books (preserves history)
- ✅ Generate weekly transaction reports
- ✅ Admin accountability tracking
- ✅ Multiple copies support
- ✅ Due date calculations (15 days)
- ✅ Date formatting (dd/mm/yyyy)
