# Library Management System 📚
**Class XII Computer Science Project**
**Student:** Jhanvi Shankar | **Roll No:** ASLSKLDK

A complete Python-based Library Management System with MySQL database integration, featuring separate interfaces for administrators and library members with comprehensive book tracking and transaction logging.

---

## ✨ Features

### 🔐 Authentication System
- Secure login with username and password
- Role-based access (Admin and Member)
- Background image on login screen
- Account status verification

### 👨‍💼 Admin Features
- **Add Members**: Create new library member accounts with full details (prevents duplicate usernames)
- **Add Books**: Add books with ISBN, multiple copies support (1-5 copies, prevents duplicate titles by same author)
- **Search Catalog**:
  - View all books with filtering (Active/Deleted/All)
  - See total copies and available copies
  - Track borrowers with issue and due dates
  - Double-click to view all copies of a book
- **Issue Books**: Assign books to members with automatic due date calculation (15 days)
- **Return Books**: Process book returns from the detailed copy view
- **Delete Books**: Soft delete books (can be restored manually)
- **Transaction Audit Trail**: All actions tracked with admin user ID

### 👤 Member Features
- **My Borrowed Books**: View all currently issued books with due dates
- **Search Books**: Browse available books in the library
- **Date Tracking**: See issue date and due date in dd/mm/yyyy format

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- MySQL 8.0 or higher
- PIL/Pillow library

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Database Connection
**IMPORTANT:** Set up your database credentials first!

```bash
# Copy the template file
cp config_template.py config.py

# Edit config.py and replace 'your_password' with your MySQL password
```

Or manually create `config.py`:
```python
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_mysql_password',  # Replace this
    'database': 'library_management_system'
}
```

### 3. Setup MySQL Database
```bash
python3 setup_database_final.py
```
Enter your MySQL credentials when prompted. This creates:
- **4 tables**: users, members, books, transactions
- **5 sample users** (2 admins, 3 members)
- **125+ Indian books** across 18 genres
- Sample issued books for testing

### 4. Run the Application
```bash
python3 login.py
```

---

## 🔑 Login Credentials

### Admin Accounts
| Username | Password | Description |
|----------|----------|-------------|
| `admin` | `admin123` | Primary administrator |
| `librarian` | `lib123` | Secondary administrator |

### Member Accounts
| Username | Password | Status |
|----------|----------|--------|
| `priya` | `priya123` | Has 1 book issued |
| `rahul` | `rahul123` | Has 1 book issued |
| `anjali` | `anjali123` | No books issued |

---

## 📁 Project Structure

```
library_app/
├── login.py                    # Login screen with authentication
├── admin.py                    # Admin dashboard
├── member.py                   # Member dashboard
├── add_member.py              # Add new member form
├── add_book.py                # Add new book form
├── setup_database_final.py    # Database setup with 125+ books
├── library.jpeg               # Background image for login
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── INSTRUCTIONS.md            # Additional setup instructions
```

---

## 🗄️ Database Schema

### `users` Table
Stores authentication and user type information.

| Column | Type | Description |
|--------|------|-------------|
| user_id | INT (PK, AUTO_INCREMENT) | Unique user identifier |
| username | VARCHAR(50) UNIQUE | Login username |
| password | VARCHAR(50) | Login password |
| full_name | VARCHAR(100) | User's full name |
| user_type | VARCHAR(20) | 'admin' or 'member' |
| status | VARCHAR(20) | 'active' or 'inactive' |
| created_date | TIMESTAMP | Account creation timestamp |

### `members` Table
Stores member-specific details.

| Column | Type | Description |
|--------|------|-------------|
| member_id | INT (PK, AUTO_INCREMENT) | Unique member identifier |
| user_id | INT (FK) | Links to users table |
| name | VARCHAR(100) | Member name |
| address | VARCHAR(200) | Member address |
| email | VARCHAR(100) | Email address |
| phone | VARCHAR(15) | Phone number |

### `books` Table
Stores book information and status.

| Column | Type | Description |
|--------|------|-------------|
| book_id | INT (PK, AUTO_INCREMENT) | Unique book identifier |
| title | VARCHAR(200) | Book title |
| author | VARCHAR(100) | Book author |
| isbn | VARCHAR(20) | ISBN number |
| year | INT | Publication year |
| copy_number | INT | Copy number (1, 2, 3...) |
| book_status | VARCHAR(20) | 'New', 'Issued', 'Returned' |
| record_status | VARCHAR(20) | 'Active' or 'Deleted' |
| issued_to_member_id | INT (FK) | Current borrower (if issued) |
| issue_date | DATE | Date when book was issued |
| created_date | TIMESTAMP | Record creation timestamp |

### `transactions` Table
Audit trail of all book operations.

| Column | Type | Description |
|--------|------|-------------|
| transaction_id | INT (PK, AUTO_INCREMENT) | Unique transaction ID |
| book_id | INT (FK) | Book involved |
| member_id | INT (FK) | Member involved (if applicable) |
| admin_user_id | INT (FK) | Admin who performed action |
| action | VARCHAR(20) | 'Add', 'Issue', 'Return', 'Delete' |
| transaction_date | TIMESTAMP | When action occurred |
| notes | VARCHAR(200) | Additional details |

---

## 📖 Book Collection

The system includes **125+ carefully curated Indian books** across multiple genres:

