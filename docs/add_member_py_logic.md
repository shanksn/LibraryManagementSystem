# add_member.py - Python Logic Explanation

**File**: `add_member.py`
**Purpose**: Form for adding new library members to the system

---

## Overview

This file provides a simple form interface for adding new members. It creates accounts in both the `users` table (for login) and `members` table (for member details). Launched from admin.py using subprocess.

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

### 1. `save()` - Save New Member

#### Get Input Values
```python
username = username_entry.get().strip()
password = password_entry.get().strip()
name = name_entry.get().strip()
address = address_entry.get().strip()
email = email_entry.get().strip()
phone = phone_entry.get().strip()
```
- `.get()` retrieves text from Entry widgets
- `.strip()` removes leading/trailing whitespace
- Prevents issues like "john " vs "john"

#### Validate Required Fields
```python
if not username or not password or not name:
    messagebox.showerror("Error", "Username, Password and Name are required")
    return
```
- **Required fields**: Username, Password, Full Name
- **Optional fields**: Address, Email, Phone
- `not username` is True if username is empty string
- `return` exits function without saving

#### Database Operations (Try-Except Block)
```python
try:
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor()
```
- `try-except` handles potential errors
- Common errors: database offline, duplicate username, network issues

#### Insert into Users Table
```python
cur.execute("INSERT INTO users (username, password, full_name, user_type, status) VALUES (%s, %s, %s, 'member', 'active')",
           (username, password, name))
user_id = cur.lastrowid
```
- Creates login account in users table
- **Fixed values**:
  - `user_type='member'` (not admin)
  - `status='active'` (account enabled)
- `cur.lastrowid` gets the auto-generated user_id
- **Important**: This ID links to members table

#### Insert into Members Table
```python
cur.execute("INSERT INTO members (user_id, name, address, email, phone) VALUES (%s, %s, %s, %s, %s)",
           (user_id, name, address, email, phone))
member_id = cur.lastrowid
```
- Creates member profile with contact details
- Uses `user_id` from previous insert (foreign key)
- Gets auto-generated `member_id`

#### Commit Changes
```python
conn.commit()
conn.close()
```
- `commit()` permanently saves changes to database
- Without commit, changes are rolled back
- `close()` frees database connection

#### Show Success Message
```python
messagebox.showinfo("Success", f"Member added successfully!\nMember ID: {member_id}")
reset()
```
- f-string embeds member_id in message
- `\n` creates new line
- Calls `reset()` to clear form for next entry

#### Error Handling
```python
except Exception as e:
    messagebox.showerror("Error", f"Failed to add member:\n{e}")
```
- Catches any error during database operations
- `e` contains error message
- Example errors:
  - "Duplicate entry 'john' for key 'username'"
  - "Can't connect to MySQL server"

---

### 2. `reset()` - Clear Form Fields

```python
def reset():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
```
- `delete(0, tk.END)` removes text from position 0 to end
- Clears all six input fields
- Prepares form for entering next member

---

## GUI Setup

### Main Window
```python
root = tk.Tk()
root.title("Add Member")
root.geometry("800x600")
root.resizable(False, False)
```
- 800x600 pixel window
- Non-resizable for consistent form layout

### Centered Frame
```python
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")
```
- Creates frame to hold form
- `relx=0.5, rely=0.5` places at 50% horizontal, 50% vertical
- `anchor="center"` centers the frame at that position
- **Result**: Form appears in center of window

---

### Form Fields (Grid Layout)

#### Username Field
```python
tk.Label(frame, text="Username:").grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)
```
- `.grid()` arranges widgets in table format
- `row=0, column=0` → Label in first row, first column
- `row=0, column=1` → Entry in first row, second column
- `padx=5, pady=5` adds 5-pixel spacing

#### Password Field
```python
tk.Label(frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)
```
- `show="*"` hides password characters
- Displays asterisks instead of actual text

#### Full Name Field
```python
tk.Label(frame, text="Full Name:").grid(row=2, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=2, column=1, padx=5, pady=5)
```

#### Address Field
```python
tk.Label(frame, text="Address:").grid(row=3, column=0, padx=5, pady=5)
address_entry = tk.Entry(frame)
address_entry.grid(row=3, column=1, padx=5, pady=5)
```

#### Email Field
```python
tk.Label(frame, text="Email:").grid(row=4, column=0, padx=5, pady=5)
email_entry = tk.Entry(frame)
email_entry.grid(row=4, column=1, padx=5, pady=5)
```

#### Phone Field
```python
tk.Label(frame, text="Phone:").grid(row=5, column=0, padx=5, pady=5)
phone_entry = tk.Entry(frame)
phone_entry.grid(row=5, column=1, padx=5, pady=5)
```

