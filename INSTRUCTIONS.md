# Library Management System - Setup Instructions

**Class XII Computer Science Project**
**Student:** Jhanvi Shankar
**Roll No:** 120214

---

## Quick Start Guide

### Step 1: Install Required Python Packages

Open terminal/command prompt and run:

```bash
pip install mysql-connector-python
```

### Step 2: Setup Database

1. Make sure MySQL is running on your system
2. Run the database setup script:

```bash
python database_setup.py
```

3. When prompted, enter your MySQL credentials:
   - **Host:** localhost (just press Enter)
   - **Username:** root (just press Enter)
   - **Password:** [your MySQL root password]

The script will:
- Create database `library_management_system`
- Create 4 tables (Categories, Books, Members, Transactions)
- Insert sample data with Indian names

### Step 3: Run the Application

```bash
python library_app.py
```

When the connection screen appears:
- **Host:** localhost
- **Username:** root
- **Password:** [your MySQL root password]

Click **Connect** button.

---

## Features Overview

### 1. Manage Books
- Add new books
- View all books with categories
- See book status (Active/Issued)

### 2. Manage Members
- Add new members
- View all members
- Track member information

### 3. Issue Book
- Issue books to active members
- Automatic transaction ID generation
- 14-day borrowing period

### 4. Return Book
- View all currently issued books
- Process book returns
- Automatic status updates

### 5. Transaction History
- View complete borrowing history
- Track all issued and returned books

### 6. Reports
- Most borrowed books
- Books by category
- Member statistics

---

## Database Schema

### Tables:

1. **Categories** (category_id, category_name)
2. **Books** (book_id, title, author, category_id, book_status)
3. **Members** (member_id, name, email, phone, member_status)
4. **Transactions** (transaction_id, member_id, book_id, issue_date, transaction_status)

---

## Sample Data Included

- **5 Categories:** Computer Science, Programming, Database, Mathematics, Web Development
- **15 Books** with Indian author names
- **10 Members** with Indian names
- **5 Sample Transactions**

---

## System Requirements

- **Python 3.x**
- **MySQL 5.7 or higher**
- **Operating System:** Windows 10/Mac/Linux
- **Python Packages:** mysql-connector-python, tkinter (built-in)

---

## Troubleshooting

### Error: "Access denied for user 'root'"
- Make sure you entered the correct MySQL password
- Try resetting your MySQL root password

### Error: "Module not found: mysql.connector"
- Run: `pip install mysql-connector-python`

### Error: "Database not found"
- Run `database_setup.py` first to create the database

### Application not starting
- Check if MySQL service is running
- Verify Python 3.x is installed: `python --version`

---

## File Structure

```
library_app/
├── database_setup.py          # Database creation script
├── library_app.py             # Main application
├── INSTRUCTIONS.md            # This file
└── requirements.txt           # Python dependencies
```

---

## How to Use

1. **First Time Setup:** Run `database_setup.py`
2. **Daily Use:** Run `library_app.py`
3. **Add Books:** Use "Manage Books" → "+ Add New Book"
4. **Add Members:** Use "Manage Members" → "+ Add New Member"
5. **Issue Books:** Use "Issue Book" → Select member and book
6. **Return Books:** Use "Return Book" → Select transaction → "Process Return"
7. **View Reports:** Use "Reports" → Choose report type

---

## Tips for Presentation

1. Show the database in MySQL:
   ```sql
   USE library_management_system;
   SHOW TABLES;
   SELECT * FROM Books;
   ```

2. Demonstrate all features:
   - Add a new book
   - Add a new member
   - Issue a book
   - Return a book
   - View reports

3. Explain the database relationships:
   - One Category → Many Books
   - One Member → Many Transactions
   - One Book → Many Transactions

---

## Project Highlights

✓ Clean and simple user interface
✓ Complete CRUD operations (Create, Read, Update)
✓ Real-time database integration
✓ Proper foreign key relationships
✓ Transaction management
✓ Reporting functionality
✓ Synthetic Indian data for demonstration

---

**Good luck with your project presentation!** 🎓
