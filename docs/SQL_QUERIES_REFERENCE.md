# SQL Queries Reference Guide
## Library Management System - Class XII Computer Science Project

**Student:** Jhanvi Shankar
**Roll No:** ASLSKLDK
**Academic Year:** 2024-2025

---

## Table of Contents
1. [Database Connection Queries](#database-connection-queries)
2. [User Authentication Queries](#user-authentication-queries)
3. [Member Management Queries](#member-management-queries)
4. [Book Management Queries](#book-management-queries)
5. [Transaction Queries](#transaction-queries)
6. [Search Queries](#search-queries)
7. [Report Queries](#report-queries)

---

## Database Connection Queries

### 1. Establish Database Connection
**File:** All files (login.py, admin.py, member.py, add_member.py, add_book.py)
**Purpose:** Connect to MySQL database using credentials from config.py

```python
conn = mysql.connector.connect(**db_config)
cur = conn.cursor()
```

**Explanation:**
- `**db_config` unpacks the dictionary containing host, user, password, database
- `cursor()` creates a cursor object to execute SQL queries
- Cursor is like a pointer that lets us interact with the database

---

## User Authentication Queries

### 2. Verify Login Credentials
**File:** login.py (line 18)
**Purpose:** Check if username and password match, and get user type and status

```sql
SELECT user_id, user_type, full_name, status
FROM users
WHERE username = %s AND password = %s
```

**Explanation:**
- Uses parameterized query with `%s` placeholders to prevent SQL injection
- Returns user_id (for session tracking), user_type (admin/member), full_name, and status (active/inactive)
- If no result found, login fails

**Example:**
```
Input: username='admin', password='admin123'
Output: (1, 'admin', 'Administrator', 'active')
```

---

## Member Management Queries

### 3. Check Duplicate Username
**File:** add_member.py (line 28)
**Purpose:** Prevent duplicate usernames when registering new members

```sql
SELECT username
FROM users
WHERE username = %s
```

**Explanation:**
- Simple SELECT to check if username already exists
- If `fetchone()` returns a result, username is taken
- Uses UNIQUE constraint on username column

---

### 4. Insert New User Account
**File:** add_member.py (line 35)
**Purpose:** Create new user account with login credentials

```sql
INSERT INTO users (username, password, full_name, user_type, status)
VALUES (%s, %s, %s, 'member', 'active')
```

**Explanation:**
- Inserts new record into users table
- user_type is hardcoded as 'member' (not admin)
- status defaults to 'active'
- `lastrowid` gives us the auto-generated user_id

---

### 5. Insert Member Details
**File:** add_member.py (line 40)
**Purpose:** Store additional member information

```sql
INSERT INTO members (user_id, name, address, email, phone)
VALUES (%s, %s, %s, %s, %s)
```

**Explanation:**
- Links to users table via user_id (foreign key)
- Stores extended profile information
- Address, email, phone are optional fields

---

### 6. Get Member ID from User ID
**File:** admin.py (line 225), member.py (line 18)
**Purpose:** Find member_id for a given user_id

```sql
SELECT member_id
FROM members
WHERE user_id = %s
```

**Explanation:**
- Converts user_id (from login) to member_id (for book transactions)
- One-to-one relationship between users and members

---

### 7. Get Member Username from Member ID
**File:** admin.py (line 89)
**Purpose:** Display member username in weekly report

```sql
SELECT username
FROM users u
JOIN members m ON u.user_id = m.user_id
WHERE m.member_id = %s
```

**Explanation:**
- Uses INNER JOIN to connect users and members tables
- Starts from member_id, navigates through user_id to get username
- Shows relationship between tables

---

## Book Management Queries

### 8. Check Duplicate Book
**File:** add_book.py (line 41)
**Purpose:** Prevent adding same book twice

```sql
SELECT title, author
FROM books
WHERE title = %s AND author = %s
LIMIT 1
```

**Explanation:**
- Checks if book with same title AND author exists
- LIMIT 1 for efficiency (we only need to know if it exists)
- Books are considered duplicates only if both title and author match

---

### 9. Insert New Book Copy
**File:** add_book.py (line 50)
**Purpose:** Add a single copy of a book to the catalog

```sql
INSERT INTO books (title, author, isbn, year, copy_number, book_status, record_status)
VALUES (%s, %s, %s, %s, %s, 'New', 'Active')
```

**Explanation:**
- Executed in a loop to add multiple copies
- book_status starts as 'New' (never issued before)
- record_status is 'Active' (not deleted)
- copy_number increments (1, 2, 3...) for each copy

---

### 10. Get Distinct Books (No Duplicates)
**File:** admin.py (line 119), member.py (line 39)
**Purpose:** Get unique books for catalog display

```sql
SELECT DISTINCT title, author, year, record_status
FROM books
WHERE title LIKE %s OR author LIKE %s OR year LIKE %s
```

**Explanation:**
- DISTINCT removes duplicate rows (multiple copies appear as one book)
- LIKE with % allows partial matching (e.g., "train" matches "Train to Pakistan")
- Searches across title, author, and year fields

---

### 11. Count Total Copies of a Book
**File:** admin.py (line 127)
**Purpose:** Show total number of copies in system

```sql
SELECT COUNT(*)
FROM books
WHERE title=%s AND author=%s AND record_status=%s
```

**Explanation:**
- COUNT(*) counts all matching rows
- Filtered by title, author, and record_status
- Returns a single number

---

### 12. Count Available Copies
**File:** admin.py (line 134), member.py (line 46)
**Purpose:** Show how many copies can be borrowed

```sql
SELECT COUNT(*)
FROM books
WHERE title=%s AND author=%s
  AND book_status IN ('Returned', 'New')
  AND record_status='Active'
```

**Explanation:**
- IN clause checks multiple values (New OR Returned)
- Only Active books (not Deleted)
- Available means not currently issued

---

### 13. Get All Copies of a Book (Admin View)
**File:** admin.py (line 212)
**Purpose:** Show detailed view of all copies

```sql
SELECT book_id, copy_number, book_status, issued_to_member_id, issue_date, record_status
FROM books
WHERE title=%s AND author=%s
```

**Explanation:**
- Returns all copies of a specific book
- Includes status, who has it, when issued
- Used in double-click popup window

---

### 14. Soft Delete Books
**File:** admin.py (line 279)
**Purpose:** Mark book as deleted without removing from database

```sql
UPDATE books
SET record_status='Deleted'
WHERE title=%s AND author=%s
```

**Explanation:**
- UPDATE changes existing records instead of deleting
- All copies of the book are marked deleted
- Data preserved for historical records and audit trail

---

### 15. Check if Book Has Issued Copies (Before Delete)
**File:** admin.py (line 269)
**Purpose:** Prevent deleting books that are currently with members

```sql
SELECT COUNT(*)
FROM books
WHERE title=%s AND author=%s AND book_status='Issued'
```

**Explanation:**
- Business rule: can't delete issued books
- COUNT returns 0 if no issued copies
- If > 0, show error and prevent deletion

---

## Book Transaction Queries

### 16. Issue Book to Member
**File:** admin.py (line 241)
**Purpose:** Mark a copy as issued and assign to member

```sql
UPDATE books
SET book_status='Issued', issued_to_member_id=%s, issue_date=%s
WHERE book_id=%s
```

**Explanation:**
- Changes single copy's status from New/Returned to Issued
- Records member_id of borrower
- Records issue_date for due date calculation

---

### 17. Find Available Copy to Issue
**File:** admin.py (line 236)
**Purpose:** Get first available copy of a book for issuing

```sql
SELECT book_id
FROM books
WHERE title=%s AND author=%s
  AND book_status IN ('Returned', 'New')
  AND record_status='Active'
LIMIT 1
```

**Explanation:**
- LIMIT 1 returns only first available copy
- System automatically picks which copy to issue
- Member doesn't choose specific copy number

---

### 18. Check Member's Current Book Count
**File:** admin.py (line 229)
**Purpose:** Enforce 3 books per member limit

```sql
SELECT COUNT(*)
FROM books
WHERE issued_to_member_id = %s AND book_status = 'Issued'
```

**Explanation:**
- Counts how many books member currently has
- If COUNT >= 3, prevent new issue
- Business rule enforcement through SQL

---

### 19. Return Book
**File:** admin.py (line 181)
**Purpose:** Mark book as returned and clear member info

```sql
UPDATE books
SET book_status='Returned', issued_to_member_id=NULL, issue_date=NULL
WHERE book_id=%s
```

**Explanation:**
- Changes status from Issued to Returned
- Sets member_id and issue_date to NULL (clears borrower info)
- Book becomes available again

---

### 20. Get Member's Borrowed Books
**File:** member.py (line 21)
**Purpose:** Show all books currently borrowed by logged-in member

```sql
SELECT book_id, title, author, year, issue_date
FROM books
WHERE issued_to_member_id=%s AND book_status='Issued'
```

**Explanation:**
- Filtered by member_id and status='Issued'
- Shows what member currently has
- Used in "My Borrowed Books" section

---

## Transaction Logging Queries

### 21. Insert Transaction Record (Add Book)
**File:** add_book.py (line 59)
**Purpose:** Log when a book is added to catalog

```sql
INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes)
VALUES (%s, NULL, %s, 'Add', %s)
```

**Explanation:**
- member_id is NULL (no member involved in Add action)
- admin_user_id records who added the book
- notes contains book details for reference

---

### 22. Insert Transaction Record (Issue)
**File:** admin.py (line 242)
**Purpose:** Log when a book is issued to member

```sql
INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes)
VALUES (%s, %s, %s, 'Issue', %s)
```

**Explanation:**
- Records book_id, member_id, and admin_id
- action = 'Issue'
- Creates audit trail of who borrowed what and when

---

### 23. Insert Transaction Record (Return)
**File:** admin.py (line 182)
**Purpose:** Log when a book is returned

```sql
INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes)
VALUES (%s, %s, %s, 'Return', %s)
```

**Explanation:**
- Records which member returned the book
- admin_user_id = who processed the return
- Completes the borrow-return cycle

---

### 24. Insert Transaction Record (Delete)
**File:** admin.py (line 283)
**Purpose:** Log when a book is deleted

```sql
INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes)
VALUES (%s, NULL, %s, 'Delete', %s)
```

**Explanation:**
- member_id is NULL (no member involved)
- Records which admin deleted the book
- Permanent record even after soft delete

---

## Report Queries

### 25. Weekly Report - Get Last 7 Days Transactions
**File:** admin.py (line 52)
**Purpose:** Show all library activity in past week

```sql
SELECT action, book_id, member_id, transaction_date, notes, admin_user_id
FROM transactions
WHERE transaction_date >= %s
ORDER BY transaction_date DESC
```

**Explanation:**
- Filters by date (transaction_date >= one week ago)
- ORDER BY DESC shows newest first
- Returns all columns needed for report display

---

### 26. Get Admin Username for Weekly Report
**File:** admin.py (line 75)
**Purpose:** Display admin who performed action in report

```sql
SELECT username
FROM users
WHERE user_id = %s
```

**Explanation:**
- Converts admin_user_id to username
- Used for Add, Delete, Return actions
- Shows accountability in reports

---

### 27. Get Member Info for Copy Display
**File:** admin.py (line 223)
**Purpose:** Show who currently has a book copy

```sql
SELECT name, username
FROM members m
JOIN users u ON m.user_id = u.user_id
WHERE member_id = %s
```

**Explanation:**
- JOIN combines members and users tables
- Returns both full name and username
- Displayed as "Priya Sharma (priya)"

---

## Key SQL Concepts Used

### 1. Parameterized Queries
```python
cur.execute("SELECT * FROM users WHERE username = %s", (username,))
```
- Prevents SQL injection attacks
- %s is placeholder, actual value passed separately
- MySQL connector automatically escapes special characters

### 2. JOIN Operations
```sql
SELECT u.username
FROM users u
JOIN members m ON u.user_id = m.user_id
```
- Combines related data from multiple tables
- ON clause specifies relationship
- u and m are table aliases for readability

### 3. Aggregate Functions
```sql
SELECT COUNT(*) FROM books WHERE title = 'xyz'
```
- COUNT(*) counts rows
- Returns single number
- Used for totals and availability checks

### 4. LIKE Operator
```sql
WHERE title LIKE '%train%'
```
- % is wildcard (matches any characters)
- Case-insensitive search
- '%train%' matches "Train to Pakistan"

### 5. IN Clause
```sql
WHERE book_status IN ('New', 'Returned')
```
- Checks if value matches any in list
- Shorthand for multiple OR conditions
- More readable than OR chains

### 6. DISTINCT Keyword
```sql
SELECT DISTINCT title, author FROM books
```
- Removes duplicate rows
- Shows each book once even if multiple copies exist
- Essential for catalog display

### 7. ORDER BY
```sql
ORDER BY transaction_date DESC
```
- Sorts results
- DESC = descending (newest first)
- ASC = ascending (default)

### 8. LIMIT Clause
```sql
LIMIT 1
```
- Restricts number of results
- Used when we only need one row
- Improves performance

---

## Common Query Patterns

### Pattern 1: Check if Record Exists
```python
cur.execute("SELECT * FROM table WHERE condition")
if cur.fetchone():
    # Record exists
else:
    # Record doesn't exist
```

### Pattern 2: Get Single Value
```python
cur.execute("SELECT COUNT(*) FROM table")
count = cur.fetchone()[0]  # [0] gets first column
```

### Pattern 3: Get Multiple Rows
```python
cur.execute("SELECT * FROM table")
rows = cur.fetchall()  # Returns list of tuples
for row in rows:
    print(row[0], row[1])  # Access by index
```

### Pattern 4: Insert and Get ID
```python
cur.execute("INSERT INTO table VALUES (%s)", (value,))
new_id = cur.lastrowid  # Auto-generated ID
```

### Pattern 5: Update Record
```python
cur.execute("UPDATE table SET column=%s WHERE id=%s", (new_value, record_id))
conn.commit()  # Must commit to save changes
```

---

## Database Best Practices Used

1. **Foreign Keys**: Link related tables (user_id, member_id, book_id)
2. **Transactions**: All changes committed together (success/failure)
3. **Soft Delete**: Mark as deleted, don't remove (record_status='Deleted')
4. **Audit Trail**: Log all actions in transactions table
5. **Parameterized Queries**: Prevent SQL injection
6. **Data Validation**: Check before insert/update (duplicates, limits)
7. **Meaningful Names**: Clear column and table names
8. **Auto Increment**: Primary keys generated automatically

---

## Tips for Viva Voce

1. **Understand the flow**: Follow a query from user action → Python code → SQL → Database → Result
2. **Know the difference**: SELECT (read), INSERT (create), UPDATE (modify), DELETE (remove)
3. **Explain JOIN**: How it combines users and members tables
4. **Transaction importance**: Why we log every action
5. **Security**: Why we use %s instead of string formatting
6. **Business rules**: How SQL enforces 3 book limit, duplicate prevention
7. **Performance**: Why LIMIT 1, DISTINCT, and indexes matter

---

**End of SQL Queries Reference**
