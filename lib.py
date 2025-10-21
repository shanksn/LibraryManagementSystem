import tkinter as tk
from tkinter import messagebox

# User data
users = {
    "admin": {"password": "adminpass", "role": "Admin"},
    "user1": {"password": "userpass1", "role": "User"}
}

# Show only one page at a time
def show_page(page_name):
    for page in pages.values():
        page.pack_forget()
    pages[page_name].pack(fill="both", expand=True)

# Initialize main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("800x600")
root.config(bg="#f3f4f6")

pages = {}

# ----------------
# Login Page
# ----------------
login_page = tk.Frame(root, bg="#f3f4f6")
pages["login"] = login_page

tk.Label(login_page, text="Library Management System", font=("Arial", 24, "bold"), bg="#f3f4f6").pack(pady=20)
tk.Label(login_page, text="Login to manage your library operations", font=("Arial", 14), bg="#f3f4f6").pack()

login_form = tk.Frame(login_page, bg="#f3f4f6")
login_form.pack(pady=20)

tk.Label(login_form, text="Username:", font=("Arial", 14), bg="#f3f4f6").grid(row=0, column=0, padx=10, pady=10)
tk.Label(login_form, text="Password:", font=("Arial", 14), bg="#f3f4f6").grid(row=1, column=0, padx=10, pady=10)

entry_username = tk.Entry(login_form, font=("Arial", 14))
entry_password = tk.Entry(login_form, show="*", font=("Arial", 14))
entry_username.grid(row=0, column=1, padx=10, pady=10)
entry_password.grid(row=1, column=1, padx=10, pady=10)

def do_login():
    username = entry_username.get()
    password = entry_password.get()
    if username in users and users[username]["password"] == password:
        role = users[username]["role"]
        current_user.set(username)
        show_page(role.lower())
        messagebox.showinfo("Login Successful", f"Welcome {role} {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

login_button = tk.Button(login_page, text="Login", font=("Arial", 14), bg="#5c65e4", fg="white", command=do_login)
login_button.pack(pady=10)

# ----------------
# Admin Page
# ----------------
admin_page = tk.Frame(root, bg="#f3f4f6")
pages["admin"] = admin_page

tk.Label(admin_page, text="Admin Dashboard", font=("Arial", 20, "bold"), bg="#f3f4f6").pack(pady=20)

def open_books():
    show_page("books")

tk.Button(admin_page, text="Books", font=("Arial", 14), width=20, command=open_books).pack(pady=5)
tk.Button(admin_page, text="Members", font=("Arial", 14), width=20, command=lambda: messagebox.showinfo("Members", "Members Page")).pack(pady=5)
tk.Button(admin_page, text="Transactions", font=("Arial", 14), width=20, command=lambda: messagebox.showinfo("Transactions", "Transactions Page")).pack(pady=5)
tk.Button(admin_page, text="Reports", font=("Arial", 14), width=20, command=lambda: messagebox.showinfo("Reports", "Reports Page")).pack(pady=5)

tk.Button(admin_page, text="Logout", font=("Arial", 14), bg="#ab1d1d", fg="white", width=20, command=lambda: show_page("login")).pack(pady=30)

# ----------------
# User Page
# ----------------
user_page = tk.Frame(root, bg="#f3f4f6")
pages["user"] = user_page

tk.Label(user_page, text="User Dashboard", font=("Arial", 20, "bold"), bg="#f3f4f6").pack(pady=20)
tk.Button(user_page, text="Books", font=("Arial", 14), width=20, command=open_books).pack(pady=5)
tk.Button(user_page, text="Logout", font=("Arial", 14), bg="#ab1d1d", fg="white", width=20, command=lambda: show_page("login")).pack(pady=30)

# ----------------
# Books Page
# ----------------
books_page = tk.Frame(root, bg="#f3f4f6")
pages["books"] = books_page

tk.Label(books_page, text="Books", font=("Arial", 20, "bold"), bg="#f3f4f6").pack(pady=20)

books_list = ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Catcher in the Rye"]
listbox = tk.Listbox(books_page, font=("Arial", 14), width=40, height=10)
listbox.pack(pady=10)

for book in books_list:
    listbox.insert(tk.END, book)

tk.Button(books_page, text="Back", font=("Arial", 14), bg="#5c65e4", fg="white", width=20, command=lambda: show_page(users[current_user.get()]["role"].lower())).pack(pady=10)

# Track current logged-in user
current_user = tk.StringVar()

# Show the login page initially
show_page("login")
root.mainloop()
