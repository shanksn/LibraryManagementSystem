# member.py - Python Logic Explanation

**File**: `member.py`
**Purpose**: Member portal for viewing borrowed books and searching available books in the library catalog

---

## Overview

This file provides a read-only interface for library members. Members can view their currently borrowed books with due dates and search the available book catalog. Members cannot issue or return books themselves - they must contact an admin.

---

## Import Statements

```python
import tkinter as tk
from tkinter import ttk
import mysql.connector
import sys
from datetime import timedelta
from config import db_config
```

- **tkinter**: For GUI components
- **ttk**: For Treeview table widgets
- **mysql.connector**: Database connectivity
- **sys**: To receive user_id from command line
- **timedelta**: For calculating due dates
- **config**: Database credentials from config.py

---

## Global Variables

```python
user_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
```
- Receives member's user_id from command line (passed by login.py)
- Default value of 1 if no argument provided (for testing)
- Used to identify which member is logged in

---

## Helper Function

### `get_conn()` - Database Connection
```python
def get_conn():
    return mysql.connector.connect(**db_config)
```
- Returns a new MySQL database connection
- Uses credentials from config.py
- `**db_config` unpacks dictionary as keyword arguments

---

## Main Functions

### 1. `refresh_borrowed()` - Display Borrowed Books

#### Purpose
Shows all books currently borrowed by the logged-in member with issue and due dates.

#### Clear Previous Data
```python
for row in borrowed_tree.get_children():
    borrowed_tree.delete(row)
```
- `get_children()` returns list of all rows in table
- Clears table before refreshing

#### Get Member ID
```python
conn = get_conn()
cur = conn.cursor()
cur.execute("SELECT member_id FROM members WHERE user_id=%s", (user_id,))
member = cur.fetchone()
```
- Looks up member_id from user_id
- **Why two IDs?**
  - `user_id` identifies login account in users table
  - `member_id` identifies member profile in members table
  - This allows separation between authentication and member data

#### Query Borrowed Books
```python
if member:
    cur.execute("SELECT book_id, title, author, year, issue_date FROM books WHERE issued_to_member_id=%s AND book_status='Issued'", (member[0],))
```
- Gets all books where `issued_to_member_id` matches this member
- Only books with status='Issued' (not Returned or New)
- Returns: book_id, title, author, year, issue_date

#### Calculate and Display Dates
```python
for book in cur.fetchall():
    issue_date_str = 'N/A'
    due_date_str = 'N/A'
    if book[4]:  # If issue_date exists
        issue_date_str = book[4].strftime('%d/%m/%Y')
        due_date = book[4] + timedelta(days=15)
        due_date_str = due_date.strftime('%d/%m/%Y')
```
- `book[4]` is the issue_date from database
- `strftime('%d/%m/%Y')` formats date as dd/mm/yyyy (Indian format)
- **Due Date Calculation**: Issue date + 15 days
- `timedelta(days=15)` creates a 15-day duration object

#### Insert into Table
```python
borrowed_tree.insert('', tk.END, values=(book[0], book[1], book[2], book[3], issue_date_str, due_date_str))
```
- `''` means insert at root level (no parent)
- `tk.END` adds to end of list
- `values=` tuple must match column order

#### Close Connection
```python
conn.close()
```
- Always close database connections when done
- Frees up database resources

---

### 2. `search_books()` - Search Available Books

#### Purpose
Allows members to search for books that are currently available (not issued).

#### Clear Previous Results
```python
for row in search_tree.get_children():
    search_tree.delete(row)
```

#### Get Search Term
```python
search_term = '%' + search_entry.get() + '%'
```
- Gets text from search entry field
- Adds `%` wildcards for SQL LIKE query
- Example: "Gandhi" becomes "%Gandhi%"
- Matches: "Autobiography of Gandhi", "Gandhi's Life", etc.

#### Query Available Books
```python
cur.execute("SELECT book_id, title, author, year FROM books WHERE (title LIKE %s OR author LIKE %s) AND book_status='Returned'",
            (search_term, search_term))
```
- **LIKE operator**: Pattern matching in SQL
- Searches both title AND author fields
- **Important**: Only shows books with status='Returned'
- This means available books (not currently issued)
- Note: 'New' books not shown (could be updated to include them)

