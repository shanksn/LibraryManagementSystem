# setup_database.py - Python Logic Explanation

**File**: `setup_database_final.py`
**Purpose**: Initialize MySQL database with tables and sample data for the library management system

---

## Overview

This is a one-time setup script that creates the database structure and populates it with initial data including:
- Admin and member user accounts
- Sample members
- 125+ Indian books across various genres
- Sample transactions

---

## Import Statements

```python
import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta
```

- **mysql.connector**: Python MySQL driver for database operations
- **Error**: Exception class for handling MySQL errors
- **datetime**: For date operations
- **timedelta**: For date arithmetic (calculating issue dates)

---

## Functions

### 1. `create_connection()` - Connect to Database

```python
def create_connection(host, user, password):
    try:
        connection = mysql.connector.connect(host=host, user=user, password=password, database='library_management_system')
        if connection.is_connected():
            print("✓ Successfully connected to MySQL")
            return connection
    except Error as e:
        print(f"✗ Error: {e}")
        return None
```

**Purpose**: Establish connection to MySQL database

**Parameters**:
- `host`: MySQL server address (usually 'localhost')
- `user`: MySQL username (usually 'root')
- `password`: MySQL password

**Logic**:
1. Try to connect to database named 'library_management_system'
2. If successful, print checkmark ✓ and return connection object
3. If error, print X mark ✗ and error message, return None

**Error Handling**:
- Catches MySQL connection errors (wrong password, server down, etc.)
- Uses try-except pattern

---

### 2. `drop_all_tables()` - Clean Slate

```python
def drop_all_tables(connection):
    try:
        cursor = connection.cursor()
        print("\nDropping tables...")
        cursor.execute("DROP TABLE IF EXISTS transactions")
        cursor.execute("DROP TABLE IF EXISTS books")
        cursor.execute("DROP TABLE IF EXISTS members")
        cursor.execute("DROP TABLE IF EXISTS users")
        connection.commit()
        cursor.close()
        print("✓ Tables dropped")
    except Error as e:
        print(f"✗ Error: {e}")
```

**Purpose**: Delete all existing tables before recreating them

**Order Matters**: Must drop in reverse order of dependencies
1. **transactions** (references books, members, users)
2. **books** (references members)
3. **members** (references users)
4. **users** (no dependencies)

**Why?**: Foreign key constraints prevent dropping parent tables first

**DROP TABLE IF EXISTS**:
- Won't error if table doesn't exist
- Safe for first-time setup

---

### 3. `create_tables()` - Database Schema

This function creates four tables with relationships.

#### Users Table
```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(100) NOT NULL,
        full_name VARCHAR(100) NOT NULL,
        user_type VARCHAR(20) NOT NULL,
        status VARCHAR(20) DEFAULT 'active',
        created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
```

**Columns Explained**:
- **user_id**: Unique identifier, auto-increments (1, 2, 3, ...)
- **username**: Login name, must be unique, cannot be null
- **password**: Plain text (for education only, should be hashed in production)
- **full_name**: User's complete name
- **user_type**: 'admin' or 'member'
- **status**: 'active' or 'inactive', defaults to 'active'
- **created_date**: Automatically set to current timestamp

**Constraints**:
- `PRIMARY KEY`: Ensures unique user_id
- `UNIQUE`: No duplicate usernames
- `NOT NULL`: Field must have value
- `DEFAULT`: Auto-fills if not specified
- `AUTO_INCREMENT`: Database assigns next number

---

#### Members Table
```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS members (
        member_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        name VARCHAR(100) NOT NULL,
        address VARCHAR(200),
        email VARCHAR(100),
        phone VARCHAR(15),
        created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
    )
""")
```

**Purpose**: Store member profile information

**Foreign Key**:
```sql
FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
```
- Links to users table
- `ON DELETE CASCADE`: If user deleted, member record also deleted

