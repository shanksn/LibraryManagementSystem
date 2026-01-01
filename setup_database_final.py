# Database Setup - Library Management System

import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta

def create_connection(host, user, password):
    try:
        connection = mysql.connector.connect(
            host=host, user=user, password=password,
            database='library_management_system')
        if connection.is_connected():
            print("✓ Successfully connected to MySQL")
            return connection
    except Error as e:
        print(f"✗ Error: {e}")
        return None

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

def create_tables(connection):
    try:
        cursor = connection.cursor()
        print("\nCreating tables...")

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

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                member_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                name VARCHAR(100) NOT NULL,
                address VARCHAR(200),
                email VARCHAR(100),
                phone VARCHAR(15),
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
                ON DELETE CASCADE
            )
        """)

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
                FOREIGN KEY (issued_to_member_id)
                REFERENCES members(member_id) ON DELETE SET NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INT AUTO_INCREMENT PRIMARY KEY,
                book_id INT NOT NULL,
                member_id INT DEFAULT NULL,
                admin_user_id INT DEFAULT NULL,
                action VARCHAR(20) NOT NULL,
                transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notes VARCHAR(200) DEFAULT NULL,
                FOREIGN KEY (book_id) REFERENCES books(book_id)
                ON DELETE CASCADE,
                FOREIGN KEY (member_id) REFERENCES members(member_id)
                ON DELETE SET NULL,
                FOREIGN KEY (admin_user_id) REFERENCES users(user_id)
                ON DELETE SET NULL
            )
        """)

        connection.commit()
        cursor.close()
        print("✓ Tables created")
    except Error as e:
        print(f"✗ Error: {e}")

def insert_sample_data(connection):
    try:
        cursor = connection.cursor()

        print("\nInserting users...")
        users = [
            ('admin', 'admin123', 'Admin User', 'admin', 'active'),
            ('priya', 'priya123', 'Priya Sharma', 'member', 'active'),
            ('rahul', 'rahul123', 'Rahul Kumar', 'member', 'active')
        ]
        query = """INSERT INTO users
                   (username, password, full_name, user_type, status)
                   VALUES (%s, %s, %s, %s, %s)"""
        cursor.executemany(query, users)

        print("Inserting members...")
        members = [
            (2, 'Priya Sharma', '123 MG Road, Mumbai',
             'priya@email.com', '9876543210'),
            (3, 'Rahul Kumar', '45 Park Street, Delhi',
             'rahul@email.com', '9876543211')
        ]
        query = """INSERT INTO members
                   (user_id, name, address, email, phone)
                   VALUES (%s, %s, %s, %s, %s)"""
        cursor.executemany(query, members)

        print("Inserting books...")
        today = datetime.now().date()
        books = [
            ('The God of Small Things', 'Arundhati Roy',
             '978-0143028574', 1997, 1, 'Returned', 'Active', None, None),
            ('The God of Small Things', 'Arundhati Roy',
             '978-0143028574', 1997, 2, 'Returned', 'Active', None, None),
            ('Midnight\'s Children', 'Salman Rushdie',
             '978-0099511892', 1981, 1, 'Returned', 'Active', None, None),
            ('The White Tiger', 'Aravind Adiga',
             '978-1416562603', 2008, 1, 'Issued', 'Active', 1, today),
            ('A Suitable Boy', 'Vikram Seth',
             '978-0143065937', 1993, 1, 'Returned', 'Active', None, None),
            ('The Namesake', 'Jhumpa Lahiri',
             '978-0618485222', 2003, 1, 'Returned', 'Active', None, None),
            ('Train to Pakistan', 'Khushwant Singh',
             '978-0143065883', 1956, 1, 'Issued', 'Active', 2,
             today - timedelta(days=5)),
            ('Train to Pakistan', 'Khushwant Singh',
             '978-0143065883', 1956, 2, 'Returned', 'Active', None, None),
            ('The Guide', 'R.K. Narayan',
             '978-0143039648', 1958, 1, 'New', 'Active', None, None),
            ('Malgudi Days', 'R.K. Narayan',
             '978-0143039655', 1943, 1, 'New', 'Active', None, None),
            ('2 States', 'Chetan Bhagat',
             '978-8129115300', 2009, 1, 'New', 'Active', None, None),
            ('2 States', 'Chetan Bhagat',
             '978-8129115300', 2009, 2, 'New', 'Active', None, None),
            ('Five Point Someone', 'Chetan Bhagat',
             '978-8129104177', 2004, 1, 'New', 'Active', None, None),
            ('The Immortals of Meluha', 'Amish Tripathi',
             '978-9380658742', 2010, 1, 'New', 'Active', None, None),
            ('The Secret of the Nagas', 'Amish Tripathi',
             '978-9380658698', 2011, 1, 'New', 'Active', None, None),
            ('Wings of Fire', 'A.P.J. Abdul Kalam',
             '978-8173711466', 1999, 1, 'New', 'Active', None, None),
            ('Wings of Fire', 'A.P.J. Abdul Kalam',
             '978-8173711466', 1999, 2, 'New', 'Active', None, None),
            ('My Experiments with Truth', 'Mahatma Gandhi',
             '978-0486245935', 1927, 1, 'New', 'Active', None, None),
            ('Discovery of India', 'Jawaharlal Nehru',
             '978-0143031055', 1946, 1, 'New', 'Active', None, None),
            ('The Blue Umbrella', 'Ruskin Bond',
             '978-0143333654', 1980, 1, 'New', 'Active', None, None),
            ('The Room on the Roof', 'Ruskin Bond',
             '978-0143333654', 1956, 1, 'New', 'Active', None, None),
            ('The Krishna Key', 'Ashwin Sanghi',
             '978-9382618287', 2012, 1, 'New', 'Active', None, None),
            ('Gitanjali', 'Rabindranath Tagore',
             '978-8129116673', 1910, 1, 'New', 'Active', None, None),
            ('The Bhagavad Gita', 'Eknath Easwaran',
             '978-1586380199', 1985, 1, 'New', 'Active', None, None),
            ('Shantaram', 'Gregory David Roberts',
             '978-0312330538', 2003, 1, 'New', 'Active', None, None)
        ]
        query = """INSERT INTO books
                   (title, author, isbn, year, copy_number, book_status,
                    record_status, issued_to_member_id, issue_date)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.executemany(query, books)

        connection.commit()
        cursor.close()
        print(f"✓ Data inserted ({len(books)} books)")
    except Error as e:
        print(f"✗ Error: {e}")

def main():
    print("="*60)
    print("Library Management System - Database Setup")
    print("="*60)

    host = input("Host (localhost): ").strip() or "localhost"
    user = input("Username (root): ").strip() or "root"
    password = input("Password: ").strip()

    connection = create_connection(host, user, password)
    if connection:
        drop_all_tables(connection)
        create_tables(connection)
        insert_sample_data(connection)

        print("\n" + "="*60)
        print("✓ Setup complete!")
        print("="*60)
        print("\nLogin Credentials:")
        print("Admin: admin/admin123")
        print("Members: priya/priya123, rahul/rahul123")
        print()
        connection.close()

if __name__ == "__main__":
    main()
