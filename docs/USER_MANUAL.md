# Library Management System
## User Manual

**Class XII Computer Science Project**
**Academic Year**: 2024-2025
**Student**: Jhanvi Shankar
**Roll No**: ASLSKLDK

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [System Overview](#2-system-overview)
3. [Getting Started](#3-getting-started)
4. [Login Process](#4-login-process)
5. [Administrator Workflows](#5-administrator-workflows)
6. [Member Workflows](#6-member-workflows)
7. [Troubleshooting](#7-troubleshooting)
8. [Appendix](#8-appendix)

---

## 1. Introduction

### 1.1 Purpose
This Library Management System is designed to efficiently manage library operations including book cataloging, member management, book issuing, and returns. The system provides separate interfaces for administrators and members, ensuring role-based access control.

### 1.2 Scope
The system supports:
- User authentication with role-based access (Admin/Member)
- Book inventory management with multiple copies support
- Member registration and profile management
- Book issue and return tracking
- Search and filter capabilities
- Transaction audit trail

### 1.3 Technology Stack
- **Programming Language**: Python 3.7+
- **GUI Framework**: Tkinter
- **Database**: MySQL 8.0
- **Libraries**: mysql-connector-python, Pillow (PIL)

---

## 2. System Overview

### 2.1 Key Features

#### For Administrators:
- Add new library members
- Add books to the catalog (1-5 copies at a time)
- Search and browse book catalog
- Issue books to members (max 3 books per member)
- Process book returns
- Soft delete books (cannot delete issued books)
- View transaction history

#### For Members:
- View borrowed books with due dates
- Search available books
- Track issue and return dates

### 2.2 System Architecture

```
┌─────────────────────────────────────────────────┐
│           Login Screen (login.py)               │
│     Role-based Authentication System            │
└─────────────┬───────────────────────────────────┘
              │
              ├─────────────────────┬──────────────────────┐
              ▼                     ▼                      ▼
    ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
    │  Admin Dashboard │  │ Member Dashboard │  │  MySQL Database  │
    │   (admin.py)     │  │  (member.py)     │  │                  │
    └──────────────────┘  └──────────────────┘  └──────────────────┘
              │                     │                      │
              ├─────────────────────┴──────────────────────┤
              │                                            │
    ┌─────────▼──────────┐                    ┌───────────▼─────────┐
    │ Add Member/Book    │                    │  Tables:            │
    │ (add_member.py,    │                    │  - users            │
    │  add_book.py)      │                    │  - members          │
    └────────────────────┘                    │  - books            │
                                               │  - transactions     │
                                               └─────────────────────┘
```

### 2.3 Database Schema Overview

| Table | Purpose | Key Fields |
|-------|---------|------------|
| **users** | Store login credentials | username, password, user_type |
| **members** | Store member details | name, address, email, phone |
| **books** | Store book inventory | title, author, isbn, copy_number |
| **transactions** | Audit trail | action, transaction_date, notes |

---

## 3. Getting Started

### 3.1 System Requirements
- Python 3.7 or higher
- MySQL 8.0 or higher
- 800x600 screen resolution minimum
- 100 MB free disk space

### 3.2 Installation Steps

**Step 1**: Install Python dependencies
```bash
pip install -r requirements.txt
```

**Step 2**: Configure database connection
```bash
cp config_template.py config.py
# Edit config.py with your MySQL password
```

**Step 3**: Setup database
```bash
python3 setup_database_final.py
```

**Step 4**: Launch the application
```bash
python3 login.py
```

### 3.3 Default Login Credentials

| Role | Username | Password | Notes |
|------|----------|----------|-------|
| Admin | `admin` | `admin123` | Primary administrator |
| Admin | `librarian` | `lib123` | Secondary administrator |
| Member | `priya` | `priya123` | Test member with issued book |
| Member | `rahul` | `rahul123` | Test member with issued book |
| Member | `anjali` | `anjali123` | Test member (no books) |

---

## 4. Login Process

### 4.1 Launching the Application

**Step 1**: Navigate to the application folder and run `login.py`

**Step 2**: The login screen will appear

**[SCREENSHOT 1: Login Screen]**
```
Screenshot should show:
- Application window (800x600)
- Library background image
- "Library Management System" title
- Username field
- Password field (with masked input)
- Login button
- Exit button
```

### 4.2 Login Workflow

**Step 1**: Enter your username in the "Username" field

**Step 2**: Enter your password in the "Password" field (appears as asterisks)

**Step 3**: Click the "Login" button

**Step 4**: System validates credentials:
- ✅ Valid credentials → Redirects to appropriate dashboard (Admin or Member)
- ❌ Invalid credentials → Shows error message "Invalid username or password"
- ⚠️ Inactive account → Shows error message "Account is inactive"

**[SCREENSHOT 2: Login with Credentials Entered]**
```
Screenshot should show:
- Username field filled with "admin"
- Password field with asterisks (*****)
- Cursor hovering over Login button
```

**[SCREENSHOT 3: Invalid Login Error]**
```
Screenshot should show:
- Error dialog box with message "Invalid username or password"
- OK button to dismiss the error
```

### 4.3 Post-Login Navigation

After successful login:
- **Admin users** → Redirected to Admin Dashboard
- **Member users** → Redirected to Member Dashboard

The login window closes automatically upon successful authentication.

---

## 5. Administrator Workflows

### 5.1 Admin Dashboard Overview

**[SCREENSHOT 4: Admin Dashboard - Main Screen]**
```
Screenshot should show:
- Welcome message with admin name
- Button: "Add Member"
- Button: "Add Book"
- Button: "Search Books"
- Button: "Logout"
- All buttons properly aligned and visible
```

The Admin Dashboard provides access to all administrative functions:

| Button | Function | Description |
|--------|----------|-------------|
| **Add Member** | Opens member registration form | Create new library member accounts |
| **Add Book** | Opens book entry form | Add new books to catalog |
| **Search Books** | Opens catalog browser | View, issue, return, and delete books |
| **Logout** | Return to login screen | Securely exit the system |

---

### 5.2 Workflow 1: Adding a New Member

#### 5.2.1 Process Flow

```
Admin Dashboard → Click "Add Member" → Fill Form → Click "Save" → Validation → Success/Error
```

#### 5.2.2 Step-by-Step Instructions

**Step 1**: From the Admin Dashboard, click the **"Add Member"** button

**[SCREENSHOT 5: Click Add Member Button]**
```
Screenshot should show:
- Admin Dashboard with "Add Member" button highlighted
- Cursor hovering over the button
```

**Step 2**: The "Add Member" form window opens (800x600 pixels)

**[SCREENSHOT 6: Add Member Form - Empty]**
```
Screenshot should show:
- Form title: "Add Member"
- All empty fields:
  * Username: [empty]
  * Password: [empty]
  * Full Name: [empty]
  * Address: [empty]
  * Email: [empty]
  * Phone: [empty]
- Save button
- Reset button
```

**Step 3**: Fill in the required fields (marked with asterisk in validation):

| Field | Type | Required | Validation Rules | Example |
|-------|------|----------|------------------|---------|
| **Username** | Text | ✅ Yes | Must be unique, no spaces | `neha_sharma` |
| **Password** | Password | ✅ Yes | Minimum 1 character | `neha@2024` |
| **Full Name** | Text | ✅ Yes | Any text | `Neha Sharma` |
| **Address** | Text | ❌ No | Any text | `123, MG Road, Delhi` |
| **Email** | Text | ❌ No | Any format (no validation) | `neha@email.com` |
| **Phone** | Text | ❌ No | Any format | `9876543210` |

**[SCREENSHOT 7: Add Member Form - Filled]**
```
Screenshot should show:
- Username: neha_sharma
- Password: ****** (masked)
- Full Name: Neha Sharma
- Address: 123, MG Road, Delhi
- Email: neha@email.com
- Phone: 9876543210
- Cursor hovering over Save button
```

**Step 4**: Click the **"Save"** button

**Step 5**: System performs validation:

##### Validation Check 1: Required Fields
If any required field is empty:

**[SCREENSHOT 8: Missing Required Fields Error]**
```
Screenshot should show:
- Error dialog: "Username, Password and Name are required"
- OK button
```

##### Validation Check 2: Duplicate Username
If username already exists in the system:

**[SCREENSHOT 9: Duplicate Username Error]**
```
Screenshot should show:
- Error dialog: "Username 'neha_sharma' already exists! Please choose a different username."
- OK button
- Form still visible in background with entered data
```

**Step 6**: Upon successful validation:

**[SCREENSHOT 10: Member Added Successfully]**
```
Screenshot should show:
- Success dialog: "Member added successfully! Member ID: 6"
- OK button
- Form cleared (all fields empty)
```

#### 5.2.3 Post-Save Actions

After clicking "OK" on success message:
- Form fields are automatically cleared (Reset function)
- You can add another member immediately
- Close the window to return to Admin Dashboard

**Step 7**: Click the **"Reset"** button (optional)

This clears all form fields without saving, useful if you want to start over.

---

### 5.3 Workflow 2: Adding a New Book

#### 5.3.1 Process Flow

```
Admin Dashboard → Click "Add Book" → Fill Form → Click "Save" → Validation → Add Multiple Copies → Success/Error
```

#### 5.3.2 Step-by-Step Instructions

**Step 1**: From the Admin Dashboard, click the **"Add Book"** button

**[SCREENSHOT 11: Click Add Book Button]**
```
Screenshot should show:
- Admin Dashboard with "Add Book" button highlighted
- Cursor hovering over the button
```

**Step 2**: The "Add Book" form window opens

**[SCREENSHOT 12: Add Book Form - Empty]**
```
Screenshot should show:
- Form title: "Add Book"
- All empty fields:
  * Book Title: [empty]
  * Author: [empty]
  * ISBN Number: [empty]
  * Publication Year: [empty]
  * Number of Copies: [empty]
- Save button
- Reset button
```

**Step 3**: Fill in all fields (all are required):

| Field | Type | Required | Validation Rules | Example |
|-------|------|----------|------------------|---------|
| **Book Title** | Text | ✅ Yes | Must be unique per author | `The God of Small Things` |
| **Author** | Text | ✅ Yes | Any text | `Arundhati Roy` |
| **ISBN Number** | Text | ✅ Yes | Any format | `978-0-375-50752-4` |
| **Publication Year** | Number | ✅ Yes | Must be valid integer | `1997` |
| **Number of Copies** | Number | ✅ Yes | 1-5 (inclusive) | `3` |

**[SCREENSHOT 13: Add Book Form - Filled]**
```
Screenshot should show:
- Book Title: The God of Small Things
- Author: Arundhati Roy
- ISBN Number: 978-0-375-50752-4
- Publication Year: 1997
- Number of Copies: 3
- Cursor hovering over Save button
```

**Step 4**: Click the **"Save"** button

**Step 5**: System performs validation:

##### Validation Check 1: All Fields Required
If any field is empty:

**[SCREENSHOT 14: Empty Fields Error]**
```
Screenshot should show:
- Error dialog: "All fields are required!"
- OK button
```

##### Validation Check 2: Number Validation
If Year or Copies contain non-numeric values:

**[SCREENSHOT 15: Invalid Number Error]**
```
Screenshot should show:
- Error dialog: "Year and copies must be valid numbers"
- OK button
```

##### Validation Check 3: Minimum Copies
If copies < 1:

**[SCREENSHOT 16: Minimum Copies Error]**
```
Screenshot should show:
- Error dialog: "Number of copies must be at least 1"
- OK button
```

##### Validation Check 4: Maximum Copies
If copies > 5:

**[SCREENSHOT 17: Maximum Copies Error]**
```
Screenshot should show:
- Error dialog: "Number of copies cannot be more than 5"
- OK button
```

##### Validation Check 5: Duplicate Book
If book with same title and author exists:

**[SCREENSHOT 18: Duplicate Book Error]**
```
Screenshot should show:
- Error dialog: "Book 'The God of Small Things' by Arundhati Roy already exists in the library! Use a different title or check existing copies."
- OK button
```

**Step 6**: Upon successful validation:

**[SCREENSHOT 19: Book Added Successfully]**
```
Screenshot should show:
- Success dialog: "3 copies of 'The God of Small Things' added successfully!"
- OK button
- Form cleared (all fields empty)
```

#### 5.3.3 How Multiple Copies Work

When you add a book with 3 copies, the system:
1. Creates 3 separate database entries
2. Assigns copy numbers: Copy 1, Copy 2, Copy 3
3. Sets all copies to status: "New"
4. Logs 3 transactions in the audit trail

Example:
```
Book ID: 201 | Title: The God of Small Things | Copy: 1 | Status: New
Book ID: 202 | Title: The God of Small Things | Copy: 2 | Status: New
Book ID: 203 | Title: The God of Small Things | Copy: 3 | Status: New
```

Each copy can be issued, returned, and tracked independently.

---

### 5.4 Workflow 3: Searching and Browsing Books

#### 5.4.1 Process Flow

```
Admin Dashboard → Click "Search Books" → Catalog Opens → Search/Filter → View Results → (Optional: Issue/Return/Delete)
```

#### 5.4.2 Step-by-Step Instructions

**Step 1**: From the Admin Dashboard, click the **"Search Books"** button

**[SCREENSHOT 20: Click Search Books Button]**
```
Screenshot should show:
- Admin Dashboard with "Search Books" button highlighted
- Cursor hovering over the button
```

**Step 2**: The Book Catalog window opens

**[SCREENSHOT 21: Book Catalog - Default View]**
```
Screenshot should show:
- Search bar at top
- Filter dropdown: "Active" (default)
- Table with columns:
  * Title
  * Author
  * ISBN
  * Year
  * Total Copies
  * Available
  * Issued To
  * Issue Date
  * Due Date
- Multiple book entries visible
- Buttons at bottom: Issue Book, Return Book, Delete Book, Close
```

#### 5.4.3 Catalog Features Explained

**Column Descriptions:**

| Column | Description | Example |
|--------|-------------|---------|
| **Title** | Book title | `Train to Pakistan` |
| **Author** | Book author | `Khushwant Singh` |
| **ISBN** | ISBN number | `978-0-14-118289-7` |
| **Year** | Publication year | `1956` |
| **Total Copies** | Number of copies in system | `2` |
| **Available** | Copies available to borrow | `1` (means 1 is issued, 1 is available) |
| **Issued To** | Member username (if issued) | `priya` or `(Multiple)` |
| **Issue Date** | Date issued (dd/mm/yyyy) | `15/11/2024` |
| **Due Date** | Return due date (dd/mm/yyyy) | `30/11/2024` (15 days from issue) |

**Step 3**: Using the Search Feature

**[SCREENSHOT 22: Search Bar in Use]**
```
Screenshot should show:
- Search bar with text: "train"
- Filtered results showing only books with "train" in title/author
- Same table structure with fewer rows
```

**Search Behavior:**
- Type any text in the search bar
- Search matches: Title, Author, ISBN
- Results update automatically (real-time search)
- Search is case-insensitive

**Step 4**: Using the Filter Dropdown

**[SCREENSHOT 23: Filter Dropdown Options]**
```
Screenshot should show:
- Filter dropdown expanded showing three options:
  * Active (selected)
  * Deleted
  * All
```

**Filter Options:**

| Filter | Shows | Use Case |
|--------|-------|----------|
| **Active** | Books with record_status = "Active" | Default view, shows current catalog |
| **Deleted** | Books with record_status = "Deleted" | View soft-deleted books |
| **All** | Both Active and Deleted books | Complete inventory view |

**[SCREENSHOT 24: Catalog with Deleted Filter]**
```
Screenshot should show:
- Filter set to "Deleted"
- Table showing only deleted books (grayed out or distinct appearance)
- Deleted books cannot be issued (grayed buttons)
```

#### 5.4.4 Viewing All Copies of a Book

**Step 5**: Double-click any book row to view all copies

**[SCREENSHOT 25: Double-Click to View Copies]**
```
Screenshot should show:
- Main catalog with one row highlighted
- Cursor positioned for double-click
- Tooltip or visual indicator showing "Double-click to view copies"
```

**Step 6**: Copy Details window opens

**[SCREENSHOT 26: All Copies View]**
```
Screenshot should show:
- New window titled: "All Copies of: Train to Pakistan by Khushwant Singh"
- Table with columns:
  * Copy Number
  * Book Status (New/Issued/Returned)
  * Issued To
  * Issue Date
  * Due Date
- Example rows:
  * Copy 1 | Issued | priya | 15/11/2024 | 30/11/2024
  * Copy 2 | New | - | - | -
- Button: "Return Selected Copy" (enabled only if copy is issued)
- Button: "Close"
```

**Copy Status Meanings:**

| Status | Description | Available to Issue? |
|--------|-------------|---------------------|
| **New** | Never issued before | ✅ Yes |
| **Issued** | Currently with a member | ❌ No (must be returned first) |
| **Returned** | Previously issued, now returned | ✅ Yes |

---

### 5.5 Workflow 4: Issuing a Book to Member

#### 5.5.1 Process Flow

```
Search Books → Select Available Book → Click "Issue Book" → Enter Member Username → Validation → Book Issued
```

#### 5.5.2 Step-by-Step Instructions

**Step 1**: From the Book Catalog, select a book that has **Available > 0**

**[SCREENSHOT 27: Selecting Book to Issue]**
```
Screenshot should show:
- Book catalog with one book row highlighted
- Book showing: Available = 1 (or more)
- "Issue Book" button enabled
```

**Step 2**: Click the **"Issue Book"** button

**Step 3**: A dialog box appears asking for member username

**[SCREENSHOT 28: Enter Member Username Dialog]**
```
Screenshot should show:
- Dialog title: "Issue Book"
- Label: "Enter member username:"
- Input field: [empty]
- OK and Cancel buttons
```

**Step 4**: Enter the member's username (e.g., `rahul`)

**[SCREENSHOT 29: Username Entered]**
```
Screenshot should show:
- Input field filled with: "rahul"
- Cursor hovering over OK button
```

**Step 5**: Click **"OK"**

**Step 6**: System validates:

##### Validation 1: Empty Username
**[SCREENSHOT 30: Empty Username Error]**
```
Screenshot should show:
- Error dialog: "Please enter a member username"
- OK button
```

##### Validation 2: Invalid Username
**[SCREENSHOT 31: Invalid Member Error]**
```
Screenshot should show:
- Error dialog: "Member 'xyz123' not found"
- OK button
```

##### Validation 3: No Available Copies
If all copies are issued:
**[SCREENSHOT 32: No Copies Available Error]**
```
Screenshot should show:
- Error dialog: "No copies of this book are available for issue"
- OK button
```

**Step 7**: Upon successful issue:

**[SCREENSHOT 33: Book Issued Successfully]**
```
Screenshot should show:
- Success dialog: "Book issued successfully to rahul! Due date: 30/11/2024"
- OK button
```

**Step 8**: Catalog updates automatically

**[SCREENSHOT 34: Catalog After Issue]**
```
Screenshot should show:
- Same book row now showing:
  * Available: decreased by 1
  * Issued To: "rahul"
  * Issue Date: "15/11/2024"
  * Due Date: "30/11/2024"
```

#### 5.5.3 Issue Logic Behind the Scenes

When a book is issued:
1. System finds first available copy (status = "New" or "Returned")
2. Updates that copy's status to "Issued"
3. Records member ID and current date
4. Calculates due date (current date + 15 days)
5. Creates transaction record (action = "Issue")
6. Refreshes catalog display

---

### 5.6 Workflow 5: Returning a Book

#### 5.6.1 Process Flow

```
Search Books → Double-click Book → View Copies → Select Issued Copy → Click "Return Selected Copy" → Book Returned
```

#### 5.6.2 Step-by-Step Instructions

**Step 1**: From the Book Catalog, find the book that was issued

**Step 2**: Double-click the book row to view all copies

**[SCREENSHOT 35: View Copies for Return]**
```
Screenshot should show:
- All copies window open
- Multiple rows visible
- One row with Status = "Issued"
- That row is highlighted/selected
- "Return Selected Copy" button is enabled
```

**Step 3**: Select the issued copy (click on it)

**Step 4**: Click **"Return Selected Copy"** button

**Step 5**: Confirmation dialog appears

**[SCREENSHOT 36: Return Confirmation Dialog]**
```
Screenshot should show:
- Confirmation dialog: "Return this book? Copy 1 issued to rahul"
- Yes and No buttons
```

**Step 6**: Click **"Yes"** to confirm

**Step 7**: Book is returned successfully

**[SCREENSHOT 37: Book Returned Successfully]**
```
Screenshot should show:
- Success dialog: "Book returned successfully!"
- OK button
```

**Step 8**: Copy window refreshes automatically

**[SCREENSHOT 38: Copy Status After Return]**
```
Screenshot should show:
- Same copy row now showing:
  * Book Status: "Returned"
  * Issued To: (cleared)
  * Issue Date: (cleared)
  * Due Date: (cleared)
- "Return Selected Copy" button now disabled (grayed out)
```

**Step 9**: Close the copy window

**Step 10**: Main catalog also updates

**[SCREENSHOT 39: Catalog After Return]**
```
Screenshot should show:
- Book row showing:
  * Available: increased by 1
  * Issued To: (cleared or shows another member if multiple copies)
  * Issue Date/Due Date: cleared
```

#### 5.6.3 Return Logic

When a book is returned:
1. Copy status changes from "Issued" to "Returned"
2. Member ID, issue date, and due date are cleared
3. Transaction logged (action = "Return")
4. Available count increases by 1
5. Book becomes available for next issue
6. Popup window stays open for processing more returns

**Important Note**: The popup window remains open after returning a book, allowing you to process multiple returns without closing and reopening.

---

### 5.7 Workflow 6: Deleting a Book

#### 5.7.1 Process Flow

```
Search Books → Select Book → Click "Delete Book" → Confirmation → Book Soft-Deleted
```

#### 5.7.2 Step-by-Step Instructions

**Step 1**: From the Book Catalog, select the book to delete

**[SCREENSHOT 40: Select Book to Delete]**
```
Screenshot should show:
- Book catalog with one book row highlighted
- "Delete Book" button enabled
- Book can be in any status (New/Issued/Returned)
```

**Step 2**: Click the **"Delete Book"** button

**Step 3**: Confirmation dialog appears

**[SCREENSHOT 41: Delete Confirmation]**
```
Screenshot should show:
- Confirmation dialog: "Are you sure you want to delete: Train to Pakistan by Khushwant Singh?"
- Yes and No buttons
```

**Step 4**: Click **"Yes"** to confirm deletion

**Step 5**: Book is soft-deleted

**[SCREENSHOT 42: Book Deleted Successfully]**
```
Screenshot should show:
- Success dialog: "Book deleted successfully"
- OK button
```

**Step 6**: Book disappears from Active view

**[SCREENSHOT 43: Catalog After Deletion]**
```
Screenshot should show:
- Book catalog with the deleted book no longer visible
- Filter still set to "Active"
- Remaining books displayed
```

**Step 7**: Verify deletion by changing filter to "Deleted"

**[SCREENSHOT 44: Viewing Deleted Books]**
```
Screenshot should show:
- Filter changed to "Deleted"
- Deleted book now visible (possibly with visual indicator)
- "Issue Book" button disabled for deleted books
```

#### 5.7.3 Soft Delete Explained

**What is Soft Delete?**
- Book is NOT permanently removed from database
- Record status changes to "Deleted"
- Book no longer appears in Active catalog
- Can be restored manually via database if needed
- Maintains data integrity and audit trail

**What Happens to All Copies?**
When you delete a book:
- ALL copies of that book are marked as deleted
- Even issued copies become "deleted" (but issue record remains)
- No new issues can be made
- Previous transaction history is preserved

---

### 5.8 Admin Dashboard - Logout

**Step 1**: From Admin Dashboard, click **"Logout"** button

**[SCREENSHOT 45: Logout Button]**
```
Screenshot should show:
- Admin Dashboard
- "Logout" button highlighted
- Cursor hovering over button
```

**Step 2**: System returns to login screen

**[SCREENSHOT 46: Back to Login Screen]**
```
Screenshot should show:
- Login screen reappears
- Fields are empty
- Ready for next login
```

No confirmation is required for logout - it happens immediately.

---

## 6. Member Workflows

### 6.1 Member Dashboard Overview

**[SCREENSHOT 47: Member Dashboard - Main Screen]**
```
Screenshot should show:
- Welcome message: "Welcome, Priya!"
- Button: "My Borrowed Books"
- Button: "Search Books"
- Button: "Logout"
- Clean, simple interface
```

The Member Dashboard provides limited functionality compared to Admin:

| Button | Function | Description |
|--------|----------|-------------|
| **My Borrowed Books** | View issued books | See all books you have borrowed |
| **Search Books** | Browse catalog | View available books (read-only) |
| **Logout** | Return to login | Exit the system |

---

### 6.2 Workflow 1: Viewing Borrowed Books

#### 6.2.1 Process Flow

```
Member Dashboard → Click "My Borrowed Books" → View Issued Books → Check Due Dates
```

#### 6.2.2 Step-by-Step Instructions

**Step 1**: Login as a member (e.g., username: `priya`, password: `priya123`)

**Step 2**: From Member Dashboard, click **"My Borrowed Books"** button

**[SCREENSHOT 48: Click My Borrowed Books]**
```
Screenshot should show:
- Member Dashboard
- "My Borrowed Books" button highlighted
- Cursor hovering over button
```

**Step 3**: Borrowed Books window opens

**[SCREENSHOT 49: My Borrowed Books - With Books]**
```
Screenshot should show:
- Window title: "My Borrowed Books - Priya"
- Table with columns:
  * Book Title
  * Author
  * ISBN
  * Issue Date (dd/mm/yyyy)
  * Due Date (dd/mm/yyyy)
- Sample row:
  * Train to Pakistan | Khushwant Singh | 978-0-14-118289-7 | 15/11/2024 | 30/11/2024
- Close button at bottom
```

**[SCREENSHOT 50: My Borrowed Books - No Books]**
```
Screenshot should show:
- Window title: "My Borrowed Books - Anjali"
- Empty table (no rows)
- Message or empty state
- Close button at bottom
```

#### 6.2.3 Understanding Due Dates

**Due Date Calculation:**
- Due Date = Issue Date + 15 days
- Format: dd/mm/yyyy (Indian standard)

**Example:**
- Issue Date: 15/11/2024
- Due Date: 30/11/2024

**Important Notes for Students:**
- Check due dates regularly
- Return books before due date
- Contact librarian for renewals
- Overdue books may result in fines (if implemented)

**Step 4**: Close the window to return to Member Dashboard

---

### 6.3 Workflow 2: Searching Available Books

#### 6.3.1 Process Flow

```
Member Dashboard → Click "Search Books" → Browse Catalog → Search by Title/Author → View Details
```

#### 6.3.2 Step-by-Step Instructions

**Step 1**: From Member Dashboard, click **"Search Books"** button

**[SCREENSHOT 51: Click Search Books (Member)]**
```
Screenshot should show:
- Member Dashboard
- "Search Books" button highlighted
- Cursor hovering over button
```

**Step 2**: Book Catalog window opens (Read-Only view)

**[SCREENSHOT 52: Member Book Catalog View]**
```
Screenshot should show:
- Search bar at top
- Table with columns:
  * Title
  * Author
  * Year
  * Available Copies
- Multiple book rows (only books with available copies)
- NO action buttons (no Issue, Return, Delete)
- Only "Close" button
- Shows only books that can be borrowed
```

**Step 3**: Use search bar to find books

**[SCREENSHOT 53: Member Searching for Book]**
```
Screenshot should show:
- Search bar with text: "chetan"
- Filtered results showing Chetan Bhagat books
- Available count visible for each book
- Books with Available = 0 shown clearly
```

#### 6.3.3 Member Catalog Features

**What Members Can See:**
- ✅ Book title, author, ISBN, year
- ✅ Number of available copies
- ✅ Search functionality (title/author/ISBN)
- ❌ Cannot see who has borrowed books
- ❌ Cannot see issue/due dates (except for their own books)
- ❌ Cannot issue, return, or delete books

**Column Descriptions:**

| Column | Description | Example |
|--------|-------------|---------|
| **Title** | Book title | `Five Point Someone` |
| **Author** | Book author | `Chetan Bhagat` |
| **ISBN** | ISBN number | `978-81-291-0000-0` |
| **Year** | Publication year | `2004` |
| **Available Copies** | Copies available to borrow | `2` |

**Step 4**: To borrow a book, members must:
1. Note down the book title and author
2. Contact admin/librarian
3. Admin will issue the book from their dashboard

---

### 6.4 Member Dashboard - Logout

**Step 1**: From Member Dashboard, click **"Logout"** button

**[SCREENSHOT 54: Member Logout]**
```
Screenshot should show:
- Member Dashboard
- "Logout" button highlighted
- Cursor hovering over button
```

**Step 2**: System returns to login screen immediately

---

## 7. Troubleshooting

### 7.1 Common Issues and Solutions

#### Issue 1: Login Failed - Invalid Credentials

**Error Message:** "Invalid username or password"

**Possible Causes:**
1. Incorrect username or password
2. Username is case-sensitive
3. Extra spaces in username/password

**Solutions:**
- ✅ Verify username and password carefully
- ✅ Check if Caps Lock is ON
- ✅ Remove any leading/trailing spaces
- ✅ Try default credentials to test system

**[SCREENSHOT 55: Invalid Credentials Error]**
```
Screenshot showing error dialog
```

---

#### Issue 2: Account Inactive

**Error Message:** "Account is inactive. Please contact administrator."

**Possible Causes:**
1. User account has been deactivated
2. Database status field set to "inactive"

**Solutions:**
- ✅ Contact system administrator
- ✅ Administrator can activate account via database:
  ```sql
  UPDATE users SET status = 'active' WHERE username = 'username';
  ```

---

#### Issue 3: Cannot Add Member - Duplicate Username

**Error Message:** "Username 'xxx' already exists! Please choose a different username."

**Possible Causes:**
1. Username already registered in system
2. Previous member with same username

**Solutions:**
- ✅ Choose a different username (e.g., add numbers: john_2024)
- ✅ Check existing members before registration
- ✅ Use naming convention: firstname_lastname

---

#### Issue 4: Cannot Add Book - Duplicate Book

**Error Message:** "Book 'xxx' by yyy already exists in the library!"

**Possible Causes:**
1. Book with exact same title and author exists
2. Attempting to add duplicates instead of additional copies

**Solutions:**
- ✅ Search catalog first to check if book exists
- ✅ If book exists, check how many copies are already available
- ✅ If you need more copies, contact database admin
- ✅ Check for typos in title/author (slight differences allowed)

---

#### Issue 5: Copies Validation Error

**Error Message:** "Number of copies cannot be more than 5"

**Possible Causes:**
1. Entered value > 5 in Number of Copies field
2. Business rule limits copies to maximum 5

**Solutions:**
- ✅ Enter a value between 1 and 5
- ✅ If you need more than 5 copies, add the book in batches
- ✅ Example: Add 5 copies, then modify database directly for more

---

#### Issue 6: Cannot Issue Book - No Copies Available

**Error Message:** "No copies of this book are available for issue"

**Possible Causes:**
1. All copies are currently issued to other members
2. Book status shows Available = 0

**Solutions:**
- ✅ Wait for members to return copies
- ✅ Check due dates to see when returns are expected
- ✅ Consider adding more copies of the book
- ✅ Search for alternative books on same topic

---

#### Issue 7: Database Connection Error

**Error Message:** "Failed to connect to database" or "Access denied for user 'root'"

**Possible Causes:**
1. MySQL server not running
2. Incorrect password in config.py
3. Database not created

**Solutions:**
- ✅ Start MySQL server:
  ```bash
  # On macOS
  mysql.server start

  # On Windows
  net start MySQL80
  ```
- ✅ Verify config.py has correct password
- ✅ Run database setup:
  ```bash
  python3 setup_database_final.py
  ```

---

#### Issue 8: Background Image Not Loading

**Error Message:** No error, but login screen shows no background

**Possible Causes:**
1. library.jpeg file missing
2. File in wrong location
3. File permissions issue

**Solutions:**
- ✅ Verify library.jpeg exists in same folder as login.py
- ✅ Check file name spelling (case-sensitive on Linux/macOS)
- ✅ Try re-downloading or replacing the image file

---

#### Issue 9: Book Not Appearing After Adding

**Symptom:** Added book successfully but cannot find it in catalog

**Possible Causes:**
1. Filter set to "Deleted"
2. Search filter active
3. Display not refreshed

**Solutions:**
- ✅ Set filter to "Active" or "All"
- ✅ Clear search bar (remove search text)
- ✅ Close and reopen Search Books window
- ✅ Logout and login again

---

#### Issue 10: Cannot Return Book

**Symptom:** "Return Selected Copy" button is disabled/grayed out

**Possible Causes:**
1. Selected copy is not in "Issued" status
2. Copy is "New" or "Returned"
3. Wrong copy selected

**Solutions:**
- ✅ Select a copy with Status = "Issued"
- ✅ Check Issued To column is not empty
- ✅ Ensure you're logged in as Admin
- ✅ Refresh the copies window

---

### 7.2 Error Prevention Best Practices

#### For Administrators:

1. **Before Adding Members:**
   - Check if username already exists
   - Use consistent naming convention
   - Keep usernames simple and lowercase

2. **Before Adding Books:**
   - Search catalog to avoid duplicates
   - Verify ISBN numbers
   - Use standard title/author formats
   - Start with 1-2 copies, add more if needed

3. **Before Issuing Books:**
   - Verify member username is correct
   - Check book availability first
   - Note down due dates for follow-up

4. **Before Deleting Books:**
   - Confirm you're deleting the correct book
   - Remember deletion is permanent (soft delete)
   - Consider if book should be retained for history

#### For Members:

1. **Borrowing Books:**
   - Note down book details before requesting
   - Keep track of due dates
   - Request renewal before due date if needed

2. **Searching Books:**
   - Use partial keywords for better results
   - Try both title and author searches
   - Check Available count before requesting

---

### 7.3 Database Recovery

#### If Database Becomes Corrupt:

**Step 1**: Backup current database (if possible)
```bash
mysqldump -u root -p library_management_system > backup.sql
```

**Step 2**: Drop and recreate database
```bash
mysql -u root -p
```
```sql
DROP DATABASE library_management_system;
```

**Step 3**: Run setup script again
```bash
python3 setup_database_final.py
```

**Step 4**: Restore data from backup (if needed)
```bash
mysql -u root -p library_management_system < backup.sql
```

---

## 8. Appendix

### 8.1 Database Table Structures

#### Table: users
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

#### Table: members
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

#### Table: books
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

#### Table: transactions
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

### 8.2 File Structure Reference

```
library_app/
├── login.py                    # Login authentication screen
├── admin.py                    # Admin dashboard
├── member.py                   # Member dashboard
├── add_member.py               # Member registration form
├── add_book.py                 # Book entry form
├── config.py                   # Database configuration (user-created)
├── config_template.py          # Template for config file
├── setup_database_final.py     # Database initialization script
├── library.jpeg                # Background image for login
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── USER_MANUAL.md              # This user manual
└── INSTRUCTIONS.md             # Setup instructions
```

---

### 8.3 Business Rules Summary

| Rule Category | Rule | Value/Behavior |
|---------------|------|----------------|
| **User Authentication** | Username uniqueness | Must be unique across all users |
| | Password storage | Plain text (for educational purposes) |
| | Account status | active/inactive |
| **Book Management** | Duplicate prevention | Same title + author blocked |
| | Copies per book | 1-5 copies allowed |
| | Copy numbering | Sequential (1, 2, 3, ...) |
| | Deletion type | Soft delete (record_status = 'Deleted') |
| **Book Issuing** | Due date | 15 days from issue date |
| | Issue availability | Only "New" or "Returned" status |
| | Member validation | Username must exist in users table |
| **Date Formats** | Display format | dd/mm/yyyy (Indian standard) |
| | Database storage | DATE type (YYYY-MM-DD) |
| **Transaction Logging** | Actions logged | Add, Issue, Return, Delete |
| | Admin tracking | All actions track admin user ID |

---

### 8.4 Keyboard Shortcuts

| Screen | Key | Action |
|--------|-----|--------|
| **All Forms** | Enter | Submit form (same as clicking Save) |
| | Escape | Close window (where applicable) |
| | Tab | Navigate to next field |
| **Login Screen** | Enter | Submit login |
| **All Windows** | Alt+F4 (Windows) / Cmd+W (Mac) | Close window |

---

### 8.5 Sample Test Cases

#### Test Case 1: Add Member Successfully
```
Input:
- Username: test_member
- Password: test123
- Full Name: Test Member
- Address: 123 Test Street
- Email: test@example.com
- Phone: 9999999999

Expected Output:
- Success message: "Member added successfully! Member ID: X"
- Form cleared
- New entry in users and members tables
```

#### Test Case 2: Add Member - Duplicate Username
```
Input:
- Username: priya (already exists)
- Password: test123
- Full Name: Priya Sharma

Expected Output:
- Error: "Username 'priya' already exists! Please choose a different username."
- Form data retained
- No database insertion
```

#### Test Case 3: Add Book Successfully
```
Input:
- Book Title: Test Book
- Author: Test Author
- ISBN Number: 978-1-234-56789-0
- Publication Year: 2024
- Number of Copies: 3

Expected Output:
- Success: "3 copies of 'Test Book' added successfully!"
- 3 separate book records created with copy_number 1, 2, 3
- 3 transaction records logged
```

#### Test Case 4: Add Book - Maximum Copies Exceeded
```
Input:
- Number of Copies: 6

Expected Output:
- Error: "Number of copies cannot be more than 5"
- No database insertion
```

#### Test Case 5: Issue Book Successfully
```
Precondition:
- Book with Available > 0 exists
- Member username "rahul" exists

Input:
- Select book
- Enter username: rahul

Expected Output:
- Success: "Book issued successfully to rahul! Due date: DD/MM/YYYY"
- Book status changed to "Issued"
- Available count decreased by 1
- Transaction logged
```

#### Test Case 6: Return Book Successfully
```
Precondition:
- Book with Status = "Issued" exists

Input:
- Select issued copy
- Click "Return Selected Copy"
- Confirm "Yes"

Expected Output:
- Success: "Book returned successfully!"
- Book status changed to "Returned"
- Available count increased by 1
- Issue details cleared
- Transaction logged
```

---

### 8.6 Validation Rules Reference

#### Add Member Form Validations

| Field | Required | Unique | Min Length | Max Length | Special Rules |
|-------|----------|--------|------------|------------|---------------|
| Username | ✅ Yes | ✅ Yes | 1 | 50 | No validation on format |
| Password | ✅ Yes | ❌ No | 1 | 50 | Stored as plain text |
| Full Name | ✅ Yes | ❌ No | 1 | 100 | Any characters allowed |
| Address | ❌ No | ❌ No | 0 | 200 | Optional |
| Email | ❌ No | ❌ No | 0 | 100 | No format validation |
| Phone | ❌ No | ❌ No | 0 | 15 | No format validation |

#### Add Book Form Validations

| Field | Required | Unique | Data Type | Min | Max | Special Rules |
|-------|----------|--------|-----------|-----|-----|---------------|
| Book Title | ✅ Yes | ✅ Yes (with author) | Text | 1 char | 200 | Case-sensitive |
| Author | ✅ Yes | ❌ No | Text | 1 char | 100 | Used with title for duplicate check |
| ISBN Number | ✅ Yes | ❌ No | Text | 1 char | 20 | No format validation |
| Publication Year | ✅ Yes | ❌ No | Integer | Any valid int | Any valid int | Must be numeric |
| Number of Copies | ✅ Yes | ❌ No | Integer | 1 | 5 | Must be between 1-5 |

---

### 8.7 Screen Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         LOGIN SCREEN                            │
│                         (login.py)                              │
└──────────────────┬──────────────────────────────────────────────┘
                   │
                   │ Authenticate
                   │
         ┌─────────┴─────────┐
         │                   │
         ▼                   ▼
┌──────────────────┐  ┌──────────────────┐
│ ADMIN DASHBOARD  │  │ MEMBER DASHBOARD │
│   (admin.py)     │  │   (member.py)    │
└────────┬─────────┘  └────────┬─────────┘
         │                     │
         │                     │
    ┌────┼────┬────┐           ├────┬─────┐
    ▼    ▼    ▼    ▼           ▼    ▼     ▼
┌────┐ ┌───┐ ┌──┐ ┌──┐    ┌──────┐ ┌────┐ ┌──┐
│Add │ │Add│ │Sch│ │Out│    │My    │ │Sch │ │Out│
│Mem │ │Book│ │Bks│ │   │    │Books │ │Bks │ │   │
└────┘ └───┘ └──┘ └──┘    └──────┘ └────┘ └──┘
  │      │     │                │      │
  ▼      ▼     │                ▼      │
┌────┐ ┌───┐   │           ┌─────────┐ │
│Form│ │Form│   │           │Issue Lst│ │
└────┘ └───┘   │           └─────────┘ │
               │                        │
               ▼                        ▼
          ┌──────────┐            ┌──────────┐
          │ Catalog  │            │ Catalog  │
          │  (Full)  │            │(ReadOnly)│
          └────┬─────┘            └──────────┘
               │
      ┌────────┼────────┐
      ▼        ▼        ▼
   ┌─────┐ ┌─────┐ ┌──────┐
   │Issue│ │Return│ │Delete│
   └─────┘ └─────┘ └──────┘
```

---

### 8.8 Glossary of Terms

| Term | Definition |
|------|------------|
| **Admin** | User with administrative privileges; can add, issue, return, delete books and members |
| **Member** | Regular user who can borrow books; limited access to view-only features |
| **Copy Number** | Sequential identifier for multiple copies of the same book (1, 2, 3, etc.) |
| **Book Status** | Current state of a book copy: New, Issued, or Returned |
| **Record Status** | Deletion state: Active (visible) or Deleted (soft-deleted) |
| **Soft Delete** | Marking records as deleted without removing from database |
| **Due Date** | Date by which book must be returned (15 days from issue date) |
| **ISBN** | International Standard Book Number - unique book identifier |
| **Transaction** | Audit trail entry logging all book operations (Add, Issue, Return, Delete) |
| **Available Copies** | Number of book copies available for borrowing (New or Returned status) |
| **Total Copies** | Total number of copies of a book in the system (regardless of status) |
| **Authentication** | Process of verifying user identity via username and password |
| **Role-Based Access** | Granting different permissions based on user type (Admin vs Member) |

---

### 8.9 Project Submission Checklist

For Class XII students submitting this project:

#### Documentation Required:
- ✅ This User Manual (with screenshots)
- ✅ README.md (project overview)
- ✅ Source code with comments
- ✅ Database schema documentation
- ✅ Sample output screenshots
- ✅ Project synopsis/abstract

#### Code Files to Submit:
- ✅ login.py
- ✅ admin.py
- ✅ member.py
- ✅ add_member.py
- ✅ add_book.py
- ✅ config_template.py (NOT config.py with password)
- ✅ setup_database_final.py
- ✅ requirements.txt

#### Additional Files:
- ✅ library.jpeg (background image)
- ✅ Sample database export (.sql file)
- ✅ Screenshots folder (organized by section)

#### Pre-Submission Testing:
- ✅ Test all admin workflows
- ✅ Test all member workflows
- ✅ Test all validation errors
- ✅ Test database connection
- ✅ Verify all screenshots are clear
- ✅ Check all code comments are present
- ✅ Run database setup from scratch
- ✅ Test on fresh system (if possible)

---

### 8.10 Screenshot Organization Guide

For easy reference, organize screenshots in folders:

```
Screenshots/
├── 01_Login/
│   ├── SS01_Login_Screen.png
│   ├── SS02_Login_Filled.png
│   └── SS03_Invalid_Login.png
├── 02_Admin_Dashboard/
│   ├── SS04_Admin_Dashboard.png
│   └── SS05_Admin_Logout.png
├── 03_Add_Member/
│   ├── SS06_Add_Member_Empty.png
│   ├── SS07_Add_Member_Filled.png
│   ├── SS08_Missing_Fields_Error.png
│   ├── SS09_Duplicate_Username_Error.png
│   └── SS10_Member_Success.png
├── 04_Add_Book/
│   ├── SS11_Add_Book_Empty.png
│   ├── SS12_Add_Book_Filled.png
│   ├── SS13_Empty_Fields_Error.png
│   ├── SS14_Invalid_Number_Error.png
│   ├── SS15_Min_Copies_Error.png
│   ├── SS16_Max_Copies_Error.png
│   ├── SS17_Duplicate_Book_Error.png
│   └── SS18_Book_Success.png
├── 05_Search_Books_Admin/
│   ├── SS19_Catalog_Default.png
│   ├── SS20_Search_Filter.png
│   ├── SS21_Filter_Options.png
│   ├── SS22_View_Copies.png
│   └── SS23_All_Copies_Window.png
├── 06_Issue_Book/
│   ├── SS24_Select_Book.png
│   ├── SS25_Enter_Username.png
│   ├── SS26_Invalid_Member.png
│   ├── SS27_Issue_Success.png
│   └── SS28_Catalog_Updated.png
├── 07_Return_Book/
│   ├── SS29_View_Issued_Copies.png
│   ├── SS30_Return_Confirmation.png
│   ├── SS31_Return_Success.png
│   └── SS32_Status_Updated.png
├── 08_Delete_Book/
│   ├── SS33_Select_Delete.png
│   ├── SS34_Delete_Confirmation.png
│   ├── SS35_Delete_Success.png
│   └── SS36_View_Deleted.png
├── 09_Member_Dashboard/
│   ├── SS37_Member_Dashboard.png
│   └── SS38_Member_Logout.png
├── 10_My_Borrowed_Books/
│   ├── SS39_My_Books_With_Data.png
│   └── SS40_My_Books_Empty.png
└── 11_Search_Books_Member/
    ├── SS41_Member_Catalog.png
    └── SS42_Member_Search.png
```

---

### 8.11 Contact and Support

For technical support or questions about this system:

**Developer**: Jhanvi Shankar
**Class**: XII-B
**Roll Number**: ASLSKLDK
**Subject**: Computer Science
**Academic Year**: 2024-2025

**Project Repository**: [GitHub Link - if applicable]
**Email**: [Student Email - if applicable]

---

### 8.12 Acknowledgments

This Library Management System was developed as part of the CBSE Class XII Computer Science practical project requirement.

**Technologies Used:**
- Python 3.x
- Tkinter (GUI Framework)
- MySQL (Database Management)
- mysql-connector-python (Database Driver)
- Pillow (Image Processing)

**References:**
- CBSE Computer Science Textbook - Class XII
- Python Official Documentation
- MySQL Documentation
- Tkinter Tutorial Resources

---

### 8.13 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Oct 2024 | Initial release with basic CRUD operations |
| 2.0 | Nov 2024 | Added multiple copies support, transaction logging |
| 3.0 | Nov 2024 | Added duplicate prevention, copies validation (1-5), improved UI |

---

## End of User Manual

**Document Version**: 1.0
**Last Updated**: November 2024
**Total Pages**: [To be counted after PDF generation]
**Total Screenshots**: 54+ (to be captured)

---

### Notes for Screenshot Capture:

**When capturing screenshots:**

1. **Window Size**: Ensure all windows are 800x600 as designed
2. **Image Quality**: Use PNG format for clarity
3. **Naming Convention**: Use descriptive names (e.g., SS01_Login_Screen.png)
4. **Annotations**: Consider adding arrows or highlights to draw attention to key elements
5. **Resolution**: Capture at actual size or high DPI for print quality
6. **Consistency**: Use same system theme/appearance for all screenshots
7. **Data**: Use sample data that looks realistic and professional
8. **Privacy**: Use test accounts only, no real personal data

**Recommended Tools for Screenshots:**
- macOS: Shift+Cmd+4 (select area)
- Windows: Snipping Tool or Snip & Sketch
- Linux: Screenshot utility or Flameshot

**Screenshot Editing (Optional):**
- Add numbered callouts
- Highlight buttons with colored boxes
- Add arrows pointing to important fields
- Blur any sensitive information
- Resize consistently for document

---

**End of Document**