**Columns**:
- **member_id**: Unique member identifier
- **user_id**: Links to users table (authentication)
- **name**: Member name
- **address, email, phone**: Contact information (optional, can be NULL)

---

#### Books Table
```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        book_id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(200) NOT NULL,
        author VARCHAR(100) NOT NULL,
        isbn VARCHAR(20) DEFAULT NULL,
        year INT NOT NULL,
        copy_number INT DEFAULT 1,
        book_status VARCHAR(20) DEFAULT 'Returned',
        record_status VARCHAR(20) DEFAULT 'Active',
        issued_to_member_id INT DEFAULT NULL,
        issue_date DATE DEFAULT NULL,
        created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (issued_to_member_id) REFERENCES members(member_id) ON DELETE SET NULL
    )
""")
```

**Purpose**: Store book catalog with multiple copy support

**Key Fields**:
- **book_id**: Unique ID for each physical copy
- **title, author**: Book information
- **isbn**: International Standard Book Number (optional)
- **year**: Publication year
- **copy_number**: Which copy (1, 2, 3 for same title)
- **book_status**: 'New', 'Issued', 'Returned'
- **record_status**: 'Active' or 'Deleted' (soft delete)
- **issued_to_member_id**: NULL if available, member_id if issued
- **issue_date**: Date when book was issued

**Foreign Key**:
```sql
FOREIGN KEY (issued_to_member_id) REFERENCES members(member_id) ON DELETE SET NULL
```
- Links to members table
- `ON DELETE SET NULL`: If member deleted, book becomes available (issued_to_member_id = NULL)

**Multiple Copies Example**:
```
book_id  title             author          copy_number
101      The White Tiger   Aravind Adiga   1
102      The White Tiger   Aravind Adiga   2
103      The White Tiger   Aravind Adiga   3
```

---

#### Transactions Table
```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INT AUTO_INCREMENT PRIMARY KEY,
        book_id INT NOT NULL,
        member_id INT DEFAULT NULL,
        admin_user_id INT DEFAULT NULL,
        action VARCHAR(20) NOT NULL,
        transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        notes VARCHAR(200) DEFAULT NULL,
        FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
        FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE SET NULL,
        FOREIGN KEY (admin_user_id) REFERENCES users(user_id) ON DELETE SET NULL
    )
""")
```

**Purpose**: Audit trail for all book operations

**Columns**:
- **transaction_id**: Unique transaction number
- **book_id**: Which book (required)
- **member_id**: Which member (NULL for delete/add actions)
- **admin_user_id**: Which admin performed action
- **action**: 'Issue', 'Return', 'Add', 'Delete'
- **transaction_date**: Automatic timestamp
- **notes**: Additional information

**Three Foreign Keys**:
1. book_id → books table
2. member_id → members table
3. admin_user_id → users table

**ON DELETE Actions**:
- `CASCADE`: Delete transaction if book deleted
- `SET NULL`: Keep transaction but set member/admin to NULL if deleted

---

### 4. `insert_sample_data()` - Populate Database

#### Insert Users
```python
users = [
    ('admin', 'admin123', 'Admin User', 'admin', 'active'),
    ('librarian', 'lib123', 'Library Admin', 'admin', 'active'),
    ('priya', 'priya123', 'Priya Sharma', 'member', 'active'),
    ('rahul', 'rahul123', 'Rahul Kumar', 'member', 'active'),
    ('anjali', 'anjali123', 'Anjali Singh', 'member', 'active')
]
cursor.executemany("INSERT INTO users (username, password, full_name, user_type, status) VALUES (%s, %s, %s, %s, %s)", users)
```

**executemany()**: Inserts multiple rows efficiently
- More efficient than 5 separate INSERT statements
- Single database round-trip

**Sample Users Created**:
- 2 admins (admin, librarian)
- 3 members (priya, rahul, anjali)

---

