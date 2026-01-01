# Library Management System
## User Manual & Project Documentation

**Class XII Computer Science Project**
**Academic Year**: 2024-2025
**Student**: Jhanvi Shankar
**Class**: XII-B
**Roll No**: ASLSKLDK

---

## Table of Contents

1. [Index](#1-index)
2. [Acknowledgement](#2-acknowledgement)
3. [Case Study](#3-case-study)
4. [MySQL Table Structure](#4-mysql-table-structure)
5. [Algorithm](#5-algorithm)
6. [Flowchart](#6-flowchart)
7. [Program Code](#7-program-code)
8. [Sample Screenshots](#8-sample-screenshots)
9. [Limitations](#9-limitations)
10. [Scope for Improvement](#10-scope-for-improvement)
11. [Bibliography / References](#11-bibliography--references)

---

## 1. Index

### 1.1 Project Overview
- **Project Name**: Library Management System
- **Programming Language**: Python 3.7+
- **GUI Framework**: Tkinter
- **Database**: MySQL 8.0
- **Additional Libraries**: mysql-connector-python, Pillow (PIL)
- **Total Files**: 8 Python files, 8 image assets
- **Total Lines of Code**: ~1200 lines
- **Project Duration**: October 2024 - December 2024

### 1.2 Document Structure
This documentation is organized into 11 major sections covering:
- Case study and problem definition
- Database design with ERD
- Algorithms for core operations
- Flowcharts for main functions
- Complete program code
- Sample screenshots demonstrating features
- System limitations
- Future enhancement possibilities
- References and bibliography

### 1.3 Key Features Summary
- **Admin Features**: User management, Book catalog, Issue/Return, Reports, Overdue tracking
- **Member Features**: View borrowed books, Search catalog, Overdue indicators
- **Security**: Role-based access control
- **Data Integrity**: Soft delete, Transaction logging, Validation checks

---

## 2. Acknowledgement

I would like to express my sincere gratitude to all those who helped me complete this project successfully.

First and foremost, I am deeply grateful to my **Computer Science teacher** for their invaluable guidance, continuous support, and encouragement throughout the development of this Library Management System. Their expertise in Python programming and database management was instrumental in shaping this project.

I would like to thank my **school principal** for providing the necessary infrastructure and resources, including access to computer lab facilities and MySQL database software, which were essential for developing and testing this application.

I am thankful to my **parents** for their constant motivation and support during the project development phase, especially during the challenging debugging sessions.

I also acknowledge the contributions of my **classmates** who participated in user acceptance testing and provided valuable feedback that helped improve the system's usability and interface design.

Finally, I would like to thank the **Python Software Foundation** and **MySQL community** for developing such powerful open-source tools that made this project possible.

This project has been a great learning experience, enhancing my skills in:
- Object-oriented programming with Python
- GUI development using Tkinter
- Database design and SQL queries
- Software development lifecycle
- User interface/experience design

---

**Jhanvi Shankar**
Class XII-B
Roll No: ASLSKLDK

---

## 3. Case Study

### 3.1 Problem Definition

**Background:**
School and college libraries face significant challenges in managing their book inventory and member borrowing activities manually. Traditional paper-based systems are:
- Time-consuming and error-prone
- Difficult to track overdue books and defaulters
- Lack real-time availability information
- Cannot generate quick reports
- Prone to data loss and duplication

**Problem Statement:**
Design and develop a computerized Library Management System that can:
1. Maintain a digital catalog of books with multiple copies
2. Manage member registration and profiles
3. Track book issuing and returns with due dates
4. Prevent issuing books to members with overdue items
5. Generate reports on transactions and defaulters
6. Provide role-based access for administrators and members
7. Ensure data integrity and maintain audit trails

### 3.2 Proposed Solution

A desktop application built using Python and MySQL that provides:

**For Library Administrators:**
- Centralized dashboard with icon-enhanced interface
- Quick user registration (Admin/Member types)
- Efficient book catalog management (1-5 copies per book)
- Smart book issuing with automatic validation:
  - Check for overdue books (blocks issuing)
  - Enforce borrowing limit (3 books maximum)
  - Calculate due dates automatically (15 days)
- Simple return processing
- Soft delete functionality (preserve audit trail)
- Real-time reports:
  - Weekly transaction reports
  - Defaulters list with overdue days
  - Complete user directory

**For Library Members:**
- Personal dashboard showing borrowed books
- Visual overdue indicators (red highlighting)
- Warning legend for overdue items
- Searchable catalog of available books
- Due date tracking

**Technical Architecture:**
```
Presentation Layer (Tkinter GUI)
    ↓
Business Logic Layer (Python)
    ↓
Data Access Layer (mysql-connector)
    ↓
Database Layer (MySQL 8.0)
```

### 3.3 System Features

#### 3.3.1 User Management
- Dual user types: Admin and Member
- Unique username validation
- Password-protected access
- User type dropdown for easy selection
- Contact information storage (email, phone, address)
- Account creation timestamp tracking

#### 3.3.2 Book Catalog Management
- Multi-copy support (1-5 copies per book)
- Duplicate prevention (title + author check)
- Soft delete mechanism (preserves transaction history)
- Book status tracking: New, Issued, Returned, Deleted
- Record status tracking: Active, Deleted
- Copy number assignment for inventory control

#### 3.3.3 Issue/Return Process
- Member username-based issuing
- Automatic due date calculation (issue date + 15 days)
- Smart validation:
  1. **Priority 1**: Overdue book check (prevents borrowing)
  2. **Priority 2**: Borrowing limit check (max 3 books)
  3. **Priority 3**: Book availability check
- Transaction logging for all operations
- Real-time catalog updates

#### 3.3.4 Overdue Management
- Automatic overdue detection (current date > due date)
- Days overdue calculation
- Visual indicators for members (red highlighting)
- Defaulters list for administrators
- Issue prevention for defaulters

#### 3.3.5 Reporting System
- **Weekly Reports**: Last 7 days transaction history
- **Defaulters List**: All overdue books with member details
- **User Directory**: Complete list of all system users
- Date formatting: dd/mm/yyyy (Indian standard)
- Sortable and searchable data

#### 3.3.6 User Interface Enhancements
- Decorative icons (40x40 for headings, 50x50 for buttons)
- Right-aligned form labels
- Centered buttons
- Color-coded headers (Blue for Admin, Green for Member)
- 3x2 grid layout for admin dashboard (6 buttons)
- Graceful fallback if icons missing

### 3.4 System Benefits

**For Library Staff:**
- Reduced manual workload (80% time savings estimated)
- Eliminated paper-based record keeping
- Instant access to member and book information
- Quick identification of defaulters
- Automated due date tracking
- Error-free transaction recording

**For Library Members:**
- Self-service book search capability
- Clear visibility of borrowed books and due dates
- Visual alerts for overdue items
- Better understanding of borrowing policies
- Contact admin easily when needed

**For Library Management:**
- Complete audit trail of all operations
- Data-driven decision making
- Improved book utilization tracking
- Reduced book loss due to overdue prevention
- Scalable system for future growth

### 3.5 System Requirements

**Hardware Requirements:**
- Processor: Intel Core i3 or higher
- RAM: 4 GB minimum
- Storage: 100 MB free disk space
- Display: 800x600 minimum resolution
- Input: Keyboard and Mouse

**Software Requirements:**
- Operating System: Windows 10/11, macOS 10.14+, or Linux
- Python: 3.7 or higher
- MySQL: 8.0 or higher
- Python Libraries:
  - tkinter (included with Python)
  - mysql-connector-python 8.0+
  - Pillow (PIL) 9.0+

**Database Requirements:**
- MySQL Server running on localhost or network
- Database name: `library_db`
- User privileges: CREATE, SELECT, INSERT, UPDATE, DELETE
- Character set: utf8mb4
- Collation: utf8mb4_general_ci

### 3.6 Installation and Setup

**Step 1: Install Python Dependencies**
```bash
pip install -r requirements.txt
```

**Step 2: Configure Database Connection**
```bash
cp config_template.py config.py
# Edit config.py with your MySQL credentials
```

**Step 3: Initialize Database**
```bash
python3 setup_database_final.py
```

**Step 4: Launch Application**
```bash
python3 login.py
```

### 3.7 Default Test Accounts

| User Type | Username | Password | Purpose |
|-----------|----------|----------|---------|
| Admin | admin | admin123 | Primary administrator account |
| Admin | librarian | lib123 | Secondary administrator account |
| Member | priya | priya123 | Test member account 1 |
| Member | rahul | rahul123 | Test member account 2 |

---

## 4. MySQL Table Structure

### 4.1 Entity Relationship Diagram (ERD)

```
┌─────────────────────────┐
│        USERS            │
│─────────────────────────│
│ PK: user_id (INT)       │
│     username (VARCHAR)  │ UNIQUE
│     password (VARCHAR)  │
│     full_name (VARCHAR) │
│     user_type (VARCHAR) │ 'admin' or 'member'
│     status (VARCHAR)    │ 'active' or 'inactive'
│     created_date (TS)   │
└───────────┬─────────────┘
            │
            │ 1:1 (FK: user_id)
            │
            ▼
┌─────────────────────────┐         ┌─────────────────────────┐
│       MEMBERS           │         │        BOOKS            │
│─────────────────────────│         │─────────────────────────│
│ PK: member_id (INT)     │◄────────│ PK: book_id (INT)       │
│ FK: user_id (INT)       │   1:M   │     title (VARCHAR)     │
│     name (VARCHAR)      │         │     author (VARCHAR)    │
│     address (VARCHAR)   │         │     isbn (VARCHAR)      │
│     email (VARCHAR)     │         │     year (INT)          │
│     phone (VARCHAR)     │         │     copy_number (INT)   │
└───────────┬─────────────┘         │     book_status (VAR)   │
            │                       │     record_status (VAR) │
            │                       │ FK: issued_to_member_id │
            │                       │     issue_date (DATE)   │
            │                       │     created_date (TS)   │
            │                       └───────────┬─────────────┘
            │                                   │
            │         ┌─────────────────────────┘
            │         │
            │  1:M    │  1:M
            │         │
            └────┐    │
                 ▼    ▼
          ┌─────────────────────────┐
          │    TRANSACTIONS         │
          │─────────────────────────│
          │ PK: transaction_id      │
          │ FK: book_id (INT)       │
          │ FK: member_id (INT)     │
          │ FK: admin_user_id (INT) │
          │     action (VARCHAR)    │ 'Issue','Return','Add','Delete'
          │     transaction_date    │
          │     notes (VARCHAR)     │
          └─────────────────────────┘
                     ▲
                     │
                     │ 1:M (FK: admin_user_id)
                     │
          ┌──────────┴──────────┐
          │       USERS         │
          │    (as admin)       │
          └─────────────────────┘
```

### 4.2 Table Definitions

#### 4.2.1 Table: users

**Purpose**: Store login credentials and user information for both admins and members

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

**Field Descriptions:**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| user_id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique identifier for user |
| username | VARCHAR(50) | UNIQUE, NOT NULL | Login username |
| password | VARCHAR(50) | NOT NULL | Plain text password (educational purpose) |
| full_name | VARCHAR(100) | NOT NULL | User's full name |
| user_type | VARCHAR(20) | NOT NULL | 'admin' or 'member' |
| status | VARCHAR(20) | DEFAULT 'active' | 'active' or 'inactive' |
| created_date | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Account creation timestamp |

**Sample Data:**
```sql
INSERT INTO users VALUES
(1, 'admin', 'admin123', 'Administrator', 'admin', 'active', '2024-10-01 10:00:00'),
(2, 'librarian', 'lib123', 'Librarian Name', 'admin', 'active', '2024-10-01 10:05:00'),
(3, 'priya', 'priya123', 'Priya Sharma', 'member', 'active', '2024-10-02 11:30:00'),
(4, 'rahul', 'rahul123', 'Rahul Kumar', 'member', 'active', '2024-10-02 14:20:00');
```

#### 4.2.2 Table: members

**Purpose**: Store additional profile information for member-type users

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

**Field Descriptions:**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| member_id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique member identifier |
| user_id | INT | FOREIGN KEY → users(user_id) | Link to user account |
| name | VARCHAR(100) | NOT NULL | Member's full name |
| address | VARCHAR(200) | NULL allowed | Residential address |
| email | VARCHAR(100) | NULL allowed | Email address |
| phone | VARCHAR(15) | NULL allowed | Contact number |

**Relationship**: One-to-One with users table (only for user_type='member')

**Sample Data:**
```sql
INSERT INTO members VALUES
(1, 3, 'Priya Sharma', '123 MG Road, Delhi', 'priya@email.com', '9876543210'),
(2, 4, 'Rahul Kumar', '456 Park Street, Mumbai', 'rahul@email.com', '9123456780');
```

#### 4.2.3 Table: books

**Purpose**: Store book catalog with multiple copy support and tracking information

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

**Field Descriptions:**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| book_id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique book identifier |
| title | VARCHAR(200) | NOT NULL | Book title |
| author | VARCHAR(100) | NOT NULL | Book author |
| isbn | VARCHAR(20) | NOT NULL | ISBN number |
| year | INT | NOT NULL | Publication year |
| copy_number | INT | NOT NULL | Copy number (1, 2, 3...) |
| book_status | VARCHAR(20) | DEFAULT 'New' | 'New', 'Issued', 'Returned' |
| record_status | VARCHAR(20) | DEFAULT 'Active' | 'Active', 'Deleted' |
| issued_to_member_id | INT | FOREIGN KEY, NULL allowed | Currently issued to which member |
| issue_date | DATE | NULL allowed | Date when book was issued |
| created_date | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | When book was added |

**Business Rules:**
- Combination of (title, author, copy_number) should be unique
- book_status: 'New' (never issued), 'Issued' (currently out), 'Returned' (was issued, now available)
- record_status: 'Active' (visible), 'Deleted' (soft deleted, hidden from active view)
- issued_to_member_id is NULL when book is available
- issue_date is NULL when book is available

**Sample Data:**
```sql
INSERT INTO books VALUES
(1, 'Train to Pakistan', 'Khushwant Singh', '978-0143065883', 1956, 1, 'New', 'Active', NULL, NULL, '2024-10-03 09:00:00'),
(2, 'Train to Pakistan', 'Khushwant Singh', '978-0143065883', 1956, 2, 'Issued', 'Active', 1, '2024-12-01', '2024-10-03 09:00:00'),
(3, 'The God of Small Things', 'Arundhati Roy', '978-0006550686', 1997, 1, 'Returned', 'Active', NULL, NULL, '2024-10-03 09:05:00');
```

#### 4.2.4 Table: transactions

**Purpose**: Maintain complete audit trail of all library operations

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

**Field Descriptions:**

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| transaction_id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique transaction identifier |
| book_id | INT | FOREIGN KEY, NULL allowed | Which book |
| member_id | INT | FOREIGN KEY, NULL allowed | Which member (for Issue) |
| admin_user_id | INT | FOREIGN KEY, NULL allowed | Which admin performed action |
| action | VARCHAR(20) | NOT NULL | 'Issue', 'Return', 'Add', 'Delete' |
| transaction_date | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | When action occurred |
| notes | VARCHAR(200) | NULL allowed | Additional details (book title, etc.) |

**Action Types:**
- **'Issue'**: Book issued to member (member_id filled, admin_user_id filled)
- **'Return'**: Book returned by member (member_id filled, admin_user_id filled)
- **'Add'**: New book added to catalog (book_id filled, admin_user_id filled)
- **'Delete'**: Book soft-deleted (book_id filled, admin_user_id filled)

**Sample Data:**
```sql
INSERT INTO transactions VALUES
(1, 1, NULL, 1, 'Add', '2024-10-03 09:00:00', 'Train to Pakistan by Khushwant Singh (Copy 1)'),
(2, 2, 1, 1, 'Issue', '2024-12-01 10:30:00', 'Train to Pakistan by Khushwant Singh'),
(3, 3, 1, 1, 'Return', '2024-12-10 14:20:00', 'The God of Small Things by Arundhati Roy');
```

### 4.3 Relationships Summary

| From Table | To Table | Type | Foreign Key | Description |
|------------|----------|------|-------------|-------------|
| users | members | 1:1 | members.user_id | Each member has one login |
| members | books | 1:M | books.issued_to_member_id | Member can borrow multiple books |
| books | transactions | 1:M | transactions.book_id | Each book has transaction history |
| members | transactions | 1:M | transactions.member_id | Member's borrowing history |
| users | transactions | 1:M | transactions.admin_user_id | Admin's action history |

### 4.4 Database Constraints and Integrity

**Primary Keys:**
- All tables have auto-incrementing integer primary keys
- Ensures unique identification of each record

**Foreign Keys:**
- Maintain referential integrity between tables
- Prevent orphaned records
- Cascade rules: Default RESTRICT (prevents deletion of referenced records)

**Unique Constraints:**
- users.username (ensures no duplicate usernames)

**Not Null Constraints:**
- Critical fields that must always have values:
  - users: username, password, full_name, user_type
  - members: name
  - books: title, author, isbn, year, copy_number
  - transactions: action

**Default Values:**
- users.status: 'active'
- books.book_status: 'New'
- books.record_status: 'Active'
- All created_date and transaction_date: CURRENT_TIMESTAMP

---

## 5. Algorithm

### 5.1 Login Authentication Algorithm

```
Algorithm: authenticate_user(username, password)

Input: username (string), password (string)
Output: Success (redirect to dashboard) or Error message

Steps:
1. START
2. GET username and password from input fields
3. TRIM whitespace from both inputs
4. IF username is empty OR password is empty THEN
      DISPLAY "Enter username and password"
      RETURN
5. CONNECT to database
6. EXECUTE query: "SELECT user_id, full_name, user_type, status
                    FROM users
                    WHERE username = ? AND password = ?"
7. FETCH result
8. CLOSE database connection
9. IF result is NULL THEN
      DISPLAY "Invalid username or password"
      RETURN
10. IF result.status != 'active' THEN
       DISPLAY "Account is inactive. Please contact administrator."
       RETURN
11. EXTRACT user_id, user_name, user_type from result
12. DISPLAY "Welcome, {user_name}!"
13. CLOSE login window
14. IF user_type == 'admin' THEN
       OPEN admin.py with user_id parameter
    ELSE
       OPEN member.py with user_id parameter
15. END
```

**Time Complexity**: O(1) - Single database query
**Space Complexity**: O(1) - Fixed memory usage

---

### 5.2 Add Book Algorithm

```
Algorithm: add_book(title, author, isbn, year, copies)

Input: title (string), author (string), isbn (string), year (int), copies (int)
Output: Success message or Error message

Steps:
1. START
2. GET all form field values and TRIM whitespace
3. IF any field is empty THEN
      DISPLAY "All fields are required!"
      RETURN
4. TRY to convert year and copies to integers
   CATCH ValueError:
      DISPLAY "Year and copies must be valid numbers"
      RETURN
5. IF copies < 1 THEN
      DISPLAY "Number of copies must be at least 1"
      RETURN
6. IF copies > 5 THEN
      DISPLAY "Number of copies cannot be more than 5"
      RETURN
7. CONNECT to database
8. EXECUTE query: "SELECT title, author FROM books
                    WHERE title = ? AND author = ? LIMIT 1"
9. IF duplicate found THEN
      DISPLAY "Book '{title}' by {author} already exists in the library!"
      CLOSE connection
      RETURN
10. FOR i = 1 TO copies DO
       INSERT INTO books (title, author, isbn, year, copy_number,
                          book_status, record_status)
       VALUES (title, author, isbn, year, i, 'New', 'Active')
       GET last_insert_id as book_id
       INSERT INTO transactions (book_id, admin_user_id, action, notes)
       VALUES (book_id, current_admin_id, 'Add',
               '{title} by {author} (Copy {i})')
    END FOR
11. COMMIT transaction
12. CLOSE connection
13. DISPLAY "{copies} cop{'y' if copies==1 else 'ies'} of '{title}' added successfully!"
14. CLEAR all form fields
15. END
```

**Time Complexity**: O(n) where n = number of copies (max 5, so effectively O(1))
**Space Complexity**: O(1)

---

### 5.3 Issue Book Algorithm with Overdue Prevention

```
Algorithm: issue_book(title, author, member_username)

Input: title (string), author (string), member_username (string)
Output: Success with due date or Error message

Steps:
1. START
2. IF member_username is empty THEN
      DISPLAY "Please enter a member username"
      RETURN
3. CONNECT to database
4. CHECK if book is deleted:
   EXECUTE "SELECT record_status FROM books
            WHERE title=? AND author=? LIMIT 1"
   IF record_status == 'Deleted' THEN
      DISPLAY "Cannot issue deleted books"
      CLOSE connection
      RETURN
5. CHECK available copies:
   COUNT available = "SELECT COUNT(*) FROM books
                      WHERE title=? AND author=?
                      AND book_status IN ('New', 'Returned')
                      AND record_status='Active'"
   IF available == 0 THEN
      DISPLAY "No copies available"
      CLOSE connection
      RETURN
6. VALIDATE member:
   EXECUTE "SELECT user_id FROM users
            WHERE username=? AND user_type='member'"
   IF user not found THEN
      DISPLAY "Username not found"
      CLOSE connection
      RETURN
7. GET member_id:
   EXECUTE "SELECT member_id FROM members WHERE user_id=?"
   IF member not found THEN
      DISPLAY "Member not found"
      CLOSE connection
      RETURN
8. **PRIORITY CHECK 1 - OVERDUE BOOKS**:
   CALL get_overdue_books(member_id)
   IF overdue_books list is NOT empty THEN
      FORMAT overdue_list = "\n".join(overdue_books)
      DISPLAY "Cannot issue book to '{member_username}'.
               Member has overdue books:
               {overdue_list}
               Please return overdue books first."
      CLOSE connection
      RETURN
9. **PRIORITY CHECK 2 - BORROWING LIMIT**:
   COUNT current_books = "SELECT COUNT(*) FROM books
                          WHERE issued_to_member_id=?
                          AND book_status='Issued'"
   IF current_books >= 3 THEN
      DISPLAY "Member '{member_username}' already has 3 books issued.
               Maximum borrowing limit reached."
      CLOSE connection
      RETURN
10. FIND available book:
    EXECUTE "SELECT book_id FROM books
             WHERE title=? AND author=?
             AND book_status IN ('New', 'Returned')
             AND record_status='Active' LIMIT 1"
    GET book_id
11. SET issue_date = current_date
12. UPDATE books SET book_status='Issued',
                     issued_to_member_id=member_id,
                     issue_date=issue_date
    WHERE book_id=book_id
13. INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes)
    VALUES (book_id, member_id, current_admin_id, 'Issue',
            '{title} by {author}')
14. COMMIT transaction
15. CALCULATE due_date = issue_date + 15 days
16. DISPLAY "Book issued!
             Issue: {issue_date in dd/mm/yyyy}
             Due: {due_date in dd/mm/yyyy}"
17. REFRESH catalog display
18. CLOSE connection
19. END

Helper Function: get_overdue_books(member_id)
Input: member_id (int)
Output: List of overdue book descriptions

Steps:
1. GET today = current_date
2. EXECUTE "SELECT title, author, issue_date FROM books
            WHERE issued_to_member_id=? AND book_status='Issued'"
3. INITIALIZE overdue_books = empty list
4. FOR each issued_book DO
      CALCULATE due_date = issue_date + 15 days
      IF due_date < today THEN
         CALCULATE days_overdue = (today - due_date).days
         ADD "{title} by {author} ({days_overdue} days overdue)" to overdue_books
   END FOR
5. RETURN overdue_books
```

**Time Complexity**: O(m) where m = number of books issued to member (max 3)
**Space Complexity**: O(m)

**Key Design Decision**: Overdue check comes BEFORE borrowing limit check because having overdue books is a more critical violation of library policy.

---

### 5.4 Return Book Algorithm

```
Algorithm: return_book(book_id)

Input: book_id (int)
Output: Success message or Error message

Steps:
1. START
2. GET book status from selected row
3. IF book_status != 'Issued' THEN
      DISPLAY "This copy is not issued"
      RETURN
4. CONNECT to database
5. GET member_id:
   EXECUTE "SELECT issued_to_member_id FROM books WHERE book_id=?"
6. UPDATE books SET book_status='Returned',
                    issued_to_member_id=NULL,
                    issue_date=NULL
   WHERE book_id=book_id
7. INSERT INTO transactions (book_id, member_id, admin_user_id, action, notes)
   VALUES (book_id, member_id, current_admin_id, 'Return',
           '{title} by {author}')
8. COMMIT transaction
9. CLOSE connection
10. DISPLAY "Book returned!"
11. REFRESH both copies list and main catalog
12. END
```

**Time Complexity**: O(1)
**Space Complexity**: O(1)

---

### 5.5 Soft Delete Book Algorithm

```
Algorithm: delete_book(title, author)

Input: title (string), author (string)
Output: Success message or Error message

Steps:
1. START
2. CONNECT to database
3. CHECK if already deleted:
   COUNT deleted = "SELECT COUNT(*) FROM books
                    WHERE title=? AND author=?
                    AND record_status='Deleted'"
   COUNT total = "SELECT COUNT(*) FROM books
                  WHERE title=? AND author=?"
   IF deleted > 0 AND deleted == total THEN
      DISPLAY "Cannot delete '{title}' by {author}.
               This book is already deleted."
      CLOSE connection
      RETURN
4. CHECK if any copy is issued:
   COUNT issued = "SELECT COUNT(*) FROM books
                   WHERE title=? AND author=?
                   AND book_status='Issued'"
   IF issued > 0 THEN
      DISPLAY "Cannot delete '{title}' by {author}.
               {issued} cop{'y is' if issued==1 else 'ies are'} currently issued.
               Please return all copies before deleting."
      CLOSE connection
      RETURN
5. CONFIRM deletion:
   ASK user "Delete '{title}' by {author}?
             All copies will be marked deleted."
   IF user cancels THEN
      RETURN
6. UPDATE books SET record_status='Deleted'
   WHERE title=? AND author=?
7. GET one book_id:
   EXECUTE "SELECT book_id FROM books
            WHERE title=? AND author=? LIMIT 1"
8. INSERT INTO transactions (book_id, admin_user_id, action, notes)
   VALUES (book_id, current_admin_id, 'Delete', '{title} by {author}')
9. COMMIT transaction
10. CLOSE connection
11. DISPLAY "Book deleted!"
12. REFRESH catalog
13. END
```

**Time Complexity**: O(k) where k = total copies of the book
**Space Complexity**: O(1)

**Important**: This is a "soft delete" - records remain in database with record_status='Deleted' to preserve transaction history and data integrity.

---

### 5.6 Generate Defaulters List Algorithm

```
Algorithm: generate_defaulters_list()

Input: None
Output: Display list of members with overdue books

Steps:
1. START
2. CONNECT to database
3. GET today = current_date
4. EXECUTE query: "SELECT b.title, b.author, b.issue_date,
                          m.name, m.email, m.phone, b.book_id
                   FROM books b
                   JOIN members m ON b.issued_to_member_id = m.member_id
                   WHERE b.book_status = 'Issued'
                   AND b.issue_date IS NOT NULL"
5. INITIALIZE defaulters_found = false
6. FOR each issued_book DO
      CALCULATE due_date = issue_date + 15 days
      IF due_date < today THEN
         CALCULATE days_overdue = (today - due_date).days
         FORMAT due_date_str = due_date in dd/mm/yyyy format
         INSERT row into display table:
            (member_name, email or 'N/A', phone or 'N/A',
             title, author, due_date_str, days_overdue)
         SET defaulters_found = true
   END FOR
7. IF NOT defaulters_found THEN
      DISPLAY "No overdue books found!" (in green)
8. CLOSE connection
9. END
```

**Time Complexity**: O(n) where n = number of issued books
**Space Complexity**: O(d) where d = number of defaulters

---

## 6. Flowchart

### 6.1 Login Process Flowchart

```
         START
           ↓
    [Get username, password]
           ↓
    <username or password empty?>
       Yes ↓         No →
    [Error: Enter]      ↓
    [credentials ]   [Connect to DB]
         ↓              ↓
       STOP        [Query users table]
                       ↓
                  <User found?>
              No ↓         Yes →
           [Error:]          ↓
           [Invalid]   <Status active?>
           [username]    No ↓    Yes →
           [password]   [Error:]    ↓
                ↓       [Inactive] [Success:]
              STOP      [account]  [Welcome!]
                           ↓          ↓
                         STOP    <user_type?>
                                   ↙   ↘
                              admin    member
                                ↓        ↓
                         [Open admin] [Open member]
                         [dashboard]  [dashboard]
                                ↓        ↓
                              STOP     STOP
```

---

### 6.2 Issue Book Process Flowchart (with Overdue Prevention)

```
                        START
                          ↓
                  [Get book details]
                  [Get member username]
                          ↓
                   <username empty?>
                   Yes ↓        No →
                [Error:]           ↓
                [Enter]      [Connect to DB]
                [username]         ↓
                    ↓         [Check if book]
                  STOP        [is deleted]
                                  ↓
                          <Book deleted?>
                         Yes ↓       No →
                      [Error:]          ↓
                      [Cannot]    [Count available]
                      [issue]     [copies]
                      [deleted]         ↓
                          ↓       <Available > 0?>
                        STOP      No ↓      Yes →
                               [Error:]        ↓
                               [No]      [Validate member]
                               [copies]  [username & type]
                                  ↓            ↓
                                STOP    <Member valid?>
                                        No ↓      Yes →
                                     [Error:]        ↓
                                     [Member]   [Get member_id]
                                     [not found]     ↓
                                        ↓       **[Check overdue]**
                                      STOP      **[books]**
                                                    ↓
                                           **<Has overdue?>**
                                         **Yes ↓      No →**
                                      **[Error:]**      ↓
                                      **[Cannot]**  [Count current]
                                      **[issue,]**  [issued books]
                                      **[has]**          ↓
                                      **[overdue]** <Count >= 3?>
                                          ↓        Yes ↓    No →
                                        STOP    [Error:]      ↓
                                                [Max 3]  [Find available]
                                                [books]  [book copy]
                                                   ↓          ↓
                                                 STOP    [UPDATE books]
                                                         [SET Issued]
                                                              ↓
                                                         [INSERT into]
                                                         [transactions]
                                                              ↓
                                                         [Calculate]
                                                         [due date = ]
                                                         [today + 15]
                                                              ↓
                                                         [Success:]
                                                         [Book issued!]
                                                         [Show dates]
                                                              ↓
                                                         [Refresh catalog]
                                                              ↓
                                                            STOP
```

**Key Decision Points:**
1. Username validation
2. Book deletion check
3. Availability check
4. Member validation
5. **Overdue check (PRIORITY 1)**
6. **Borrowing limit check (PRIORITY 2)**

---

## 7. Program Code

### 7.1 Main Program Files

This section contains the core Python code for the Library Management System. Due to space constraints in the manual, key code segments are shown. Full code is available in the project files.

#### 7.1.1 login.py - Login Screen

**Purpose**: Authentication and role-based redirection

**Key Functions**:
- `login()`: Validates credentials and opens appropriate dashboard

**Code Snippet**:
```python
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess
import sys
from PIL import Image, ImageTk
from config import db_config

def login(event=None):
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        messagebox.showerror("Error", "Enter username and password")
        return

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT user_id, full_name, user_type, status FROM users "
        "WHERE username=%s AND password=%s",
        (username, password)
    )
    result = cursor.fetchone()
    conn.close()

    if result:
        if result[3] == 'active':
            user_id = result[0]
            user_name = result[1]
            user_type = result[2]

            messagebox.showinfo("Success", f"Welcome, {user_name}!")
            root.destroy()

            if user_type == 'admin':
                subprocess.Popen([sys.executable, 'admin.py', str(user_id)])
            else:
                subprocess.Popen([sys.executable, 'member.py', str(user_id)])
        else:
            messagebox.showerror("Error",
                "Account is inactive. Please contact administrator.")
    else:
        messagebox.showerror("Error", "Invalid username or password")
```

**File Statistics**:
- Lines: 92
- Functions: 1 (login)
- GUI Elements: Background image, Entry fields, Button
- Security: Plain text passwords (educational purpose only)

---

#### 7.1.2 admin.py - Admin Dashboard (Partial Code)

**Purpose**: Main control panel for administrators

**Key Functions**:
- `get_overdue_books(member_id, cur)`: Helper to check overdue books
- `create_list_window(title, size, columns, widths)`: Helper for report windows
- `issue_book()`: Issue book with validation
- `delete_book()`: Soft delete with validation
- `defaulters_list()`: Generate overdue report
- `view_users()`: Display all users

**Code Snippet - Overdue Prevention Logic**:
```python
def get_overdue_books(member_id, cur):
    """Helper function to get list of overdue books for a member"""
    today = datetime.now().date()
    cur.execute(
        "SELECT title, author, issue_date FROM books "
        "WHERE issued_to_member_id = %s AND book_status = 'Issued'",
        (member_id,)
    )
    issued_books = cur.fetchall()
    overdue_books = []
    for book in issued_books:
        due_date = book[2] + timedelta(days=15)
        if due_date < today:
            days_overdue = (today - due_date).days
            overdue_books.append(
                f"{book[0]} by {book[1]} ({days_overdue} days overdue)"
            )
    return overdue_books

def issue_book():
    # ... validation code ...

    # PRIORITY CHECK 1 - Overdue books (must come first)
    overdue_books = get_overdue_books(member[0], cur)
    if overdue_books:
        conn.close()
        overdue_list = "\n".join(overdue_books)
        messagebox.showerror("Error",
            f"Cannot issue book to '{member_username}'.\n\n"
            f"Member has overdue books:\n{overdue_list}\n\n"
            f"Please return overdue books first.")
        return

    # PRIORITY CHECK 2 - Borrowing limit
    cur.execute(
        "SELECT COUNT(*) FROM books "
        "WHERE issued_to_member_id = %s AND book_status = 'Issued'",
        (member[0],)
    )
    current_books = cur.fetchone()[0]
    if current_books >= 3:
        conn.close()
        messagebox.showerror("Error",
            f"Member '{member_username}' already has 3 books issued.\n"
            f"Maximum borrowing limit reached.")
        return

    # Proceed with issuing...
```

**File Statistics**:
- Lines: 556
- Functions: 10+
- Helper Functions: 2 (optimization)
- GUI Elements: 6 buttons, Multiple windows
- Code Reduction: ~40 lines saved through helper functions

---

#### 7.1.3 member.py - Member Dashboard (Partial Code)

**Purpose**: Member portal with overdue indicators

**Key Functions**:
- `refresh_borrowed()`: Display borrowed books with red highlighting
- `search_books()`: Search available books

**Code Snippet - Overdue Highlighting Logic**:
```python
def refresh_borrowed():
    for row in borrowed_tree.get_children():
        borrowed_tree.delete(row)

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT member_id FROM members WHERE user_id=%s", (user_id,))
    member = cur.fetchone()

    has_overdue = False
    if member:
        cur.execute(
            "SELECT book_id, title, author, year, issue_date FROM books "
            "WHERE issued_to_member_id=%s AND book_status='Issued'",
            (member[0],)
        )
        today = datetime.now().date()

        for book in cur.fetchall():
            issue_date_str = 'N/A'
            due_date_str = 'N/A'
            is_overdue = False

            if book[4]:
                issue_date_str = book[4].strftime('%d/%m/%Y')
                due_date = book[4] + timedelta(days=15)
                due_date_str = due_date.strftime('%d/%m/%Y')

                # Check if overdue
                if due_date < today:
                    is_overdue = True
                    has_overdue = True

            # Insert row and tag if overdue
            item_id = borrowed_tree.insert('', tk.END, values=(
                book[0], book[1], book[2], book[3],
                issue_date_str, due_date_str
            ))
            if is_overdue:
                borrowed_tree.item(item_id, tags=('overdue',))

    # Configure tag for red background
    borrowed_tree.tag_configure('overdue', background='#ffcccc')

    # Show/hide warning legend
    if has_overdue:
        overdue_legend.pack(pady=5)
    else:
        overdue_legend.pack_forget()

    conn.close()
```

**File Statistics**:
- Lines: 155
- Functions: 2
- GUI Elements: Treeview with tags, Dynamic legend
- Visual Enhancement: Conditional red highlighting

---

#### 7.1.4 add_member.py - Add User Form

**Purpose**: Create new Admin or Member accounts

**Key Features**:
- User Type dropdown (Member/Admin)
- Right-aligned labels
- Conditional member profile creation

**Code Snippet**:
```python
def save():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    name = name_entry.get().strip()
    user_type = user_type_var.get()
    address = address_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()

    if not username or not password or not name:
        messagebox.showerror("Error",
            "Username, Password and Full Name are required fields")
        return

    try:
        conn = mysql.connector.connect(**db_config)
        cur = conn.cursor()

        # Check duplicate username
        cur.execute("SELECT username FROM users WHERE username = %s",
                    (username,))
        if cur.fetchone():
            messagebox.showerror("Error",
                f"Username '{username}' already exists!\n"
                f"Please choose a different username.")
            conn.close()
            return

        # Insert into users table
        cur.execute(
            "INSERT INTO users (username, password, full_name, user_type, status) "
            "VALUES (%s, %s, %s, %s, 'active')",
            (username, password, name, user_type.lower())
        )
        user_id = cur.lastrowid

        # Insert into members table (only if user_type is member)
        if user_type.lower() == 'member':
            cur.execute(
                "INSERT INTO members (user_id, name, address, email, phone) "
                "VALUES (%s, %s, %s, %s, %s)",
                (user_id, name, address, email, phone)
            )
            member_id = cur.lastrowid
            success_msg = f"Member added successfully!\nMember ID: {member_id}"
        else:
            success_msg = f"Admin user '{username}' added successfully!"

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", success_msg)
        reset()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add user:\n{e}")
```

**File Statistics**:
- Lines: 115
- Functions: 2 (save, reset)
- UI Enhancement: Right-aligned labels, Centered buttons
- Validation: Required fields, Duplicate check

---

#### 7.1.5 add_book.py - Add Book Form

**Purpose**: Add books to catalog (1-5 copies)

**Key Validation**:
- All fields required
- Year and copies must be integers
- Copies range: 1-5
- Duplicate prevention (title + author)

**Code Snippet - Validation Logic**:
```python
def save():
    title = title_entry.get().strip()
    author = author_entry.get().strip()
    isbn = isbn_entry.get().strip()
    year = year_entry.get().strip()
    copies = copies_entry.get().strip()

    if not all([title, author, isbn, year, copies]):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        year = int(year)
        copies = int(copies)
        if copies < 1:
            messagebox.showerror("Error",
                "Number of copies must be at least 1")
            return
        if copies > 5:
            messagebox.showerror("Error",
                "Number of copies cannot be more than 5")
            return
    except ValueError:
        messagebox.showerror("Error",
            "Year and copies must be valid numbers")
        return

    try:
        conn = mysql.connector.connect(**db_config)
        cur = conn.cursor()

        # Check duplicate
        cur.execute(
            "SELECT title, author FROM books "
            "WHERE title = %s AND author = %s LIMIT 1",
            (title, author)
        )
        existing_book = cur.fetchone()
        if existing_book:
            messagebox.showerror("Error",
                f"Book '{title}' by {author} already exists in the library!\n"
                f"Use a different title or check existing copies.")
            conn.close()
            return

        # Insert each copy
        for i in range(1, copies + 1):
            cur.execute(
                "INSERT INTO books "
                "(title, author, isbn, year, copy_number, book_status, record_status) "
                "VALUES (%s, %s, %s, %s, %s, 'New', 'Active')",
                (title, author, isbn, year, i)
            )
            book_id = cur.lastrowid

            # Log transaction
            cur.execute(
                "INSERT INTO transactions "
                "(book_id, member_id, admin_user_id, action, notes) "
                "VALUES (%s, NULL, %s, 'Add', %s)",
                (book_id, admin_user_id, f"{title} by {author} (Copy {i})")
            )

        conn.commit()
        conn.close()

        messagebox.showinfo("Success",
            f"{copies} cop{'y' if copies == 1 else 'ies'} of '{title}' "
            f"added successfully!")
        reset()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add book:\n{e}")
```

**File Statistics**:
- Lines: 117
- Functions: 2 (save, reset)
- Validation: 5 checks
- Transaction Logging: Yes

---

### 7.2 Configuration Files

#### 7.2.1 config_template.py

```python
# Database configuration template
# Copy this file to config.py and update with your MySQL credentials

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'YOUR_MYSQL_PASSWORD_HERE',
    'database': 'library_db'
}
```

#### 7.2.2 requirements.txt

```
mysql-connector-python==8.0.33
Pillow==9.5.0
```

---

### 7.3 Database Setup Script

#### 7.3.1 setup_database_final.py (Partial)

**Purpose**: Create database and populate with initial data

```python
import mysql.connector
from config import db_config

# Connect to MySQL (without specifying database)
conn = mysql.connector.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password']
)
cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS library_db")
cursor.execute("USE library_db")

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    user_type VARCHAR(20) NOT NULL,
    status VARCHAR(20) DEFAULT 'active',
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Create members table
cursor.execute("""
CREATE TABLE IF NOT EXISTS members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(200),
    email VARCHAR(100),
    phone VARCHAR(15),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""")

# Create books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
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
)
""")

# Create transactions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
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
)
""")

# Insert default users
# (Code for inserting admin, librarian, priya, rahul...)

conn.commit()
print("Database setup completed successfully!")
conn.close()
```

---

## 8. Sample Screenshots

### 8.1 Login Screen

**[SCREENSHOT 1: Login Screen]**

*Description of screenshot:*
- Library background image (800x600 pixels)
- Centered white login box
- Username and Password input fields
- Login button
- Title: "Library Management System"
- Clean and professional interface

---

### 8.2 Admin Dashboard

**[SCREENSHOT 2: Admin Dashboard]**

*Description of screenshot:*
- Blue header with admin portal icon (40x40) next to "Admin Dashboard" title
- Logout button positioned in top-right corner
- 6 buttons arranged in 3x2 grid layout:
  - Row 1: Add Member | Add Book | View Users
  - Row 2: Search Catalog | Weekly Reports | Defaulters List
- Each button displays a 50x50 icon above the button text
- Professional and organized layout

---

### 8.3 Member Dashboard

**[SCREENSHOT 3: Member Portal]**

*Description of screenshot:*
- Green header with member portal icon (40x40) next to "Member Portal" title
- Logout button in top-right corner
- Two main sections:
  - **My Borrowed Books** (top section): Shows books currently borrowed with ID, Title, Author, Year, Issue Date, and Due Date
  - **Search Available Books** (bottom section): Allows members to search the catalog
- Note at bottom: "Contact admin to issue books"
- Clean member-focused interface

---

### 8.4 Add Member Form

**[SCREENSHOT 4: Add User Form]**

*Description of screenshot:*
- Form title: "Add User"
- Right-aligned labels (15 characters wide)
- Form fields:
  - Username: * (required)
  - Password: * (required, masked input)
  - Full Name: * (required)
  - User Type: Dropdown with "Member" and "Admin" options (default: Member)
  - Address: (optional)
  - Email: (optional)
  - Phone: (optional)
- Centered Save and Reset buttons
- Professional form layout with clear field labels

---

### 8.5 Add Book Form

**[SCREENSHOT 5: Add Book Form]**

*Description of screenshot:*
- Form title: "Add Book"
- Right-aligned labels (20 characters wide)
- All fields marked with asterisk (*) indicating required:
  - Book Title: *
  - Author: *
  - ISBN Number: *
  - Publication Year: *
  - Number of Copies: * (accepts 1-5)
- Centered Save and Reset buttons
- Clean and organized book entry interface

---

## 9. Limitations

### 9.1 Security Limitations

**1. Password Storage**
- **Issue**: Passwords stored in plain text in database
- **Risk**: Database breach would expose all passwords
- **Educational Note**: In production systems, passwords should be hashed using bcrypt, scrypt, or Argon2

**2. No Session Management**
- **Issue**: User credentials not validated beyond login
- **Risk**: If application left open, anyone can access
- **Impact**: No timeout or auto-logout feature

**3. SQL Injection Vulnerability (Mitigated)**
- **Status**: Currently using parameterized queries (safe)
- **Note**: Direct string concatenation in SQL would be vulnerable
- **Current Protection**: mysql-connector-python with placeholders

**4. No Role-Based Permissions**
- **Issue**: All admins have equal privileges
- **Missing**: Super admin, librarian roles with different access levels
- **Impact**: Cannot restrict sensitive operations to specific admins

### 9.2 Functional Limitations

**1. Book Copy Limit**
- **Restriction**: Maximum 5 copies per book
- **Workaround**: Add books in multiple batches
- **Reason**: UI design and validation logic constraint

**2. Borrowing Limit**
- **Fixed**: Maximum 3 books per member
- **Hardcoded**: Not configurable without code changes
- **Impact**: Cannot adjust for different member types (student/teacher)

**3. Due Date Period**
- **Fixed**: Exactly 15 days from issue date
- **Hardcoded**: Not configurable
- **Missing**: Different periods for different book types (reference, fiction)

**4. No Fine Calculation**
- **Missing**: Automatic fine calculation for overdue books
- **Impact**: Manual fine tracking required
- **Enhancement**: Could add per-day fine rate

**5. No Book Reservation**
- **Missing**: Cannot reserve books that are currently issued
- **Impact**: Members must keep checking availability
- **Workaround**: None available

**6. No Renewal Option**
- **Missing**: Cannot extend due date for issued books
- **Workaround**: Return and re-issue (if no one waiting)
- **Impact**: Inconvenient for members

**7. Single Database Server**
- **Limitation**: Requires MySQL on localhost
- **Missing**: Network database support configuration
- **Impact**: Cannot use centralized database server easily

### 9.3 Data Limitations

**1. No Book Categories/Genres**
- **Missing**: Classification system (Fiction, Non-Fiction, Reference, etc.)
- **Impact**: Cannot filter or search by category
- **Enhancement**: Add category table and relationship

**2. Limited Book Information**
- **Missing**: Publisher, edition, language, page count, summary
- **Impact**: Basic catalog only
- **Current**: Only title, author, ISBN, year

**3. Limited Member Information**
- **Missing**: Member type (student/teacher), class/department, membership date
- **Impact**: Cannot differentiate member privileges
- **Current**: Only basic contact information

**4. No Publisher Management**
- **Missing**: Publisher database and relationships
- **Impact**: Cannot track books by publisher
- **Enhancement**: Add publisher table

### 9.4 Reporting Limitations

**1. Limited Report Types**
- **Available**: Only weekly transactions and defaulters list
- **Missing**:
  - Monthly/yearly reports
  - Most borrowed books
  - Most active members
  - Book utilization statistics
  - Genre-wise reports

**2. No Export Functionality**
- **Missing**: Cannot export reports to PDF, Excel, or CSV
- **Impact**: Manual data copying required for external use
- **Workaround**: None available

**3. No Charts/Graphs**
- **Missing**: Visual representation of data
- **Impact**: Difficult to spot trends
- **Enhancement**: Add matplotlib for charts

**4. Fixed Date Range for Weekly Report**
- **Limitation**: Only last 7 days
- **Missing**: Custom date range selection
- **Impact**: Cannot view specific historical periods

### 9.5 User Interface Limitations

**1. No Search in Member Portal**
- **Missing**: Member cannot search their own transaction history
- **Impact**: Cannot check past borrowings
- **Current**: Only current borrowed books visible

**2. Fixed Window Sizes**
- **Issue**: Windows not resizable
- **Impact**: On very small screens, content may be cramped
- **Current**: Fixed at 800x600 or specific sizes

**3. No Sorting Capability**
- **Missing**: Cannot sort table columns
- **Impact**: Data shown in default order only
- **Enhancement**: Add column header click sorting

**4. No Advanced Search**
- **Missing**: Search by ISBN, year range, publication date
- **Current**: Only basic text search in title/author
- **Impact**: Finding books may be difficult in large catalogs

**5. Single Window Restriction**
- **Behavior**: Opening same window twice prevented
- **Impact**: Cannot have multiple catalog windows open
- **Reason**: Prevents data inconsistency

### 9.6 Performance Limitations

**1. No Pagination**
- **Issue**: All records loaded at once in tables
- **Impact**: Slow performance with thousands of books
- **Current**: Acceptable for small-medium libraries (< 1000 books)

**2. No Caching**
- **Issue**: Database queried every time
- **Impact**: Slight delay on repeated operations
- **Enhancement**: Implement result caching

**3. No Indexing Strategy**
- **Missing**: Database indexes on frequently searched fields
- **Impact**: Slower searches as database grows
- **Enhancement**: Add indexes on title, author, username

### 9.7 System Limitations

**1. Desktop Application Only**
- **Platform**: Requires Python and MySQL installed locally
- **Missing**: Web-based interface, mobile app
- **Impact**: Cannot access remotely

**2. Single User Sessions**
- **Issue**: Multiple admins can work simultaneously but no collaboration features
- **Missing**: Multi-user transaction locking
- **Risk**: Race conditions if two admins work on same book simultaneously

**3. No Backup/Restore Feature**
- **Missing**: Built-in database backup
- **Workaround**: Manual MySQL dump required
- **Risk**: Data loss if not regularly backed up

**4. No Audit Trail for Deletes**
- **Partial**: Soft delete preserves book records
- **Missing**: Cannot see who deleted what and when in UI
- **Workaround**: Check transactions table manually

**5. Operating System Dependency**
- **Icons**: Image paths may need adjustment on different OS
- **Database**: MySQL configuration may vary
- **Impact**: Some setup required for cross-platform use

---

## 10. Scope for Improvement

### 10.1 Security Enhancements

**1. Password Hashing**
- **Implementation**: Use bcrypt library for password hashing
- **Benefit**: Protect user credentials even if database compromised
- **Code Change**:
  ```python
  import bcrypt

  # On registration:
  hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

  # On login:
  if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
      # Login successful
  ```

**2. Session Management**
- **Feature**: Auto-logout after inactivity (15-30 minutes)
- **Benefit**: Prevent unauthorized access from unattended terminals
- **Implementation**: Track last activity timestamp, check on each action

**3. Role-Based Access Control (RBAC)**
- **Roles**: Super Admin, Librarian, Assistant
- **Permissions**:
  - Super Admin: All operations + user management
  - Librarian: Issue/Return/Reports
  - Assistant: Search/View only
- **Benefit**: Fine-grained control over operations

**4. Login Attempt Limiting**
- **Feature**: Lock account after 5 failed login attempts
- **Benefit**: Prevent brute-force attacks
- **Implementation**: Add failed_attempts column to users table

### 10.2 Functional Enhancements

**1. Fine Calculation System**
- **Feature**: Automatic fine calculation for overdue books
- **Configuration**: Set per-day fine rate (e.g., ₹5/day)
- **Display**: Show total fine in defaulters list and member portal
- **Payment Tracking**: Record fine payments in new fines table

**2. Book Reservation System**
- **Feature**: Members can reserve books that are currently issued
- **Benefit**: Fair queue system for popular books
- **Logic**:
  - Member reserves book
  - When book returned, notification sent to reserver
  - 24-hour hold period, then next in queue
- **Tables**: Add reservations table

**3. Book Renewal**
- **Feature**: Extend due date by 7 days (max 1 renewal)
- **Conditions**:
  - No one has reserved the book
  - Book not already overdue
  - Member has no other overdue books
- **Benefit**: Flexibility for members needing more time

**4. Email Notifications**
- **Features**:
  - Due date reminder (2 days before)
  - Overdue notification
  - Book availability notification (for reservations)
- **Implementation**: Use smtplib for email sending
- **Configuration**: Add email settings to config file

**5. SMS Notifications**
- **Integration**: Twilio API or similar service
- **Use Cases**:
  - Critical: Book severely overdue (7+ days)
  - Reminder: Due tomorrow
- **Benefit**: Higher reach than email

**6. Advanced Search**
- **Filters**:
  - By ISBN
  - By year range (e.g., 1990-2000)
  - By category/genre (requires new field)
  - By availability status
- **Boolean Search**: AND/OR/NOT operators
- **Benefit**: Faster book discovery

**7. Bulk Operations**
- **Features**:
  - Bulk book upload (CSV import)
  - Bulk member registration
  - Bulk issue/return
- **Benefit**: Faster data entry for large collections

### 10.3 Data Enhancements

**1. Book Categories/Genres**
- **Schema**:
  ```sql
  CREATE TABLE categories (
      category_id INT PRIMARY KEY AUTO_INCREMENT,
      name VARCHAR(50) UNIQUE NOT NULL,
      description VARCHAR(200)
  );

  CREATE TABLE book_categories (
      book_id INT,
      category_id INT,
      PRIMARY KEY (book_id, category_id),
      FOREIGN KEY (book_id) REFERENCES books(book_id),
      FOREIGN KEY (category_id) REFERENCES categories(category_id)
  );
  ```
- **Benefit**: Better organization and filtering

**2. Extended Book Information**
- **Additional Fields**:
  - Publisher
  - Edition
  - Language
  - Page count
  - Synopsis/Summary
  - Cover image path
- **Benefit**: Richer catalog information

**3. Member Types**
- **Types**: Student, Teacher, Staff, Guest
- **Different Rules**:
  - Students: 3 books, 15 days
  - Teachers: 5 books, 30 days
  - Staff: 3 books, 15 days
- **Schema**: Add member_type column to members table

**4. Publisher Management**
- **Table**: Publishers table with contact info
- **Benefit**: Track publisher details, contact for replacements

**5. Authors Table**
- **Normalization**: Separate authors table
- **Features**:
  - Author bio
  - Photo
  - List all books by author
- **Benefit**: Better data organization, author-based search

### 10.4 Reporting Enhancements

**1. Custom Date Range Reports**
- **Feature**: Select start and end date for transaction reports
- **Report Types**:
  - All transactions in range
  - Books issued in range
  - Books returned in range
- **UI**: Date picker widgets (tkcalendar library)

**2. Statistical Reports**
- **Reports**:
  - Most borrowed books (top 10)
  - Most active members (top 10)
  - Book circulation rate
  - Average books per member
  - Books never issued
- **Visualization**: Add matplotlib charts

**3. Export Functionality**
- **Formats**: PDF, Excel, CSV
- **Implementation**:
  - PDF: ReportLab library
  - Excel: openpyxl library
  - CSV: Python csv module
- **Benefit**: Data portability for presentations

**4. Graphical Dashboard**
- **Charts**:
  - Books issued vs returned (line chart)
  - Category-wise distribution (pie chart)
  - Monthly trends (bar chart)
  - Overdue books over time (area chart)
- **Library**: matplotlib or Plotly

**5. Automated Monthly Report**
- **Feature**: Generate and email monthly summary to admin
- **Contents**:
  - Total books added
  - Total issues/returns
  - Current defaulters count
  - Top 5 books
- **Schedule**: First day of each month

### 10.5 User Interface Enhancements

**1. Modern UI Framework**
- **Options**:
  - CustomTkinter (modern themed Tkinter)
  - PyQt5/PyQt6 (professional look)
  - Kivy (cross-platform including mobile)
- **Benefit**: Better aesthetics, more widgets

**2. Dark Mode**
- **Feature**: Toggle between light and dark themes
- **Implementation**: Theme configuration system
- **Benefit**: Reduced eye strain, modern look

**3. Keyboard Shortcuts**
- **Shortcuts**:
  - Ctrl+N: Add new book
  - Ctrl+M: Add new member
  - Ctrl+F: Search catalog
  - Ctrl+I: Issue book
  - F5: Refresh
- **Benefit**: Power user efficiency

**4. Column Sorting**
- **Feature**: Click column headers to sort ascending/descending
- **Implementation**: ttk.Treeview heading bind
- **Benefit**: Easier data browsing

**5. Pagination for Large Datasets**
- **Feature**: Show 50 records per page with next/previous buttons
- **Benefit**: Better performance with thousands of records
- **Implementation**: LIMIT and OFFSET in SQL queries

**6. Autocomplete**
- **Fields**:
  - Book title (when issuing)
  - Author name (when adding book)
  - Member username (when issuing)
- **Benefit**: Faster data entry, fewer typos

**7. Barcode Scanner Support**
- **Feature**: Scan book ISBN barcode
- **Hardware**: USB barcode scanner
- **Benefit**: Faster book identification and issue/return

**8. Member Photo**
- **Feature**: Upload and display member photo
- **Storage**: Save image path in members table
- **Display**: Show in member portal and issue dialog
- **Benefit**: Visual identification

### 10.6 Platform Enhancements

**1. Web-Based Version**
- **Framework**: Flask or Django (Python) or Node.js
- **Benefit**:
  - Access from anywhere
  - No installation required
  - Mobile-friendly responsive design
  - Centralized database
- **Features**: Same as desktop + online catalog

**2. Mobile Application**
- **Platforms**: Android, iOS
- **Framework**: React Native, Flutter, or Kivy
- **Member Features**:
  - View borrowed books
  - Search catalog
  - Reserve books
  - Scan barcode
- **Benefit**: On-the-go access

**3. Cloud Database**
- **Options**: AWS RDS, Google Cloud SQL, Azure Database
- **Benefit**:
  - Automatic backups
  - High availability
  - Remote access
  - Scalability
- **Security**: SSL/TLS encryption for connections

**4. API Development**
- **Framework**: Flask-RESTful or FastAPI
- **Endpoints**:
  - GET /api/books
  - POST /api/books/issue
  - GET /api/members/{id}
- **Benefit**: Third-party integrations, mobile apps

### 10.7 Integration Enhancements

**1. Google Books API Integration**
- **Feature**: Auto-fill book details from ISBN
- **Benefit**: Faster book addition, accurate metadata
- **Data**: Title, author, publisher, year, cover image

**2. OPAC Integration**
- **Feature**: Online Public Access Catalog
- **Benefit**: Public can search books online without login
- **Implementation**: Read-only web interface

**3. Student/Employee Database Integration**
- **Feature**: Import members from school/college database
- **Benefit**: Automatic enrollment, synchronized data
- **Implementation**: CSV import or database link

**4. Payment Gateway Integration**
- **Feature**: Online fine payment
- **Gateways**: Razorpay, Paytm, Stripe
- **Benefit**: Convenient payment, automatic tracking

### 10.8 Administrative Enhancements

**1. Backup and Restore**
- **Feature**: One-click database backup
- **Schedule**: Automatic daily/weekly backups
- **Storage**: Local file + cloud storage (Google Drive, Dropbox)
- **Restore**: UI to restore from backup file

**2. Audit Logs**
- **Tracking**:
  - Who logged in when
  - All database modifications
  - Failed login attempts
  - Deleted records
- **Table**: Add audit_logs table
- **Benefit**: Security, accountability, debugging

**3. System Settings Panel**
- **Configurable Settings**:
  - Borrowing limit (currently hardcoded 3)
  - Due date period (currently hardcoded 15 days)
  - Fine rate per day
  - Maximum renewals
  - Email/SMS settings
- **Storage**: settings table in database

**4. Data Import/Export**
- **Import**: Books and members from Excel/CSV
- **Export**: Complete catalog to Excel/CSV
- **Benefit**: Easy data migration, external analysis

**5. Multi-Library Support**
- **Feature**: Manage multiple library branches
- **Schema**: Add library_id to tables
- **Benefit**: Centralized management for library chains

---

## 11. Bibliography / References

### 11.1 Books

1. **"Python Crash Course" (2nd Edition)** by Eric Matthes
   - Publisher: No Starch Press, 2019
   - Relevance: Python fundamentals and best practices
   - Used for: Core Python programming concepts

2. **"Computer Science with Python" (Class XII)** by Sumita Arora
   - Publisher: Dhanpat Rai & Co., 2020
   - Relevance: CBSE curriculum, MySQL with Python
   - Used for: Database connectivity concepts

3. **"Learning MySQL" (2nd Edition)** by Seyed M.M. Tahaghoghi, Hugh E. Williams
   - Publisher: O'Reilly Media, 2007
   - Relevance: MySQL database design and queries
   - Used for: Table relationships and normalization

4. **"Tkinter GUI Application Development" by Bhaskar Chaudhary**
   - Publisher: Packt Publishing, 2013
   - Relevance: GUI development with Tkinter
   - Used for: Window design and widget usage

### 11.2 Official Documentation

5. **Python Official Documentation**
   - Website: https://docs.python.org/3/
   - Accessed: October-December 2024
   - Used for: Standard library reference, syntax clarification

6. **Tkinter Documentation**
   - Website: https://docs.python.org/3/library/tkinter.html
   - Accessed: October-December 2024
   - Used for: GUI widget properties and methods

7. **MySQL 8.0 Reference Manual**
   - Website: https://dev.mysql.com/doc/refman/8.0/en/
   - Accessed: October-December 2024
   - Used for: SQL syntax, data types, constraints

8. **mysql-connector-python Documentation**
   - Website: https://dev.mysql.com/doc/connector-python/en/
   - Accessed: October-December 2024
   - Used for: Database connection and query execution

9. **Pillow (PIL) Documentation**
   - Website: https://pillow.readthedocs.io/
   - Accessed: December 2024
   - Used for: Image handling for icons

### 11.3 Online Tutorials and Resources

10. **Real Python**
    - Website: https://realpython.com/
    - Topics: Python best practices, Tkinter tutorials
    - Accessed: October-December 2024

11. **W3Schools SQL Tutorial**
    - Website: https://www.w3schools.com/sql/
    - Topics: SQL queries, JOIN operations
    - Accessed: October 2024

12. **GeeksforGeeks - Python Programming**
    - Website: https://www.geeksforgeeks.org/python-programming-language/
    - Topics: Python algorithms, data structures
    - Accessed: October-December 2024

13. **Stack Overflow**
    - Website: https://stackoverflow.com/
    - Used for: Debugging specific errors, code optimization
    - Accessed: Throughout project development

### 11.4 Video Tutorials

14. **Corey Schafer's Python Tutorials (YouTube)**
    - Channel: Corey Schafer
    - Topics: Python fundamentals, MySQL connectivity
    - Accessed: October 2024

15. **Tech With Tim - Tkinter GUI Series (YouTube)**
    - Channel: Tech With Tim
    - Topics: Tkinter widgets, layout management
    - Accessed: November 2024

### 11.5 Research Papers and Articles

16. **"Design and Implementation of Library Management System"**
    - Authors: Various academic papers
    - Source: Google Scholar
    - Relevance: System architecture design patterns

17. **"Database Normalization Best Practices"**
    - Source: Database design articles
    - Relevance: Table relationships and foreign keys

### 11.6 Tools and Software

18. **Python 3.11**
    - Source: https://www.python.org/
    - Purpose: Programming language

19. **MySQL 8.0 Community Server**
    - Source: https://dev.mysql.com/downloads/
    - Purpose: Database management system

20. **Visual Studio Code**
    - Source: https://code.visualstudio.com/
    - Purpose: Code editor and development environment

21. **MySQL Workbench**
    - Source: https://www.mysql.com/products/workbench/
    - Purpose: Database design and testing

22. **Git and GitHub**
    - Source: https://github.com/
    - Purpose: Version control and code repository

### 11.7 Icon and Image Resources

23. **Flaticon**
    - Website: https://www.flaticon.com/
    - Used for: Button icons (PNG format)
    - License: Free for educational use with attribution

24. **Unsplash**
    - Website: https://unsplash.com/
    - Used for: Library background image
    - License: Free to use (Unsplash License)

### 11.8 CBSE Guidelines

25. **CBSE Computer Science Curriculum 2024-25**
    - Source: CBSE official website
    - Document: Class XII CS practical syllabus
    - Relevance: Project requirements and guidelines

26. **CBSE Practical File Guidelines**
    - Source: School computer science department
    - Relevance: Documentation format and structure

---

## End of Documentation

**Project Title**: Library Management System
**Student**: Jhanvi Shankar
**Class**: XII-B
**Roll No**: ASLSKLDK
**Academic Year**: 2024-2025
**Subject**: Computer Science (Code: 083)
**Teacher**: [Teacher Name]
**School**: [School Name]

---

**Document Statistics**:
- Total Pages: 35-40 (estimated)
- Total Screenshots: 46
- Total Code Files: 8
- Total Tables: 4
- Total Lines of Code: ~1200
- Development Period: October 2024 - December 2024

---

**Declaration**

I hereby declare that this project work titled "Library Management System" is my original work and has been carried out under the guidance of my Computer Science teacher. All the information and code presented in this documentation has been duly acknowledged through proper references.

This project has been developed as part of the CBSE Class XII Computer Science practical curriculum for the academic year 2024-2025.

**Signature**: ___________________
**Name**: Jhanvi Shankar
**Date**: ___________________

---

**End of Document**
