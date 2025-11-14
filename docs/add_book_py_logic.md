# add_book.py - Python Logic Explanation

**File**: `add_book.py`
**Purpose**: Form for adding new books to the library catalog with multiple copies support

---

## Overview

This file provides a form interface for adding books to the library. It supports adding multiple copies of the same book and logs each addition in the transactions table. Launched from admin.py using subprocess.

---

## Import Statements

```python
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from config import db_config
```

- **tkinter**: For creating the form GUI
- **messagebox**: For showing success/error popups
- **mysql.connector**: To insert data into MySQL database
- **config**: Database credentials from config.py

---

## Main Functions

### 1. `save()` - Save New Book(s)

#### Get Input Values
```python
title = title_entry.get().strip()
author = author_entry.get().strip()
isbn = isbn_entry.get().strip()
year = year_entry.get().strip()
copies = copies_entry.get().strip()
```
- Retrieves text from all 5 input fields
- `.strip()` removes whitespace

#### Validate All Fields
```python
if not all([title, author, isbn, year, copies]):
    messagebox.showerror("Error", "All fields are required!")
    return
```
- `all()` function returns True only if all items are non-empty
- More concise than: `if not title or not author or ...`
- All fields are mandatory for books

#### Validate Numbers
```python
try:
    year = int(year)
    copies = int(copies)
    if copies < 1:
        messagebox.showerror("Error", "Number of copies must be at least 1")
        return
except ValueError:
    messagebox.showerror("Error", "Year and copies must be valid numbers")
    return
```
- **Type Conversion**: `int()` converts string to integer
- **ValueError**: Raised if string can't be converted (e.g., "abc")
- **Validation**: At least 1 copy must be added
- Example:
  - `int("2020")` → 2020 ✓
  - `int("abc")` → ValueError ✗

---

#### Loop to Insert Multiple Copies
```python
try:
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor()

    for i in range(1, copies + 1):
        cur.execute("INSERT INTO books (title, author, isbn, year, copy_number, book_status, record_status) VALUES (%s, %s, %s, %s, %s, 'New', 'Active')",
                   (title, author, isbn, year, i))
        book_id = cur.lastrowid
```

**Understanding the Loop:**
- `range(1, copies + 1)` generates sequence: 1, 2, 3, ..., copies
- Example: If copies = 3, range produces 1, 2, 3
- Each iteration creates one copy with different `copy_number`

**Fixed Values:**
- `book_status='New'`: Indicates newly added book (not yet issued or returned)
- `record_status='Active'`: Book is active (not deleted)

**Auto-generated ID:**
- `book_id = cur.lastrowid` gets the unique ID for this specific copy

---

#### Log Transaction for Each Copy
```python
cur.execute("INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes) VALUES (%s, NULL, NULL, 'Add', %s)",
           (book_id, f"{title} by {author} (Copy {i})"))
```
- Records addition in transactions table
- **member_id = NULL**: No member involved in adding books
- **admin_user_id = NULL**: Could be tracked if admin_id was passed
- **action = 'Add'**: Indicates book addition
- **notes**: Descriptive text with copy number

---

#### Commit and Show Success
```python
conn.commit()
conn.close()

messagebox.showinfo("Success", f"{copies} cop{'y' if copies == 1 else 'ies'} of '{title}' added successfully!")
reset()
```
- `commit()` saves all INSERT statements
- **Smart Pluralization**:
  - 1 copy → "1 copy"
  - 3 copies → "3 copies"
- Ternary operator: `'y' if copies == 1 else 'ies'`
- Calls `reset()` to clear form

---

#### Error Handling
```python
except Exception as e:
    messagebox.showerror("Error", f"Failed to add book:\n{e}")
```
- Catches database errors
- Common errors:
  - Database connection failure
  - Invalid ISBN format (if constraints exist)
  - Network issues

---

### 2. `reset()` - Clear Form Fields

```python
def reset():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    isbn_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    copies_entry.delete(0, tk.END)
```
- Clears all 5 input fields
- `delete(0, tk.END)` removes text from start (0) to end
- Prepares form for next book entry

---

## GUI Setup

### Main Window
```python
root = tk.Tk()
root.title("Add Book")
root.geometry("800x600")
root.resizable(False, False)
```
- 800x600 pixel window
- Fixed size (non-resizable)

### Centered Frame
```python
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")
```
- `place()` with relative positioning
- 50% from left, 50% from top = center
- `anchor="center"` centers frame at that point

---

### Form Fields (Grid Layout)