#### Insert Members
```python
members = [
    (3, 'Priya Sharma', '123 MG Road, Mumbai', 'priya@email.com', '9876543210'),
    (4, 'Rahul Kumar', '45 Park Street, Delhi', 'rahul@email.com', '9876543211'),
    (5, 'Anjali Singh', '78 Brigade Road, Bangalore', 'anjali@email.com', '9876543212')
]
cursor.executemany("INSERT INTO members (user_id, name, address, email, phone) VALUES (%s, %s, %s, %s, %s)", members)
```

**Note**: user_id values (3, 4, 5) correspond to:
- user_id 1 = admin
- user_id 2 = librarian
- user_id 3 = priya
- user_id 4 = rahul
- user_id 5 = anjali

---

#### Insert Books
```python
today = datetime.now().date()
books = [
    # Format: (title, author, isbn, year, copy_number, book_status, record_status, issued_to_member_id, issue_date)

    ('The God of Small Things', 'Arundhati Roy', '978-0143028574', 1997, 1, 'Returned', 'Active', None, None),
    ('The God of Small Things', 'Arundhati Roy', '978-0143028574', 1997, 2, 'Returned', 'Active', None, None),
    ('The White Tiger', 'Aravind Adiga', '978-1416562603', 2008, 1, 'Issued', 'Active', 1, today),
    ('Train to Pakistan', 'Khushwant Singh', '978-0143065883', 1956, 1, 'Issued', 'Active', 2, today - timedelta(days=5)),
    # ... 125+ more books
]
```

**Book Status Examples**:

1. **Available Books**:
   - `book_status='Returned'` or `'New'`
   - `issued_to_member_id=None`
   - `issue_date=None`

2. **Issued Books**:
   - `book_status='Issued'`
   - `issued_to_member_id=1` (issued to Priya)
   - `issue_date=today` (issued today)

3. **Date Arithmetic**:
   ```python
   today - timedelta(days=5)
   ```
   - If today is Nov 14, this gives Nov 9
   - Used for books issued 5 days ago

**Book Collection**: 125+ books including:
- Classic Indian Literature
- Chetan Bhagat novels
- Amish Tripathi mythology
- Biographies (APJ Abdul Kalam, Gandhi)
- Contemporary fiction
- Multiple genres

---

## Database Design Principles

### 1. Normalization
- **No Redundancy**: Member info stored once in members table
- **Foreign Keys**: Relationships defined explicitly

### 2. Data Integrity
- **Primary Keys**: Ensure unique records
- **Foreign Keys**: Maintain relationships
- **Constraints**: NOT NULL, UNIQUE enforce rules

### 3. Soft Delete
- Books marked 'Deleted' in record_status
- Preserves transaction history
- Can be restored if needed

### 4. Audit Trail
- Transactions table logs all actions
- Who (admin_user_id), What (action), When (transaction_date)

---

## Entity Relationship Diagram

```
┌──────────────┐
│    users     │
│              │
│  user_id PK  │◄─────┐
│  username    │      │
│  password    │      │
│  user_type   │      │
└──────────────┘      │
       │              │
       │              │
       │ 1            │
       │              │
       │              │ N
       │         ┌──────────────┐
       │         │  members     │
       │         │              │
       └────────►│  member_id PK│◄────┐
                 │  user_id  FK │     │
                 │  name        │     │
                 │  address     │     │
                 └──────────────┘     │
                        │             │
                        │             │
                        │ 1           │
                        │             │
                        │             │ N
                        │        ┌──────────────────┐
                        │        │     books        │
                        │        │                  │
                        │        │  book_id      PK │◄───┐
                        └───────►│  issued_to... FK │    │
                                 │  title           │    │
                                 │  author          │    │
                                 │  copy_number     │    │
                                 │  book_status     │    │
                                 └──────────────────┘    │
                                          │              │
                                          │              │
                                          │ 1            │ N
                                          │         ┌────────────────┐
                                          │         │ transactions   │
                                          │         │                │
                                          └────────►│  book_id    FK │
                                                    │  member_id  FK │
                                                    │  admin_...  FK │
                                                    │  action        │
                                                    │  notes         │
                                                    └────────────────┘
```

