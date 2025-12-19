# Library Management System
## User Manual

**Class XII Computer Science Project**
**Academic Year**: 2024-2025
**Student**: Jhanvi Shankar
**Roll No**: ASLSKLDK

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Getting Started](#2-getting-started)
3. [Login Process](#3-login-process)
4. [Administrator Guide](#4-administrator-guide)
5. [Member Guide](#5-member-guide)
6. [Troubleshooting](#6-troubleshooting)
7. [Appendix](#7-appendix)

---

## 1. Introduction

### 1.1 Purpose
This Library Management System efficiently manages library operations including book cataloging, member management, book issuing, and returns with an intuitive graphical interface featuring decorative icons for better user experience.

### 1.2 Key Features

**For Administrators:**
- Add new users (Admin or Member type) with validation
- Add books to catalog (1-5 copies at a time)
- View all users with contact information
- Search and browse book catalog with filters
- Issue books to members (max 3 books per member)
- **Prevent issuing to defaulters** - Members with overdue books cannot borrow
- Process book returns
- Soft delete books with validation
- View defaulters list with overdue details
- Visual dashboard with decorative icons (6 buttons in 3x2 grid)

**For Members:**
- View borrowed books with due dates
- **Visual overdue indicator** - Overdue books highlighted in red
- Search available books
- Clean interface with icon-enhanced navigation

### 1.3 Technology Stack
- **Programming Language**: Python 3.7+
- **GUI Framework**: Tkinter
- **Database**: MySQL 8.0
- **Libraries**: mysql-connector-python, Pillow (PIL)
- **UI Enhancement**: Decorative PNG icons (40x40 and 50x50 pixels)

### 1.4 System Architecture

```
Login Screen (login.py) → Role-based Authentication
    ↓
    ├── Admin Dashboard (admin.py) - 6 icon-enhanced buttons
    │   ├── Add User (add_member.py) - Create Admin/Member
    │   ├── Add Book (add_book.py)
    │   ├── View Users - List all users
    │   ├── Search Catalog - Issue/Return/Delete
    │   ├── Weekly Reports - Last 7 days transactions
    │   └── Defaulters List - Overdue books report
    │
    └── Member Dashboard (member.py) with icon-enhanced header
        ├── My Borrowed Books (red highlight for overdue)
        └── Search Books (read-only)
```

---

## 2. Getting Started

### 2.1 System Requirements
- Python 3.7 or higher
- MySQL 8.0 or higher
- 800x600 screen resolution minimum
- 100 MB free disk space

### 2.2 Installation

**Step 1**: Install Python dependencies
```bash
pip install -r requirements.txt
```

**Step 2**: Configure database
```bash
cp config_template.py config.py
# Edit config.py with your MySQL password
```

**Step 3**: Setup database
```bash
python3 setup_database_final.py
```

**Step 4**: Launch application
```bash
python3 login.py
```

### 2.3 Default Login Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | admin123 |
| Admin | librarian | lib123 |
| Member | priya | priya123 |
| Member | rahul | rahul123 |

---

## 3. Login Process

### 3.1 Accessing the System

[SCREENSHOT: Login screen with library background image, username/password fields, and login button]

**Steps:**
1. Run `python3 login.py`
2. Enter username and password
3. Click "Login" or press Enter
4. System validates credentials and redirects based on role

**Validation:**
- Valid credentials → Redirects to appropriate dashboard
- Invalid credentials → Error: "Invalid username or password"
- Inactive account → Error: "Account is inactive"

---

## 4. Administrator Guide

### 4.1 Admin Dashboard Overview

[SCREENSHOT: Admin Dashboard showing 6 buttons in 3x2 grid - admin portal icon (40x40) next to heading, and icons (50x50) above each button]

The Admin Dashboard features an icon-enhanced interface with 6 buttons:
- **Admin Portal Icon** (40x40 pixels) next to "Admin Dashboard" heading
- **Button Icons** (50x50 pixels) displayed above each button for visual clarity
- **Logout button** in the top-right corner
- **3x2 Grid Layout**: Row 1: Add User, Add Book, View Users | Row 2: Search Catalog, Weekly Reports, Defaulters List

**Icon-Enhanced Buttons:**

| Button Icon | Button Name | Function |
|-------------|-------------|----------|
| Add Member icon | Add User | Create new Admin or Member account |
| Add Books icon | Add Book | Add books to catalog |
| View Users icon | View Users | Display all system users |
| Search Catalog icon | Search Catalog | Browse, issue, return, delete books |
| Weekly Report icon | Weekly Reports | View last 7 days transactions |
| Defaulters List icon | Defaulters List | View members with overdue books |

---

### 4.2 Adding a New User (Admin or Member)

[SCREENSHOT: Add User form with right-aligned labels and User Type dropdown]

**Step 1**: Click "Add User" button on Admin Dashboard
**Step 2**: Fill in the form fields (note: labels are right-aligned for professional appearance)

| Field | Required | Validation | Default |
|-------|----------|------------|---------|
| Username | Yes | Must be unique | - |
| Password | Yes | Min 1 character | - |
| Full Name | Yes | Any text | - |
| User Type | Auto | Member or Admin | Member |
| Address | No | Optional | - |
| Email | No | Optional | - |
| Phone | No | Optional | - |

**User Type Options:**
- **Member**: Creates user account + member profile (with contact info)
- **Admin**: Creates admin user account only (no member profile)

**Step 3**: Click centered "Save" button

[SCREENSHOT: Success message for Member - "Member added successfully! Member ID: 6"]
[SCREENSHOT: Success message for Admin - "Admin user 'librarian2' added successfully!"]

**Common Errors:**
- Empty required fields → "Username, Password and Full Name are required fields"
- Duplicate username → "Username 'xxx' already exists! Please choose a different username."

---

### 4.3 Adding a New Book

[SCREENSHOT: Add Book form with right-aligned labels and centered buttons]

**Step 1**: Click "Add Book" button on Admin Dashboard
**Step 2**: Fill in all required fields (note: labels are right-aligned for professional appearance)

| Field | Required | Validation |
|-------|----------|------------|
| Book Title | Yes | Must be unique per author |
| Author | Yes | Any text |
| ISBN Number | Yes | Any format |
| Publication Year | Yes | Must be integer |
| Number of Copies | Yes | 1-5 (inclusive) |

**Step 3**: Click "Save"

[SCREENSHOT: Success message "3 copies of 'The God of Small Things' added successfully!"]

**How Multiple Copies Work:**
When you add a book with 3 copies:
- 3 separate database entries are created
- Each copy gets a copy number: 1, 2, 3
- All copies start with status "New"
- Each can be issued/returned independently

**Common Errors:**
- Empty fields → "All fields are required!"
- Invalid number → "Year and copies must be valid numbers"
- Copies < 1 → "Number of copies must be at least 1"
- Copies > 5 → "Number of copies cannot be more than 5"
- Duplicate book → "Book 'xxx' by yyy already exists in the library!"

---

### 4.4 Searching and Managing Books

[SCREENSHOT: Book catalog showing table with columns: Title, Author, ISBN, Year, Total Copies, Available, Issued To, Issue Date, Due Date]

**Catalog Features:**
- **Search bar**: Search by title, author, or ISBN
- **Filter dropdown**: Active / Deleted / All
- **Double-click rows**: View all copies of a book
- **Action buttons**: Issue Book, Return Book, Delete Book

**Column Descriptions:**

| Column | Description |
|--------|-------------|
| Title | Book title |
| Author | Book author |
| ISBN | ISBN number |
| Year | Publication year |
| Total Copies | Total number of copies |
| Available | Copies available to borrow |
| Issued To | Member username (or "Multiple") |
| Issue Date | Date issued (dd/mm/yyyy) |
| Due Date | Return due date (15 days from issue) |

---

### 4.5 Issuing a Book

[SCREENSHOT: Issue book dialog asking for member username]

**Steps:**
1. Select a book with Available > 0
2. Click "Issue Book"
3. Enter member username (e.g., "rahul")
4. Click OK

[SCREENSHOT: Success message "Book issued successfully to rahul! Due date: 30/11/2024"]

**Validation:**
- Empty username → "Please enter a member username"
- Invalid username → "Member 'xxx' not found"
- No copies available → "No copies of this book are available for issue"

**What Happens:**
- First available copy status changes to "Issued"
- Member ID and current date recorded
- Due date calculated (current date + 15 days)
- Transaction logged

---

### 4.6 Returning a Book

[SCREENSHOT: All copies window showing one issued copy selected, with "Return Selected Copy" button]

**Steps:**
1. From catalog, double-click the issued book
2. Select the issued copy (Status = "Issued")
3. Click "Return Selected Copy"
4. Confirm "Yes" in the dialog

[SCREENSHOT: Success message "Book returned successfully!"]

**What Happens:**
- Copy status changes from "Issued" to "Returned"
- Member ID, issue date, and due date cleared
- Available count increases by 1
- Transaction logged

---

### 4.7 Deleting a Book

[SCREENSHOT: Delete confirmation dialog "Are you sure you want to delete: Train to Pakistan by Khushwant Singh?"]

**Steps:**
1. Select book to delete
2. Click "Delete Book"
3. Confirm "Yes"

**Soft Delete Behavior:**
- Book marked as "Deleted" (not permanently removed)
- Disappears from Active view
- Visible in Deleted filter
- All copies marked deleted
- Maintains audit trail

**Delete Validation (NEW):**
- **Cannot delete already deleted books** - System checks and shows error: "Cannot delete '[Book Title]' by [Author]. This book is already deleted."

[SCREENSHOT: Error message when trying to delete an already deleted book]

---

### 4.8 Viewing All Users

[SCREENSHOT: View Users window showing table with Username, User Type, Date Added, Email, Phone columns]

**Step 1**: Click "View Users" button on Admin Dashboard
**Step 2**: Browse the complete user list

**Information Displayed:**
| Column | Description |
|--------|-------------|
| Username | User's login username |
| User Type | Admin or Member |
| Date Added | Account creation date/time (dd/mm/yyyy HH:MM) |
| Email | Email address (or 'N/A') |
| Phone | Phone number (or 'N/A') |

**Features:**
- Shows ALL users (both Admin and Member types)
- Sorted by creation date (newest first)
- Includes contact information
- Window size: 900x500 pixels

---

### 4.9 Viewing Defaulters List

[SCREENSHOT: Defaulters List window showing overdue books with member details]

**Step 1**: Click "Defaulters List" button on Admin Dashboard
**Step 2**: Review members with overdue books

**Information Displayed:**
| Column | Description |
|--------|-------------|
| Member Name | Full name of member |
| Email | Email address (or 'N/A') |
| Phone | Phone number (or 'N/A') |
| Book Title | Title of overdue book |
| Author | Book author |
| Due Date | Date book was due (dd/mm/yyyy) |
| Days Overdue | Number of days past due date |

**Features:**
- Shows only members with overdue books (past 15-day due date)
- Automatically calculates days overdue
- Useful for follow-up and fines
- Shows "No overdue books found!" if list is empty

---

### 4.10 Issuing Books - Overdue Prevention (NEW)

**Important**: The system now prevents issuing books to members with overdue books.

**Validation Order:**
1. **First Check**: Does member have overdue books? (PRIORITY)
2. **Second Check**: Has member reached borrowing limit (3 books)?

[SCREENSHOT: Error message showing overdue books preventing new issue]

**Error Message Example:**
```
Cannot issue book to 'rahul'.

Member has overdue books:
Train to Pakistan by Khushwant Singh (5 days overdue)
The God of Small Things by Arundhati Roy (3 days overdue)

Please return overdue books first.
```

**Why This Matters:**
- Encourages timely returns
- Protects library inventory
- Fair access for all members
- Reduces loss and damage

---

## 5. Member Guide

### 5.1 Member Dashboard Overview

[SCREENSHOT: Member Dashboard showing decorative member portal icon (40x40) next to "Member Portal" heading in green header]

The Member Dashboard features:
- **Member Portal Icon** (40x40 pixels) next to "Member Portal" heading
- **Green header** with logout button
- **Simple interface** with two main functions

**Available Functions:**

| Section | Function |
|---------|----------|
| My Borrowed Books | View currently issued books with due dates |
| Search Available Books | Browse catalog (read-only) |

---

### 5.2 Viewing Borrowed Books with Overdue Indicator (NEW)

[SCREENSHOT: My Borrowed Books window showing mix of normal and red-highlighted overdue books]

**Features:**
- See all books you have borrowed
- Check issue dates and due dates
- Due dates are 15 days from issue date
- Format: dd/mm/yyyy
- **NEW: Overdue books highlighted in red background**
- **NEW: Warning legend appears when overdue books exist**

[SCREENSHOT: Warning legend - "⚠ Red highlighted books are overdue. Please contact admin."]

**Visual Indicators:**
- **Normal books**: White/default background
- **Overdue books**: Light red background (#ffcccc)
- **Legend**: Only appears when you have overdue books

**Example:**
- Issue Date: 15/11/2024
- Due Date: 30/11/2024
- If today is 05/12/2024 → Book highlighted in RED (5 days overdue)

**Important Notes:**
- Return overdue books as soon as possible
- Cannot borrow new books while you have overdue books
- Contact admin/librarian for assistance

---

### 5.3 Searching Available Books

[SCREENSHOT: Member catalog showing Title, Author, Year, Available Copies columns]

**Features:**
- Search by title, author, or year
- See number of available copies
- Read-only view (cannot issue/return)
- Shows only books with available copies

**To Borrow a Book:**
1. Note the book details
2. Contact admin/librarian
3. Admin will issue from their dashboard

---

## 6. Troubleshooting

### 6.1 Common Issues

**Issue: Login Failed**
- Error: "Invalid username or password"
- Solution: Check Caps Lock, verify credentials, remove spaces

**Issue: Cannot Add Member - Duplicate Username**
- Error: "Username 'xxx' already exists!"
- Solution: Choose different username (e.g., add numbers: john_2024)

**Issue: Cannot Add Book - Duplicate**
- Error: "Book 'xxx' by yyy already exists!"
- Solution: Search catalog first, check for typos in title/author

**Issue: Copies Validation Error**
- Error: "Number of copies cannot be more than 5"
- Solution: Enter value between 1-5, add in batches if needed

**Issue: Cannot Issue Book**
- Error: "No copies of this book are available for issue"
- Solution: Wait for returns, check due dates, add more copies

**Issue: Database Connection Error**
- Error: "Failed to connect to database"
- Solution:
  ```bash
  # Start MySQL server
  mysql.server start  # macOS
  # Verify config.py password
  # Run setup script
  python3 setup_database_final.py
  ```

**Issue: Icons Not Displaying**
- Check that `images/` folder exists in application directory
- Verify icon files: admin_portal.png, member_portal.png, add_member.png, add_books.png, search_catalog.png, weekly_report.png, view_users.png, defaulters_list.png
- Icon sizes: 40x40 for headings, 50x50 for buttons
- Application will continue without icons if files missing (graceful fallback)

**Issue: Cannot Issue Book - Member Has Overdue Books**
- Error: "Cannot issue book to '[username]'. Member has overdue books..."
- Solution: Member must return all overdue books before borrowing new ones
- This is by design to encourage timely returns

**Issue: Background Image Not Loading**
- Verify library.jpeg exists in application folder
- Check file name spelling (case-sensitive)
- Try replacing the image file

---

## 7. Appendix

### 7.1 Database Schema

**Table: users**
```sql
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    user_type VARCHAR(20) NOT NULL,
    status VARCHAR(20) DEFAULT 'active',
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Table: members**
```sql
CREATE TABLE members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(200),
    email VARCHAR(100),
    phone VARCHAR(15),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

**Table: books**
```sql
CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) NOT NULL,
    year INT NOT NULL,
    copy_number INT NOT NULL,
    book_status VARCHAR(20) DEFAULT 'New',
    record_status VARCHAR(20) DEFAULT 'Active',
    issued_to_member_id INT,
    issue_date DATE,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (issued_to_member_id) REFERENCES members(member_id)
);
```

**Table: transactions**
```sql
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    member_id INT,
    admin_user_id INT,
    action VARCHAR(20) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes VARCHAR(200),
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (admin_user_id) REFERENCES users(user_id)
);
```

---

### 7.2 File Structure

```
library_app/
├── login.py                    # Login screen
├── admin.py                    # Admin dashboard with icons
├── member.py                   # Member dashboard with icon
├── add_member.py               # Member registration form
├── add_book.py                 # Book entry form
├── config.py                   # Database config (user-created)
├── config_template.py          # Config template
├── setup_database_final.py     # Database setup script
├── requirements.txt            # Python dependencies
├── images/                     # Icon and image assets
│   ├── admin_portal.png        # 40x40 admin icon
│   ├── member_portal.png       # 40x40 member icon
│   ├── add_member.png          # 50x50 button icon
│   ├── add_books.png           # 50x50 button icon
│   ├── search_catalog.png      # 50x50 button icon
│   ├── weekly_report.png       # 50x50 button icon
│   └── library.jpeg            # Background image
└── docs/
    └── USER_MANUAL.md          # This manual
```

---

### 7.3 UI Enhancement - Decorative Icons

**Icon Implementation Overview:**

This system features decorative icons to enhance user experience and visual appeal. Icons are implemented using PIL/Pillow library for image handling.

**Icon Specifications:**

| Location | Icon Size | Purpose |
|----------|-----------|---------|
| Admin Dashboard Heading | 40x40 pixels | Visual branding next to "Admin Dashboard" |
| Member Portal Heading | 40x40 pixels | Visual branding next to "Member Portal" |
| Admin Dashboard Buttons | 50x50 pixels | Visual indicators above each button |

**Technical Implementation:**

```python
from PIL import Image, ImageTk

# Load and resize icon
icon_img = Image.open("images/admin_portal.png").resize((40, 40))
icon_photo = ImageTk.PhotoImage(icon_img)

# Display in Label widget
tk.Label(header, image=icon_photo, bg="#2196F3").place(x=230, y=20)

# Keep reference to prevent garbage collection
header.admin_icon = icon_photo
```

**Graceful Fallback:**
If icon files are missing, the application continues without icons using try-except blocks. No errors displayed to users.

**Icon Files Required:**
- admin_portal.png (40x40) - Admin dashboard heading
- member_portal.png (40x40) - Member dashboard heading
- add_member.png (50x50) - Add Member button
- add_books.png (50x50) - Add Book button
- search_catalog.png (50x50) - Search Catalog button
- weekly_report.png (50x50) - Weekly Reports button

---

### 7.4 Business Rules

| Category | Rule | Value |
|----------|------|-------|
| Username | Must be unique | Yes |
| Password | Plain text storage | For educational purposes |
| Book Duplicates | Title + Author check | Prevents duplicates |
| Copies per Book | Allowed range | 1-5 copies |
| Deletion Type | Soft delete | record_status = 'Deleted' |
| Due Date | Calculation | Issue date + 15 days |
| Date Format | Display | dd/mm/yyyy (Indian standard) |

---

### 7.5 Validation Rules

**Add Member Form:**

| Field | Required | Unique | Max Length |
|-------|----------|--------|------------|
| Username | Yes | Yes | 50 |
| Password | Yes | No | 50 |
| Full Name | Yes | No | 100 |
| Address | No | No | 200 |
| Email | No | No | 100 |
| Phone | No | No | 15 |

**Add Book Form:**

| Field | Required | Validation |
|-------|----------|------------|
| Book Title | Yes | Unique with author |
| Author | Yes | Any text |
| ISBN Number | Yes | Any format |
| Publication Year | Yes | Must be integer |
| Number of Copies | Yes | 1-5 inclusive |

---

### 7.6 Keyboard Shortcuts

| Screen | Key | Action |
|--------|-----|--------|
| All Forms | Enter | Submit form |
| All Forms | Tab | Next field |
| Login | Enter | Submit login |
| All Windows | Alt+F4 / Cmd+W | Close window |

---

### 7.7 Glossary

| Term | Definition |
|------|------------|
| **Admin** | User with full privileges to manage library |
| **Member** | Regular user who can borrow books |
| **Copy Number** | Sequential ID for multiple copies (1, 2, 3...) |
| **Book Status** | Current state: New, Issued, or Returned |
| **Record Status** | Deletion state: Active or Deleted |
| **Soft Delete** | Marking as deleted without database removal |
| **Due Date** | Return date (15 days from issue) |
| **ISBN** | International Standard Book Number |
| **Transaction** | Audit trail of all operations |
| **Decorative Icon** | PNG image used for UI enhancement (not functional window icon) |

---

### 7.8 Project Submission Checklist

**Documentation:**
- This User Manual with screenshot placeholders
- README.md
- Source code with comments
- Database schema documentation

**Code Files:**
- login.py
- admin.py (with decorative icons)
- member.py (with decorative icons)
- add_member.py
- add_book.py
- config_template.py (NOT config.py)
- setup_database_final.py
- requirements.txt

**Assets:**
- images/ folder with all icon files
- library.jpeg background
- Sample database export (.sql file)

**Testing:**
- All admin workflows tested
- All member workflows tested
- All validation errors tested
- Icon display verified
- Database connection verified

---

### 7.9 Screenshot Placeholders

The following screenshots should be captured for complete documentation:

**Login & Dashboard:**
1. [SCREENSHOT: Login screen with background image]
2. [SCREENSHOT: Admin Dashboard - 6 buttons in 3x2 grid with icons]

**Add User (Admin/Member):**
3. [SCREENSHOT: Add User form with right-aligned labels and User Type dropdown]
4. [SCREENSHOT: Add User form filled - Member type selected]
5. [SCREENSHOT: Add User form filled - Admin type selected]
6. [SCREENSHOT: Member added successfully with Member ID]
7. [SCREENSHOT: Admin user added successfully message]
8. [SCREENSHOT: Duplicate username error]
9. [SCREENSHOT: Required fields validation error]

**Add Book:**
10. [SCREENSHOT: Add Book form with right-aligned labels and centered buttons]
11. [SCREENSHOT: Book added successfully - multiple copies]
12. [SCREENSHOT: Maximum copies error (> 5)]

**View Users:**
13. [SCREENSHOT: View Users window with all users listed]

**Search Catalog & Book Management:**
14. [SCREENSHOT: Book catalog with search and filter options]
15. [SCREENSHOT: All copies window showing different statuses]
16. [SCREENSHOT: Issue book dialog with member username]
17. [SCREENSHOT: Book issued successfully with due date]
18. [SCREENSHOT: Overdue prevention error - cannot issue to defaulter]
19. [SCREENSHOT: Return book confirmation dialog]
20. [SCREENSHOT: Delete book validation - already deleted error]

**Defaulters List:**
21. [SCREENSHOT: Defaulters List window showing overdue books]
22. [SCREENSHOT: No overdue books found message]

**Weekly Reports:**
23. [SCREENSHOT: Weekly Report window with transactions]

**Member Portal:**
24. [SCREENSHOT: Member Dashboard with icon next to heading]
25. [SCREENSHOT: My Borrowed Books - normal and overdue (red) highlighted]
26. [SCREENSHOT: Overdue legend warning message]
27. [SCREENSHOT: Member search books catalog (read-only)]

---

### 7.10 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Oct 2024 | Initial release with basic CRUD operations |
| 2.0 | Nov 2024 | Added multiple copies, transaction logging |
| 3.0 | Nov 2024 | Added duplicate prevention, validation (1-5 copies) |
| 3.1 | Dec 2024 | Added decorative UI icons (40x40 and 50x50) |
| 3.2 | Dec 2024 | Fixed delete bug, added Defaulters List, overdue prevention |
| 3.3 | Dec 2024 | Added View Users, Member overdue highlighting, code optimization |
| 3.4 | Dec 2024 | UI improvements: right-aligned labels, centered buttons, User Type dropdown |

---

## End of User Manual

**Document Version**: 2.0
**Last Updated**: December 2024
**Estimated Pages**: 20-25 pages
**Features**: Icon-enhanced UI with decorative PNG images

---

**Contact Information**

**Developer**: Jhanvi Shankar
**Class**: XII-B
**Roll Number**: ASLSKLDK
**Subject**: Computer Science
**Academic Year**: 2024-2025

---

**Acknowledgments**

This Library Management System was developed as part of the CBSE Class XII Computer Science practical project requirement.

**Technologies Used:**
- Python 3.x
- Tkinter (GUI Framework)
- MySQL (Database Management)
- mysql-connector-python (Database Driver)
- Pillow (PIL - Image Processing for decorative icons)

**References:**
- CBSE Computer Science Textbook - Class XII
- Python Official Documentation
- MySQL Documentation
- Tkinter and PIL/Pillow Documentation

---

**End of Document**