#### Display Results
```python
for row in cur.fetchall():
    search_tree.insert('', tk.END, values=row)
```
- Loops through all matching books
- `values=row` inserts entire row tuple

---

## GUI Setup

### Main Window
```python
root = tk.Tk()
root.title("Library Management System - Member")
root.geometry("800x600")
root.resizable(False, False)
```
- Creates 800x600 pixel window
- Non-resizable for consistent layout

### Center Window on Screen
```python
root.update_idletasks()
x = (root.winfo_screenwidth() // 2) - 400
y = (root.winfo_screenheight() // 2) - 300
root.geometry(f'800x600+{x}+{y}')
```
- `update_idletasks()` processes pending GUI updates
- `winfo_screenwidth()` gets monitor width in pixels
- `//` is integer division (no decimals)
- Calculation: (screen width / 2) - (window width / 2) = centered position
- `+{x}+{y}` syntax sets window position from top-left corner

---

### Header Section
```python
header = tk.Frame(root, bg="#4CAF50", height=70)
header.pack(fill=tk.X)
tk.Label(header, text="Member Portal", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white").pack(pady=20)
tk.Button(header, text="Logout", font=("Arial", 10), command=root.destroy).place(x=700, y=20)
```
- **Color**: #4CAF50 = Material Design Green (different from admin's blue)
- `fill=tk.X` stretches frame horizontally
- `fg="white"` sets text color to white
- Logout button uses `.place()` for absolute positioning at (700, 20)
- `command=root.destroy` closes window

---