- **Classic Literature**: Arundhati Roy, Salman Rushdie, R.K. Narayan
- **Chetan Bhagat Series**: 2 States, Five Point Someone, Half Girlfriend, etc.
- **Mythology**: Complete Amish Tripathi collection (Shiva & Ram series)
- **Biographies**: Wings of Fire, My Experiments with Truth, Discovery of India
- **Contemporary Fiction**: Ruskin Bond, Jhumpa Lahiri, Rohinton Mistry
- **Mystery & Thriller**: Ashwin Sanghi novels
- **Women Writers**: Manju Kapur, Anita Nair, Anuja Chauhan
- **Social Commentary**: Shashi Tharoor, Bipan Chandra
- **Poetry**: Rabindranath Tagore, Kamala Das
- **Business**: Nandan Nilekani, Gurcharan Das
- **And many more...**

All books include authentic ISBN numbers and publication years.

---

## 🎯 Key Business Rules

✅ **Book Status Workflow**:
- New books → Status: "New"
- First issue → Status: "Issued"
- On return → Status: "Returned"

✅ **Multiple Copies**:
- Same book title can have multiple copies
- Each copy tracked separately with copy_number
- Available count shows copies with status "New" or "Returned"
- Maximum 5 copies per book can be added at once
- Minimum 1 copy required

✅ **Duplicate Prevention**:
- Members: Username must be unique across all users
- Books: Same title by same author cannot be added twice

✅ **Date Format**: dd/mm/yyyy (Indian standard)

✅ **Due Date**: Automatically calculated as 15 days from issue date

✅ **Soft Delete**: Deleted books remain in database with record_status="Deleted"

✅ **Transaction Logging**: Every book action logged with admin user ID for accountability

✅ **Admin Tracking**: System tracks which admin performed each action

---

## 🛠️ Configuration

### Database Connection (Using config.py)
This project uses a **separate configuration file** approach (CBSE syllabus compliant):

**File: `config.py`** (not tracked in Git)
```python
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',  # Your actual password here
    'database': 'library_management_system'
}
```

**Benefits:**
- ✅ Single location for database credentials
- ✅ Easy to update password once
- ✅ Secure (config.py is ignored by Git)
- ✅ CBSE recommended practice (modular programming)
- ✅ All files import from: `from config import db_config`

**For GitHub users:**
1. Copy `config_template.py` to `config.py`
2. Update your password in `config.py`
3. `config.py` is automatically ignored by Git

### Window Size
All screens are set to **800x600** for consistency.

---

## 🐛 Troubleshooting

**Error: "No module named 'config'"**
- You need to create `config.py` from `config_template.py`
- Run: `cp config_template.py config.py`
- Then edit `config.py` with your MySQL password

**Error: "Access denied for user 'root'"**
- Update the password in `config.py`

**Error: "No module named 'mysql.connector'"**
```bash
pip install mysql-connector-python
```

**Error: "No module named 'PIL'"**
```bash
pip install Pillow
```

**Error: "Unknown database 'library_management_system'"**
- Run `setup_database_final.py` first to create the database

**Login screen background not showing**
- Ensure `library.jpeg` is in the same folder as `login.py`

---

## 💡 Usage Guide

### For Administrators

1. **Login** with admin credentials
2. **Add Members**: Click "Add Member" → Fill form → Save
   - Username must be unique (system checks for duplicates)
3. **Add Books**: Click "Add Book" → Enter details → Specify copies (1-5) → Save
   - System prevents duplicate books (same title + author)
   - Number of copies must be between 1 and 5
4. **Search Books**:
   - Use search bar to find books
   - Use filter dropdown to view Active/Deleted/All books
   - Double-click any book to see all copies
5. **Issue Book**: Select book → Click "Issue Book" → Enter member username
6. **Return Book**: Double-click book → Select copy → Click "Return Selected Copy"
7. **Delete Book**: Select book → Click "Delete Book" → Confirm

### For Members

1. **Login** with member credentials
2. **View Borrowed Books**: See all books you have with due dates
3. **Search Books**: Browse available books in the catalog

---

## 🎓 Educational Value

This project demonstrates key concepts from CBSE Class XII Computer Science curriculum:

### Python Concepts
- Functions and modular programming
- Exception handling (try/except)
- String formatting and manipulation
- Date and time operations
- Command-line arguments
- Multiple file project structure

### Database Concepts
- MySQL connectivity
- CRUD operations (Create, Read, Update, Delete)
- Foreign keys and relationships
- Transactions and data integrity
- Simple SQL queries without JOINs (beginner-friendly)
- Auto-increment primary keys

### GUI Development
- Tkinter basics
- Event-driven programming
- Form validation
- User-friendly interfaces
- Background images
- Treeview widgets for data display

---

## 📝 Code Style

- **Clear comments** for CBSE students
- **Simple variable names** (no complex abbreviations)
- **Step-by-step logic** (easy to follow)
- **No advanced patterns** (suitable for Class XII level)
- **Proper error handling** with user-friendly messages

---

## 🔄 Future Enhancements

Potential features for advanced students:
- Fine calculation for overdue books
- Book reservation system
- Email notifications for due dates
- Barcode scanning for books
- Report generation (PDF/Excel)
- Search history
- Book recommendations
- User password hashing

---

## 📜 License

This is an educational project for CBSE Class XII Computer Science.

---

## 👥 Credits

**Developer**: Jhanvi Shankar
**Class**: XII-B
**Roll Number**: ASKSLSK
**Subject**: Computer Science
**Academic Year**: 2024-2025

---

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review the code comments
3. Refer to CBSE Computer Science textbook
4. Create an issue on GitHub

---

**Version**: 3.0
**Last Updated**: November 2025

---

⭐ If this project helped you, please star the repository!