---

### Buttons
```python
tk.Button(frame, text="Save", command=save).grid(row=6, column=0, pady=10)
tk.Button(frame, text="Reset", command=reset).grid(row=6, column=1, pady=10)
```
- Both buttons in row 6
- Save button in column 0 (left)
- Reset button in column 1 (right)
- `command=save` connects button to function

---

### Start Application
```python
root.mainloop()
```
- Starts event loop
- Keeps window open until closed

---

## CBSE Class XII Concepts Demonstrated

1. **Functions**: Defining save() and reset() functions
2. **Database INSERT Operations**: Adding records to multiple tables
3. **Foreign Keys**: user_id links users and members tables
4. **Data Validation**: Checking required fields
5. **Exception Handling**: try-except for database errors
6. **String Methods**: .strip() for cleaning input
7. **GUI Forms**: Grid layout for organized input
8. **Event Handling**: Button commands
9. **Auto-increment IDs**: lastrowid property
10. **Transaction Management**: commit() for saving changes

---

## Database Tables Structure

### users table
```sql
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50),
    full_name VARCHAR(100),
    user_type VARCHAR(20),
    status VARCHAR(20)
)
```

### members table
```sql
CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(100),
    address VARCHAR(200),
    email VARCHAR(100),
    phone VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
```

---

## Data Flow

```
User fills form
  ↓
Clicks Save button
  ↓
save() function called
  ↓
Validate required fields
  ↓ (valid)
Connect to database
  ↓
INSERT into users table
  ↓
Get user_id
  ↓
INSERT into members table (with user_id)
  ↓
Get member_id
  ↓
Commit changes
  ↓
Show success message with member_id
  ↓
Clear form (reset)
  ↓
Ready for next entry
```

---

## Example Data

**Input:**
- Username: aisha
- Password: aisha123
- Full Name: Aisha Patel
- Address: 123 Main St, Mumbai
- Email: aisha@email.com
- Phone: 9876543210

**Result in users table:**
| user_id | username | password | full_name | user_type | status |
|---------|----------|----------|-----------|-----------|--------|
| 5 | aisha | aisha123 | Aisha Patel | member | active |

**Result in members table:**
| member_id | user_id | name | address | email | phone |
|-----------|---------|------|---------|-------|-------|
| 5 | 5 | Aisha Patel | 123 Main St, Mumbai | aisha@email.com | 9876543210 |

---

## Security Considerations

**⚠️ Educational Implementation:**
- Passwords stored in plain text (not secure)
- No password strength validation
- No email format validation
- No phone number format validation

**Production Requirements:**
- Hash passwords (bcrypt, SHA-256)
- Validate email format (regex)
- Validate phone format (10 digits)
- Prevent SQL injection (already done with parameterized queries ✓)
- Check for duplicate usernames before INSERT

---

## Common Errors and Solutions

### Error 1: "Duplicate entry 'john' for key 'username'"
**Cause**: Username already exists
**Solution**: Choose different username

### Error 2: "Data too long for column 'phone'"
**Cause**: Phone number exceeds VARCHAR length
**Solution**: Limit input length or increase column size

### Error 3: "Can't connect to MySQL server"
**Cause**: Database not running or wrong credentials
**Solution**: Check MySQL service and config.py

### Error 4: "Field 'password' doesn't have a default value"
**Cause**: Password field empty but validation failed to catch it
**Solution**: Validation logic prevents this (check required fields)

---

## Grid Layout Visualization

```
           Column 0          Column 1
Row 0  |  Username:     |  [entry box]  |
Row 1  |  Password:     |  [******]     |
Row 2  |  Full Name:    |  [entry box]  |
Row 3  |  Address:      |  [entry box]  |
Row 4  |  Email:        |  [entry box]  |
Row 5  |  Phone:        |  [entry box]  |
Row 6  |  [Save btn]    |  [Reset btn]  |
```

---

## Why Two Tables?

**Design Pattern: Separation of Concerns**

**users table** = Authentication data
- Who can log in?
- What's their password?
- What type of user? (admin/member)
- Is account active?

**members table** = Profile data
- Contact information
- Personal details
- Library-specific information

**Benefits:**
1. Can have users who aren't members (future admins)
2. Can deactivate account without losing member history
3. Cleaner data organization
4. Follows database normalization principles

---

## Integration with System

**Called From:** admin.py
```python
def add_user():
    subprocess.Popen([sys.executable, 'add_member.py'])
```

**Opens:** New window (independent process)

**User Action:** Admin clicks "Add Member" button

**Result:** New member can log in with created username/password