### Main Container
```python
main = tk.Frame(root, bg="#f5f5f5")
main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
```
- Light gray background (#f5f5f5)
- `fill=tk.BOTH` expands both horizontally and vertically
- `expand=True` allows frame to grow with window
- `padx=10, pady=10` adds 10-pixel padding on all sides

---

### My Borrowed Books Section

#### Frame Setup
```python
borrowed_frame = tk.Frame(main, bg="white", relief=tk.RAISED, bd=1)
borrowed_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 5))
```
- White background for clean look
- `relief=tk.RAISED` creates 3D raised border effect
- `bd=1` sets border width to 1 pixel
- `pady=(0, 5)` adds 0 padding on top, 5 pixels on bottom

#### Section Header
```python
tk.Label(borrowed_frame, text="My Borrowed Books", font=("Arial", 14, "bold"), bg="white").pack(pady=10)
```
- Bold 14pt font for section title

#### Table Setup
```python
cols = ('ID', 'Title', 'Author', 'Year', 'Issue Date', 'Due Date')
borrowed_tree = ttk.Treeview(borrowed_frame, columns=cols, show='headings', height=5)
widths = [50, 200, 150, 80, 100, 100]
```
- `Treeview` widget displays tabular data
- `columns=cols` defines 6 columns
- `show='headings'` hides default first column
- `height=5` shows 5 rows at a time (with scrollbar if more)
- Different widths for different columns

#### Configure Columns
```python
for i, col in enumerate(cols):
    borrowed_tree.heading(col, text=col)
    borrowed_tree.column(col, width=widths[i])
```
- `enumerate()` gives both index (i) and value (col)
- `heading()` sets column header text
- `column()` configures column properties
- `widths[i]` gets corresponding width from list

---

### Search Books Section

#### Frame Setup
```python
search_frame = tk.Frame(main, bg="white", relief=tk.RAISED, bd=1)
search_frame.pack(fill=tk.BOTH, expand=True)
```
- Similar styling to borrowed books section

#### Section Header
```python
tk.Label(search_frame, text="Search Available Books", font=("Arial", 14, "bold"), bg="white").pack(pady=10)
```

#### Search Bar
```python
search_bar = tk.Frame(search_frame, bg="white")
search_bar.pack()
tk.Label(search_bar, text="Search:", bg="white").pack(side=tk.LEFT, padx=5)
search_entry = tk.Entry(search_bar, font=("Arial", 11), width=35)
search_entry.pack(side=tk.LEFT, padx=5)
tk.Button(search_bar, text="Search", command=search_books).pack(side=tk.LEFT, padx=5)
```
- Nested frame for horizontal layout
- `side=tk.LEFT` arranges widgets left-to-right
- Label → Entry → Button layout
- `command=search_books` calls function when button clicked

#### Search Results Table
```python
search_tree = ttk.Treeview(search_frame, columns=cols, show='headings', height=8)
for col in cols:
    search_tree.heading(col, text=col)
    search_tree.column(col, width=180)
```
- Uses same columns as borrowed books table
- `height=8` shows more rows (8 vs 5)
- All columns have uniform 180px width

#### Instructional Text
```python
tk.Label(search_frame, text="Contact admin to issue books", font=("Arial", 10), bg="white", fg="#666").pack(pady=10)
```
- Gray text (#666) for secondary information
- Informs users they cannot self-issue books

---

### Initial Data Load
```python
refresh_borrowed()
search_books()
```
- Calls both functions when window first opens
- Shows borrowed books immediately
- Shows all available books (empty search = show all)

### Start Event Loop
```python
root.mainloop()
```
- Starts tkinter event loop
- Keeps window open and responsive

---

## CBSE Class XII Concepts Demonstrated

1. **Functions**: Defining and calling functions
2. **Database Connectivity**: MySQL queries with parameterized statements
3. **GUI Programming**: Tkinter frames, labels, buttons, entry widgets
4. **Treeview Widget**: Displaying tabular data
5. **Date Operations**: timedelta for date arithmetic
6. **String Formatting**: strftime() for date formatting
7. **String Operations**: Concatenation with + operator
8. **Loops**: for loops to iterate through database results
9. **Conditional Statements**: if statements for data validation
10. **Command-line Arguments**: sys.argv for receiving user_id
11. **Wildcard Search**: SQL LIKE operator with %
12. **Layout Management**: pack() with various options

---

## Database Tables Used

1. **users**: user_id (received from command line)
2. **members**: member_id, user_id, name
3. **books**: book_id, title, author, year, book_status, issued_to_member_id, issue_date

---

## Key Features

- ✅ View currently borrowed books
- ✅ Display issue date and due date (15 days)
- ✅ Date formatting in dd/mm/yyyy format
- ✅ Search available books by title or author
- ✅ Read-only interface (cannot issue/return)
- ✅ Clean two-section layout
- ✅ Green color scheme (different from admin)
- ✅ Auto-refresh on startup

---

## Design Decisions

### Why Read-Only?
- **Security**: Members cannot manipulate book records
- **Accountability**: All transactions tracked through admin
- **Workflow**: Admin verifies book condition before issue/return

### Why Two Tables?
The search shows only books with status='Returned', which might seem limiting. This is because:
1. 'New' books might need admin processing first
2. 'Issued' books are already borrowed
3. Simple query keeps code CBSE-friendly

**Possible Enhancement**: Could change query to:
```python
AND book_status IN ('Returned', 'New')
```
This would show both returned and newly added books.

---

## Flow Diagram

```
Member Login (from login.py)
  ↓
member.py receives user_id
  ↓
Create window with two sections
  ↓
Section 1: My Borrowed Books
  - Query books issued to this member
  - Calculate due dates
  - Display in table
  ↓
Section 2: Search Available Books
  - Show search bar
  - Query available books
  - Display results
  ↓
Wait for user actions:
  - Type in search box → Click Search → Update results
  - Click Logout → Close window
```

---

## Comparison with admin.py

| Feature | admin.py | member.py |
|---------|----------|-----------|
| Color Scheme | Blue (#2196F3) | Green (#4CAF50) |
| Can Issue Books | ✅ Yes | ❌ No |
| Can Return Books | ✅ Yes | ❌ No |
| Can Add Books | ✅ Yes | ❌ No |
| Can Delete Books | ✅ Yes | ❌ No |
| View Borrowed Books | ✅ All members | ✅ Own books only |
| Search Catalog | ✅ All books | ✅ Available only |
| Weekly Reports | ✅ Yes | ❌ No |
| Lines of Code | ~280 | ~102 |

---

## User Experience

**Member logs in → Sees:**
1. Top section showing their borrowed books with due dates
2. Bottom section to search available books
3. Simple, clean interface without overwhelming options
4. Clear message: "Contact admin to issue books"

**Workflow:**
1. Member searches for desired book
2. Finds book in available books list
3. Contacts admin (in person or via library desk)
4. Admin issues book using admin.py
5. Book appears in member's "My Borrowed Books" section
6. Member can track due date
