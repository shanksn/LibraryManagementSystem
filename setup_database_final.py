"""
Final Database Setup - With issue_date, due_date and copy_number
"""

import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta

def create_connection(host, user, password):
    try:
        connection = mysql.connector.connect(host=host, user=user, password=password, database='library_management_system')
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

        # Users table
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

        # Members table
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

        # Books table with issue_date, copy_number, isbn, and record_status
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

        # Transactions table for audit trail
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

        connection.commit()
        cursor.close()
        print("✓ Tables created")
    except Error as e:
        print(f"✗ Error: {e}")

def insert_sample_data(connection):
    try:
        cursor = connection.cursor()

        # Insert users
        print("\nInserting users...")
        users = [
            ('admin', 'admin123', 'Admin User', 'admin', 'active'),
            ('librarian', 'lib123', 'Library Admin', 'admin', 'active'),
            ('priya', 'priya123', 'Priya Sharma', 'member', 'active'),
            ('rahul', 'rahul123', 'Rahul Kumar', 'member', 'active'),
            ('anjali', 'anjali123', 'Anjali Singh', 'member', 'active')
        ]
        cursor.executemany("INSERT INTO users (username, password, full_name, user_type, status) VALUES (%s, %s, %s, %s, %s)", users)

        # Insert members
        print("Inserting members...")
        members = [
            (3, 'Priya Sharma', '123 MG Road, Mumbai', 'priya@email.com', '9876543210'),
            (4, 'Rahul Kumar', '45 Park Street, Delhi', 'rahul@email.com', '9876543211'),
            (5, 'Anjali Singh', '78 Brigade Road, Bangalore', 'anjali@email.com', '9876543212')
        ]
        cursor.executemany("INSERT INTO members (user_id, name, address, email, phone) VALUES (%s, %s, %s, %s, %s)", members)

        # Insert books (125+ Indian books across genres)
        print("Inserting books...")
        today = datetime.now().date()
        books = [
            # Format: (title, author, isbn, year, copy_number, book_status, record_status, issued_to_member_id, issue_date)

            # Classic Indian Literature
            ('The God of Small Things', 'Arundhati Roy', '978-0143028574', 1997, 1, 'Returned', 'Active', None, None),
            ('The God of Small Things', 'Arundhati Roy', '978-0143028574', 1997, 2, 'Returned', 'Active', None, None),
            ('Midnight\'s Children', 'Salman Rushdie', '978-0099511892', 1981, 1, 'Returned', 'Active', None, None),
            ('The White Tiger', 'Aravind Adiga', '978-1416562603', 2008, 1, 'Issued', 'Active', 1, today),
            ('The White Tiger', 'Aravind Adiga', '978-1416562603', 2008, 2, 'Returned', 'Active', None, None),
            ('A Suitable Boy', 'Vikram Seth', '978-0143065937', 1993, 1, 'Returned', 'Active', None, None),
            ('The Namesake', 'Jhumpa Lahiri', '978-0618485222', 2003, 1, 'Returned', 'Active', None, None),
            ('Train to Pakistan', 'Khushwant Singh', '978-0143065883', 1956, 1, 'Issued', 'Active', 2, today - timedelta(days=5)),
            ('Train to Pakistan', 'Khushwant Singh', '978-0143065883', 1956, 2, 'Returned', 'Active', None, None),
            ('The Palace of Illusions', 'Chitra Banerjee Divakaruni', '978-0307416445', 2008, 1, 'New', 'Active', None, None),
            ('The Inheritance of Loss', 'Kiran Desai', '978-0802142818', 2006, 1, 'New', 'Active', None, None),
            ('The Guide', 'R.K. Narayan', '978-0143039648', 1958, 1, 'New', 'Active', None, None),
            ('Malgudi Days', 'R.K. Narayan', '978-0143039655', 1943, 1, 'New', 'Active', None, None),

            # Chetan Bhagat Series
            ('2 States', 'Chetan Bhagat', '978-8129115300', 2009, 1, 'New', 'Active', None, None),
            ('2 States', 'Chetan Bhagat', '978-8129115300', 2009, 2, 'New', 'Active', None, None),
            ('2 States', 'Chetan Bhagat', '978-8129115300', 2009, 3, 'New', 'Active', None, None),
            ('Five Point Someone', 'Chetan Bhagat', '978-8129104177', 2004, 1, 'New', 'Active', None, None),
            ('Five Point Someone', 'Chetan Bhagat', '978-8129104177', 2004, 2, 'New', 'Active', None, None),
            ('The 3 Mistakes of My Life', 'Chetan Bhagat', '978-8129112071', 2008, 1, 'New', 'Active', None, None),
            ('Revolution 2020', 'Chetan Bhagat', '978-8129118769', 2011, 1, 'New', 'Active', None, None),
            ('Half Girlfriend', 'Chetan Bhagat', '978-8129135728', 2014, 1, 'New', 'Active', None, None),
            ('One Night at the Call Center', 'Chetan Bhagat', '978-8129106278', 2005, 1, 'New', 'Active', None, None),

            # Mythology and Historical Fiction
            ('Sacred Games', 'Vikram Chandra', '978-0143032168', 2006, 1, 'New', 'Active', None, None),
            ('The Immortals of Meluha', 'Amish Tripathi', '978-9380658742', 2010, 1, 'New', 'Active', None, None),
            ('The Immortals of Meluha', 'Amish Tripathi', '978-9380658742', 2010, 2, 'New', 'Active', None, None),
            ('The Secret of the Nagas', 'Amish Tripathi', '978-9380658698', 2011, 1, 'New', 'Active', None, None),
            ('The Oath of the Vayuputras', 'Amish Tripathi', '978-9382618218', 2013, 1, 'New', 'Active', None, None),
            ('Sita: Warrior of Mithila', 'Amish Tripathi', '978-9386224576', 2017, 1, 'New', 'Active', None, None),
            ('Ram: Scion of Ikshvaku', 'Amish Tripathi', '978-9385152146', 2015, 1, 'New', 'Active', None, None),
            ('Raavan: Enemy of Aryavarta', 'Amish Tripathi', '978-9388754194', 2019, 1, 'New', 'Active', None, None),

            # Biographies and Non-Fiction
            ('Wings of Fire', 'A.P.J. Abdul Kalam', '978-8173711466', 1999, 1, 'New', 'Active', None, None),
            ('Wings of Fire', 'A.P.J. Abdul Kalam', '978-8173711466', 1999, 2, 'New', 'Active', None, None),
            ('My Experiments with Truth', 'Mahatma Gandhi', '978-0486245935', 1927, 1, 'New', 'Active', None, None),
            ('Discovery of India', 'Jawaharlal Nehru', '978-0143031055', 1946, 1, 'New', 'Active', None, None),
            ('India After Gandhi', 'Ramachandra Guha', '978-0330505543', 2007, 1, 'New', 'Active', None, None),
            ('The Argumentative Indian', 'Amartya Sen', '978-0312427436', 2005, 1, 'New', 'Active', None, None),
            ('India Unbound', 'Gurcharan Das', '978-0143031635', 2000, 1, 'New', 'Active', None, None),

            # Contemporary Fiction
            ('The Ministry of Utmost Happiness', 'Arundhati Roy', '978-0241303085', 2017, 1, 'New', 'Active', None, None),
            ('A Fine Balance', 'Rohinton Mistry', '978-0679642411', 1995, 1, 'New', 'Active', None, None),
            ('The Blue Umbrella', 'Ruskin Bond', '978-0143333654', 1980, 1, 'New', 'Active', None, None),
            ('The Room on the Roof', 'Ruskin Bond', '978-0143333654', 1956, 1, 'New', 'Active', None, None),
            ('Interpreter of Maladies', 'Jhumpa Lahiri', '978-0618173587', 1999, 1, 'New', 'Active', None, None),
            ('The Lowland', 'Jhumpa Lahiri', '978-0307265746', 2013, 1, 'New', 'Active', None, None),
            ('Serious Men', 'Manu Joseph', '978-0393339796', 2010, 1, 'New', 'Active', None, None),
            ('The Perennial Philosophy', 'Aldous Huxley', '978-0060802868', 1945, 1, 'New', 'Active', None, None),

            # Mystery and Thriller
            ('The Girl in Room 105', 'Chetan Bhagat', '978-9386850669', 2018, 1, 'New', 'Active', None, None),
            ('One Arranged Murder', 'Chetan Bhagat', '978-9388754156', 2020, 1, 'New', 'Active', None, None),
            ('The Krishna Key', 'Ashwin Sanghi', '978-9382618287', 2012, 1, 'New', 'Active', None, None),
            ('The Rozabal Line', 'Ashwin Sanghi', '978-9380658681', 2007, 1, 'New', 'Active', None, None),
            ('Chanakya\'s Chant', 'Ashwin Sanghi', '978-9382618294', 2010, 1, 'New', 'Active', None, None),
            ('The Sialkot Saga', 'Ashwin Sanghi', '978-9385152290', 2016, 1, 'New', 'Active', None, None),

            # Women Writers
            ('Difficult Daughters', 'Manju Kapur', '978-0571203376', 1998, 1, 'New', 'Active', None, None),
            ('A Married Woman', 'Manju Kapur', '978-0571220229', 2002, 1, 'New', 'Active', None, None),
            ('Mistress', 'Anita Nair', '978-0143029649', 2005, 1, 'New', 'Active', None, None),
            ('Ladies Coupe', 'Anita Nair', '978-0312287627', 2001, 1, 'New', 'Active', None, None),
            ('Those Pricey Thakur Girls', 'Anuja Chauhan', '978-0007393084', 2013, 1, 'New', 'Active', None, None),
            ('The Zoya Factor', 'Anuja Chauhan', '978-0007279081', 2008, 1, 'New', 'Active', None, None),
            ('Battle for Bittora', 'Anuja Chauhan', '978-0007326877', 2010, 1, 'New', 'Active', None, None),

            # Social and Political Commentary
            ('India\'s Struggle for Independence', 'Bipan Chandra', '978-0140107814', 1988, 1, 'New', 'Active', None, None),
            ('The Idea of India', 'Sunil Khilnani', '978-0374174583', 1997, 1, 'New', 'Active', None, None),
            ('An Era of Darkness', 'Shashi Tharoor', '978-9386228857', 2016, 1, 'New', 'Active', None, None),
            ('Why I Am a Hindu', 'Shashi Tharoor', '978-9386228987', 2018, 1, 'New', 'Active', None, None),
            ('The Great Indian Novel', 'Shashi Tharoor', '978-0140118193', 1989, 1, 'New', 'Active', None, None),

            # Poetry and Short Stories
            ('Gitanjali', 'Rabindranath Tagore', '978-8129116673', 1910, 1, 'New', 'Active', None, None),
            ('The Home and the World', 'Rabindranath Tagore', '978-0141189260', 1916, 1, 'New', 'Active', None, None),
            ('Selected Poems', 'Kamala Das', '978-0140424515', 1984, 1, 'New', 'Active', None, None),
            ('Night of the Scorpion', 'Nissim Ezekiel', '978-0195644815', 1965, 1, 'New', 'Active', None, None),

            # Young Adult Fiction
            ('The Inscrutable Americans', 'Anurag Mathur', '978-8171675197', 1991, 1, 'New', 'Active', None, None),
            ('Keep Off the Grass', 'Karan Bajaj', '978-0061702860', 2008, 1, 'New', 'Active', None, None),
            ('The Death of Vishnu', 'Manil Suri', '978-0393320954', 2001, 1, 'New', 'Active', None, None),
            ('The Age of Shiva', 'Manil Suri', '978-0393065978', 2008, 1, 'New', 'Active', None, None),

            # Crime and Detective
            ('The Case That Shook India', 'Prashant Jha', '978-9388754323', 2019, 1, 'New', 'Active', None, None),
            ('If God Was a Banker', 'Ravi Subramanian', '978-8129110541', 2007, 1, 'New', 'Active', None, None),
            ('The Incredible Banker', 'Ravi Subramanian', '978-0143419471', 2011, 1, 'New', 'Active', None, None),
            ('The Bankster', 'Ravi Subramanian', '978-0143419846', 2012, 1, 'New', 'Active', None, None),

            # Science Fiction and Fantasy
            ('River of Gods', 'Ian McDonald', '978-1591024361', 2004, 1, 'New', 'Active', None, None),
            ('The Calcutta Chromosome', 'Amitav Ghosh', '978-0380973354', 1995, 1, 'New', 'Active', None, None),
            ('The Shadow Lines', 'Amitav Ghosh', '978-0395519578', 1988, 1, 'New', 'Active', None, None),
            ('Sea of Poppies', 'Amitav Ghosh', '978-0374174217', 2008, 1, 'New', 'Active', None, None),
            ('The Glass Palace', 'Amitav Ghosh', '978-0375758775', 2000, 1, 'New', 'Active', None, None),

            # Philosophy and Spirituality
            ('The Book of Mirdad', 'Mikhail Naimy', '978-0140194630', 1948, 1, 'New', 'Active', None, None),
            ('Autobiography of a Yogi', 'Paramahansa Yogananda', '978-8189297435', 1946, 1, 'New', 'Active', None, None),
            ('The Bhagavad Gita', 'Eknath Easwaran', '978-1586380199', 1985, 1, 'New', 'Active', None, None),
            ('The Upanishads', 'Eknath Easwaran', '978-1586380212', 1987, 1, 'New', 'Active', None, None),

            # Business and Economics
            ('Imagining India', 'Nandan Nilekani', '978-0143104995', 2008, 1, 'New', 'Active', None, None),
            ('The Elephant Paradigm', 'Gurcharan Das', '978-0143419327', 2012, 1, 'New', 'Active', None, None),
            ('In Spite of the Gods', 'Edward Luce', '978-0385514743', 2007, 1, 'New', 'Active', None, None),

            # Travel and Memoirs
            ('Shantaram', 'Gregory David Roberts', '978-0312330538', 2003, 1, 'New', 'Active', None, None),
            ('Maximum City', 'Suketu Mehta', '978-0375703409', 2004, 1, 'New', 'Active', None, None),
            ('The White Castle', 'Orhan Pamuk', '978-0571147182', 1985, 1, 'New', 'Active', None, None),

            # Historical Novels
            ('The Last Mughal', 'William Dalrymple', '978-0143031031', 2006, 1, 'New', 'Active', None, None),
            ('City of Djinns', 'William Dalrymple', '978-0006376897', 1993, 1, 'New', 'Active', None, None),
            ('The Twentieth Wife', 'Indu Sundaresan', '978-0671028114', 2002, 1, 'New', 'Active', None, None),
            ('The Feast of Roses', 'Indu Sundaresan', '978-0743470407', 2003, 1, 'New', 'Active', None, None),
            ('The Tiger Claw', 'Shauna Singh Baldwin', '978-0385720410', 2004, 1, 'New', 'Active', None, None),

            # Romance
            ('It Happened One Night', 'Nidhi Upadhyay', '978-9387779969', 2016, 1, 'New', 'Active', None, None),
            ('Someone Like You', 'Durjoy Datta', '978-9382618386', 2013, 1, 'New', 'Active', None, None),
            ('Of Course I Love You', 'Durjoy Datta', '978-0143419433', 2008, 1, 'New', 'Active', None, None),
            ('Now That You\'re Rich', 'Durjoy Datta', '978-0143419860', 2010, 1, 'New', 'Active', None, None),
            ('She Broke Up I Didn\'t', 'Durjoy Datta', '978-0143423614', 2011, 1, 'New', 'Active', None, None),

            # Comics and Graphic Novels
            ('Delhi Calm', 'Vishwajyoti Ghosh', '978-9380032085', 2010, 1, 'New', 'Active', None, None),
            ('The Harappa Files', 'Parismita Singh', '978-9351950042', 2016, 1, 'New', 'Active', None, None),
            ('Sita\'s Ramayana', 'Samhita Arni', '978-8181581822', 2011, 1, 'New', 'Active', None, None),
        ]
        cursor.executemany("INSERT INTO books (title, author, isbn, year, copy_number, book_status, record_status, issued_to_member_id, issue_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", books)

        connection.commit()
        cursor.close()
        print(f"✓ Data inserted ({len(books)} books)")
    except Error as e:
        print(f"✗ Error: {e}")

def main():
    print("="*60)
    print("Library Management System - Final Database Setup")
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
        print("Members: priya/priya123, rahul/rahul123, anjali/anjali123")
        print()
        connection.close()

if __name__ == "__main__":
    main()