---

## Running the Script

### Main Execution Block (Not shown in snippet but typically):
```python
if __name__ == "__main__":
    # Database credentials
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = 'your_password'

    # Connect to MySQL
    conn = create_connection(HOST, USER, PASSWORD)

    if conn:
        # Drop existing tables
        drop_all_tables(conn)

        # Create new tables
        create_tables(conn)

        # Insert sample data
        insert_sample_data(conn)

        # Close connection
        conn.close()
        print("\n✓ Database setup complete!")
```

---

## CBSE Class XII Concepts Demonstrated

1. **Functions**: Modular code organization
2. **Database DDL**: CREATE TABLE statements
3. **Database DML**: INSERT statements
4. **Primary Keys**: AUTO_INCREMENT
5. **Foreign Keys**: Relationships between tables
6. **Data Types**: INT, VARCHAR, DATE, TIMESTAMP
7. **Constraints**: NOT NULL, UNIQUE, DEFAULT
8. **Exception Handling**: try-except blocks
9. **Date Operations**: datetime, timedelta
10. **Batch Operations**: executemany()

---

## Common SQL Commands Explained

### CREATE TABLE
```sql
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    ...
)
```

### Data Types:
- **INT**: Integer numbers (user_id, year)
- **VARCHAR(n)**: Variable-length string up to n characters
- **DATE**: Date without time (YYYY-MM-DD)
- **TIMESTAMP**: Date with time

### Constraints:
- **PRIMARY KEY**: Unique identifier, cannot be NULL
- **FOREIGN KEY**: Links to another table
- **UNIQUE**: No duplicates allowed
- **NOT NULL**: Must have value
- **DEFAULT**: Value if not specified
- **AUTO_INCREMENT**: Database assigns next number

### Referential Actions:
- **ON DELETE CASCADE**: Delete child when parent deleted
- **ON DELETE SET NULL**: Set to NULL when parent deleted

---

## Sample Data Summary

### Users Table (5 records):
```
user_id | username  | user_type | status
1       | admin     | admin     | active
2       | librarian | admin     | active
3       | priya     | member    | active
4       | rahul     | member    | active
5       | anjali    | member    | active
```

### Books Summary:
- **125+ books** from Indian authors
- **Multiple copies** of popular books
- **Various statuses**:
  - New: Just added
  - Returned: Available
  - Issued: Currently borrowed
- **Genres**: Fiction, Biography, Mythology, Romance, Mystery, etc.

---

## Why This Design?

### Separate Login and Profile
**users** = authentication
**members** = profile information

Allows:
- Admin users without member profiles
- Deactivating login without losing member data
- Future expansion (vendors, publishers, etc.)

### Copy Number System
Same book, multiple physical copies:
```
'The White Tiger' Copy 1 → Issued to Priya
'The White Tiger' Copy 2 → Available
```

### Transactions Table
Complete audit trail:
- Who issued which book to whom
- When was it returned
- Which admin processed the transaction

---

## Script Output Example

```
✓ Successfully connected to MySQL

Dropping tables...
✓ Tables dropped

Creating tables...
✓ Tables created

Inserting users...
Inserting members...
Inserting books...

✓ Database setup complete!
```

---

## Important Notes

1. **Run Once**: This script is for initial setup only
2. **Destructive**: Drops all existing data
3. **Plain Text Passwords**: Educational purpose only
4. **Sample Data**: Includes realistic Indian library books
5. **Multiple Copies**: Demonstrates copy_number system
6. **Transactions**: Provides audit trail foundation

---

## Next Steps After Setup

1. Run this script to create database
2. Create config.py with database credentials
3. Run login.py to start application
4. Log in as admin (username: admin, password: admin123)
5. Test all features (add books, issue, return, reports)
