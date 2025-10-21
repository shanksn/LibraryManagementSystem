import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Hardcoded users for demo (In production, use database with hashed passwords)
USERS = {
    "admin": {
        "password": "admin123",
        "user_type": "Admin",
        "full_name": "Administrator",
        "user_id": "USR001",
        "linked_to_id": None
    },
    "librarian": {
        "password": "lib123",
        "user_type": "Admin",
        "full_name": "Librarian Staff",
        "user_id": "USR002",
        "linked_to_id": None
    },
    "rajesh": {
        "password": "raj123",
        "user_type": "Member",
        "full_name": "Rajesh Kumar",
        "user_id": "USR003",
        "linked_to_id": "MEM001",
        "member_data": {
            "first_name": "Rajesh",
            "last_name": "Kumar",
            "books_issued": 2,
            "max_books_allowed": 3,
            "membership_type": "Student"
        }
    },
    "priya": {
        "password": "priya123",
        "user_type": "Member",
        "full_name": "Priya Sharma",
        "user_id": "USR004",
        "linked_to_id": "MEM002",
        "member_data": {
            "first_name": "Priya",
            "last_name": "Sharma",
            "books_issued": 1,
            "max_books_allowed": 5,
            "membership_type": "Faculty"
        }
    }
}

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Center window on screen
        self.center_window()
        
        # Store current user info
        self.current_user = None
        self.user_type = None
        
        # Show login screen
        self.show_login_screen()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_login_screen(self):
        self.clear_screen()
        
        # Main frame
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Login box
        login_frame = tk.Frame(main_frame, bg="white", relief=tk.RAISED, borderwidth=2)
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=400, height=350)
        
        # Title
        title_label = tk.Label(login_frame, text="Library Management System", 
                              font=("Arial", 18, "bold"), bg="white", fg="#333")
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(login_frame, text="Please login to continue", 
                                 font=("Arial", 10), bg="white", fg="#666")
        subtitle_label.pack(pady=5)
        
        # Username
        tk.Label(login_frame, text="Username", font=("Arial", 10), 
                bg="white", fg="#333").pack(pady=(20, 5))
        username_entry = tk.Entry(login_frame, font=("Arial", 11), width=30)
        username_entry.pack(pady=5, ipady=5)
        
        # Password
        tk.Label(login_frame, text="Password", font=("Arial", 10), 
                bg="white", fg="#333").pack(pady=(10, 5))
        password_entry = tk.Entry(login_frame, font=("Arial", 11), 
                                 width=30, show="*")
        password_entry.pack(pady=5, ipady=5)
        
        # Login button
        login_btn = tk.Button(login_frame, text="Login", 
                             font=("Arial", 11, "bold"), bg="#4CAF50", 
                             fg="white", width=20, cursor="hand2",
                             command=lambda: self.login(username_entry.get(), 
                                                       password_entry.get()))
        login_btn.pack(pady=20)
        
        # Footer
        footer_label = tk.Label(login_frame, text="Version 1.0 | Class XII Project", 
                               font=("Arial", 8), bg="white", fg="#999")
        footer_label.pack(side=tk.BOTTOM, pady=10)
        
        # Bind Enter key to login
        password_entry.bind('<Return>', lambda e: self.login(username_entry.get(), 
                                                             password_entry.get()))
    
    def login(self, username, password):
        if not username or not password:
            messagebox.showerror("Error", "Please enter username and password")
            return
        
        # Check hardcoded users
        if username in USERS:
            user = USERS[username]
            if user["password"] == password:
                self.current_user = user
                self.user_type = user['user_type']
                
                messagebox.showinfo("Success", f"Welcome, {user['full_name']}!")
                
                if self.user_type == "Admin":
                    self.show_admin_dashboard()
                else:
                    self.show_member_dashboard()
            else:
                messagebox.showerror("Error", "Invalid password")
        else:
            messagebox.showerror("Error", "Username not found")
    
    def show_admin_dashboard(self):
        self.clear_screen()
        
        # Header
        header_frame = tk.Frame(self.root, bg="#2196F3", height=80)
        header_frame.pack(fill=tk.X)
        
        tk.Label(header_frame, text="Library Management System - Admin Dashboard", 
                font=("Arial", 16, "bold"), bg="#2196F3", fg="white").pack(pady=10)
        
        tk.Label(header_frame, text=f"Welcome, {self.current_user['Full_Name']}", 
                font=("Arial", 10), bg="#2196F3", fg="white").pack()
        
        # Logout button
        logout_btn = tk.Button(header_frame, text="Logout", 
                              font=("Arial", 9), bg="#f44336", fg="white",
                              command=self.show_login_screen)
        logout_btn.place(x=700, y=25)
        
        # Main content area
        content_frame = tk.Frame(self.root, bg="#f5f5f5")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create grid of menu cards
        cards = [
            ("Manage Books", "Add, edit, and view books", self.manage_books),
            ("Manage Members", "Add, edit, and view members", self.manage_members),
            ("Manage Users", "Create and manage user accounts", self.manage_users),
            ("Issue Book", "Issue books to members", self.issue_book),
            ("Return Book", "Process book returns", self.return_book),
            ("View Transactions", "View borrowing history", self.view_transactions),
            ("Overdue Books", "View overdue books", self.view_overdue),
            ("Reports", "Generate reports", self.view_reports)
        ]
        
        row, col = 0, 0
        for title, desc, command in cards:
            card = self.create_menu_card(content_frame, title, desc, command)
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Configure grid weights
        for i in range(4):
            content_frame.grid_columnconfigure(i, weight=1)
        for i in range(2):
            content_frame.grid_rowconfigure(i, weight=1)
    
    def show_member_dashboard(self):
        self.clear_screen()
        
        # Get member details from hardcoded data
        member = self.current_user.get('member_data', {})
        
        # Header
        header_frame = tk.Frame(self.root, bg="#4CAF50", height=80)
        header_frame.pack(fill=tk.X)
        
        tk.Label(header_frame, text="Library Management System - Member Portal", 
                font=("Arial", 16, "bold"), bg="#4CAF50", fg="white").pack(pady=10)
        
        if member:
            tk.Label(header_frame, 
                    text=f"Welcome, {member.get('first_name', '')} {member.get('last_name', '')} | Books Issued: {member.get('books_issued', 0)}/{member.get('max_books_allowed', 3)}", 
                    font=("Arial", 10), bg="#4CAF50", fg="white").pack()
        
        # Logout button
        logout_btn = tk.Button(header_frame, text="Logout", 
                              font=("Arial", 9), bg="#f44336", fg="white",
                              command=self.show_login_screen)
        logout_btn.place(x=700, y=25)
        
        # Main content area
        content_frame = tk.Frame(self.root, bg="#f5f5f5")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create menu cards for members
        cards = [
            ("Search Books", "Find books in catalog", self.search_books),
            ("My Issued Books", "View your borrowed books", self.my_issued_books),
            ("Borrowing History", "View your complete history", self.my_history),
            ("My Profile", "View and update your profile", self.my_profile)
        ]
        
        row, col = 0, 0
        for title, desc, command in cards:
            card = self.create_menu_card(content_frame, title, desc, command)
            card.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")
            
            col += 1
            if col > 1:
                col = 0
                row += 1
        
        # Configure grid weights
        for i in range(2):
            content_frame.grid_columnconfigure(i, weight=1)
            content_frame.grid_rowconfigure(i, weight=1)
    
    def create_menu_card(self, parent, title, description, command):
        card = tk.Frame(parent, bg="white", relief=tk.RAISED, 
                       borderwidth=1, cursor="hand2")
        
        tk.Label(card, text=title, font=("Arial", 14, "bold"), 
                bg="white", fg="#333").pack(pady=15)
        
        tk.Label(card, text=description, font=("Arial", 9), 
                bg="white", fg="#666", wraplength=150).pack(pady=5)
        
        btn = tk.Button(card, text="Open", font=("Arial", 10), 
                       bg="#2196F3", fg="white", width=12,
                       command=command)
        btn.pack(pady=15)
        
        return card
    
    # Placeholder functions for menu items
    def manage_books(self):
        messagebox.showinfo("Manage Books", "Books management screen will open here")
    
    def manage_members(self):
        messagebox.showinfo("Manage Members", "Members management screen will open here")
    
    def manage_users(self):
        messagebox.showinfo("Manage Users", "User management screen will open here")
    
    def issue_book(self):
        messagebox.showinfo("Issue Book", "Book issuing screen will open here")
    
    def return_book(self):
        messagebox.showinfo("Return Book", "Book return screen will open here")
    
    def view_transactions(self):
        messagebox.showinfo("Transactions", "Transaction history will open here")
    
    def view_overdue(self):
        messagebox.showinfo("Overdue Books", "Overdue books list will open here")
    
    def view_reports(self):
        messagebox.showinfo("Reports", "Reports screen will open here")
    
    def search_books(self):
        messagebox.showinfo("Search Books", "Book search screen will open here")
    
    def my_issued_books(self):
        messagebox.showinfo("My Books", "Your issued books will show here")
    
    def my_history(self):
        messagebox.showinfo("History", "Your borrowing history will show here")
    
    def my_profile(self):
        messagebox.showinfo("Profile", "Your profile screen will open here")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()