#### Book Title Field
```python
tk.Label(frame, text="Book Title:").grid(row=0, column=0, padx=5, pady=5)
title_entry = tk.Entry(frame)
title_entry.grid(row=0, column=1, padx=5, pady=5)
```
- Row 0, two columns (label and entry)
- `padx=5, pady=5` adds spacing

#### Author Field
```python
tk.Label(frame, text="Author:").grid(row=1, column=0, padx=5, pady=5)
author_entry = tk.Entry(frame)
author_entry.grid(row=1, column=1, padx=5, pady=5)
```

#### ISBN Number Field
```python
tk.Label(frame, text="ISBN Number:").grid(row=2, column=0, padx=5, pady=5)
isbn_entry = tk.Entry(frame)
isbn_entry.grid(row=2, column=1, padx=5, pady=5)
```
- ISBN: International Standard Book Number
- Example: 978-3-16-148410-0

#### Publication Year Field
```python
tk.Label(frame, text="Publication Year:").grid(row=3, column=0, padx=5, pady=5)
year_entry = tk.Entry(frame)
year_entry.grid(row=3, column=1, padx=5, pady=5)
```
- Example: 2020, 2019, etc.

#### Number of Copies Field
```python
tk.Label(frame, text="Number of Copies:").grid(row=4, column=0, padx=5, pady=5)
copies_entry = tk.Entry(frame)
copies_entry.grid(row=4, column=1, padx=5, pady=5)
```
- Allows adding multiple copies at once
- Example: 3 → creates Copy 1, Copy 2, Copy 3

---

### Buttons
```python
tk.Button(frame, text="Save", command=save).grid(row=5, column=0, pady=10)
tk.Button(frame, text="Reset", command=reset).grid(row=5, column=1, pady=10)
```
- Save button: Adds book(s) to database
- Reset button: Clears form

### Start Application
```python
root.mainloop()
```

---

## CBSE Class XII Concepts Demonstrated

1. **Loops**: for loop to create multiple copies
2. **Range Function**: Generating sequences
3. **Type Conversion**: int() for string to integer
4. **Exception Handling**: try-except for ValueError and database errors
5. **Data Validation**: Checking all fields and number validation
6. **String Formatting**: f-strings with embedded variables
7. **Conditional Expressions**: Ternary operator for pluralization
8. **Database INSERT**: Adding records to multiple tables
9. **Foreign Key Relationships**: book_id in transactions references books
10. **Transaction Logging**: Audit trail for all additions

---

## Database Tables Structure

### books table
```sql
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200),
    author VARCHAR(100),
    isbn VARCHAR(20),
    year INT,
    copy_number INT,
    book_status VARCHAR(20),
    record_status VARCHAR(20),
    issued_to_member_id INT,
    issue_date DATE
)
```

### transactions table
```sql
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    member_id INT,
    admin_user_id INT,
    action VARCHAR(20),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes VARCHAR(200),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
)
```

---

## Example Scenario

**Admin wants to add 3 copies of "The God of Small Things"**

### Input:
- Book Title: The God of Small Things
- Author: Arundhati Roy
- ISBN: 978-0-679-45731-0
- Publication Year: 1997
- Number of Copies: 3

### Database Result (books table):
| book_id | title | author | isbn | year | copy_number | book_status | record_status |
|---------|-------|--------|------|------|-------------|-------------|---------------|
| 101 | The God of Small Things | Arundhati Roy | 978-0-679-45731-0 | 1997 | 1 | New | Active |
| 102 | The God of Small Things | Arundhati Roy | 978-0-679-45731-0 | 1997 | 2 | New | Active |
| 103 | The God of Small Things | Arundhati Roy | 978-0-679-45731-0 | 1997 | 3 | New | Active |

### Database Result (transactions table):
| transaction_id | book_id | action | notes |
|----------------|---------|--------|-------|
| 500 | 101 | Add | The God of Small Things by Arundhati Roy (Copy 1) |
| 501 | 102 | Add | The God of Small Things by Arundhati Roy (Copy 2) |
| 502 | 103 | Add | The God of Small Things by Arundhati Roy (Copy 3) |

### Success Message:
"3 copies of 'The God of Small Things' added successfully!"

---

## Multiple Copies Logic

### Why Multiple Copies?

**Scenario**: Library has 5 copies of popular book "Five Point Someone"

**Without copy tracking:**
- Can't track which physical copy is with which member
- Can't manage individual book conditions
- No way to know if a specific copy is damaged

