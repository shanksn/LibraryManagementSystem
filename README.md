# Library Management System

A Python-based Library Management System built with Tkinter, designed as a Class XII Computer Science project. This application provides separate interfaces for administrators and library members to manage books, users, and borrowing operations.

## Features

### Admin Features
- **Manage Books**: Add, edit, and view book catalog
- **Manage Members**: Add, edit, and view library members
- **Manage Users**: Create and manage user accounts
- **Issue Book**: Issue books to members
- **Return Book**: Process book returns
- **View Transactions**: View borrowing history
- **Overdue Books**: Track and view overdue books
- **Reports**: Generate various library reports

### Member Features
- **Search Books**: Browse and search the library catalog
- **My Issued Books**: View currently borrowed books
- **Borrowing History**: View complete borrowing history
- **My Profile**: View and update profile information

## Project Structure

```
library_app/
├── login.py           # Main application with login and dashboards
├── admin.py           # Admin interface launcher
├── add_user.py        # Add user form
├── search_books.py    # Book search functionality
├── booklist.py        # Book listing
├── lib.py             # Core library functions
├── logindb.py         # Database login implementation
├── basic.py           # Basic UI components
├── simple.py          # Simple interface version
├── login_gpt.py       # GPT-enhanced login (experimental)
└── assets/
    ├── lib.png        # Library logo
    ├── lib.jpg        # Library logo (JPG)
    ├── lib1.png       # Library screenshot
    └── library_bg.jpg # Background image
```

## Installation

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually comes with Python)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/shanksn/library-management-system.git
cd library-management-system
```

2. Install dependencies (if any):
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

**Main Application (with login):**
```bash
python login.py
```

**Admin Interface:**
```bash
python admin.py
```

**Add User Form:**
```bash
python add_user.py
```

### Default Login Credentials

**Admin Accounts:**
- Username: `admin` | Password: `admin123`
- Username: `librarian` | Password: `lib123`

**Member Accounts:**
- Username: `rajesh` | Password: `raj123` (Student, 2/3 books issued)
- Username: `priya` | Password: `priya123` (Faculty, 1/5 books issued)

> **Note**: These are hardcoded demo credentials. In production, implement proper database authentication with hashed passwords.

## Features in Detail

### Login System
- Role-based authentication (Admin/Member)
- Separate dashboards for different user types
- Session management
- User profile information

### Admin Dashboard
A comprehensive card-based interface providing:
- Book catalog management
- Member management
- User account management
- Book issuing and return operations
- Transaction history tracking
- Overdue book monitoring
- Report generation

### Member Dashboard
User-friendly interface for members:
- Book search and browse functionality
- View currently issued books
- Access borrowing history
- Update profile information
- Check borrowing limits

## Database Schema (Planned)

The application currently uses hardcoded data. Database integration is planned with the following schema:

- **Users**: User accounts and authentication
- **Members**: Library member information
- **Books**: Book catalog
- **Transactions**: Book issue/return records
- **Categories**: Book categories

## Development Status

**Completed:**
- Login interface with role-based access
- Admin and Member dashboards
- UI/UX design and layout
- Navigation structure

**In Progress:**
- Database integration
- Book management functionality
- Member management functionality
- Transaction processing

**Planned:**
- Search and filter functionality
- Report generation
- Email notifications
- Fine calculation for overdue books
- Book reservation system

## Screenshots

![Library Management System](lib1.png)

## Technical Details

- **Language**: Python 3
- **GUI Framework**: Tkinter
- **Database**: SQLite (planned)
- **Architecture**: MVC pattern

## Contributing

This is a student project, but suggestions and improvements are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is created for educational purposes as part of Class XII Computer Science curriculum.

## Acknowledgments

- Developed as a Class XII Computer Science project
- Built with Python and Tkinter
- Icons and images from local assets

## Contact

For questions or feedback, please open an issue on GitHub.

---
**Version**: 1.0
**Last Updated**: October 2024