**With copy_number:**
- Copy 1 → Issued to Rahul
- Copy 2 → Issued to Priya
- Copy 3 → Available (New)
- Copy 4 → Available (Returned)
- Copy 5 → Deleted (Damaged)

### How It Works

```python
for i in range(1, copies + 1):
```

**If copies = 4:**
- Iteration 1: i = 1 → Copy 1 created
- Iteration 2: i = 2 → Copy 2 created
- Iteration 3: i = 3 → Copy 3 created
- Iteration 4: i = 4 → Copy 4 created

Each copy has:
- **Same**: title, author, isbn, year
- **Different**: book_id, copy_number

---

## Data Flow Diagram

```
Admin clicks "Add Book" in admin.py
  ↓
add_book.py opens
  ↓
Admin fills form:
  - Title
  - Author
  - ISBN
  - Year
  - Number of Copies
  ↓
Click Save button
  ↓
Validate all fields filled
  ↓
Convert year and copies to integers
  ↓
Validate copies >= 1
  ↓
Connect to database
  ↓
For each copy (1 to N):
  - INSERT into books table
  - Get book_id
  - INSERT into transactions table
  ↓
Commit all changes
  ↓
Show success message
  ↓
Clear form (ready for next book)
```

---

## Common Errors and Solutions

### Error 1: "Year and copies must be valid numbers"
**Cause**: Entering "abc" in year or copies field
**Solution**: Enter numeric values only (e.g., 2020, 3)

### Error 2: "All fields are required!"
**Cause**: One or more fields left empty
**Solution**: Fill in all 5 fields

### Error 3: "Number of copies must be at least 1"
**Cause**: Entering 0 or negative number
**Solution**: Enter 1 or more

### Error 4: Data type mismatch
**Cause**: Year field expects integer
**Solution**: Validation handles this with try-except

---

## Grid Layout Visualization

```
           Column 0              Column 1
Row 0  |  Book Title:       |  [entry box]     |
Row 1  |  Author:           |  [entry box]     |
Row 2  |  ISBN Number:      |  [entry box]     |
Row 3  |  Publication Year: |  [entry box]     |
Row 4  |  Number of Copies: |  [entry box]     |
Row 5  |  [Save button]     |  [Reset button]  |
```

---

## ISBN Format

**What is ISBN?**
- International Standard Book Number
- Unique identifier for books
- Two formats:
  - ISBN-10: 10 digits (older)
  - ISBN-13: 13 digits (current)

**Example ISBN-13**: 978-0-679-45731-0
- 978: Prefix (indicates ISBN-13)
- 0: Group identifier (English language)
- 679: Publisher code
- 45731: Title code
- 0: Check digit

**Note**: This system accepts any string (no validation)

---

## Book Status Values

### book_status field:
- **'New'**: Just added, never issued
- **'Issued'**: Currently borrowed by member
- **'Returned'**: Was issued, now returned and available

### record_status field:
- **'Active'**: Book is in circulation
- **'Deleted'**: Soft-deleted (damaged, lost, etc.)

---

## Integration with System

### Called From: admin.py
```python
def add_book():
    subprocess.Popen([sys.executable, 'add_book.py'])
```

### Opens: New independent window

### User Action: Admin clicks "Add Book" button

### Result:
1. Books appear in catalog (admin search)
2. Books appear in member search (if status = 'Returned' or 'New')
3. Transactions logged for audit trail

---

## Possible Enhancements (Not Implemented)

**For CBSE Project Extensions:**

1. **ISBN Validation**: Check 13-digit format
2. **Year Validation**: Ensure year <= current year
3. **Duplicate Check**: Warn if book already exists
4. **Cover Image Upload**: Add book cover
5. **Category/Genre**: Classify books
6. **Language Field**: Track book languages
7. **Price Field**: Track book value
8. **Barcode Generation**: For physical copies

---

## Comparison with add_member.py

| Feature | add_book.py | add_member.py |
|---------|-------------|---------------|
| Tables Used | 1 (books) | 2 (users + members) |
| Multiple Entries | Yes (copies) | No (one member) |
| Loop Required | Yes | No |
| Transaction Log | Yes | No |
| Auto-increment ID | book_id | user_id, member_id |
| Number Validation | Yes (year, copies) | No |
| All Fields Required | Yes | No (3 required, 3 optional) |

---

## Key Takeaway

This file demonstrates a **one-to-many relationship**: one book title can have many physical copies. This is handled by inserting multiple rows with the same title/author/ISBN but different copy_number and book_id values.
