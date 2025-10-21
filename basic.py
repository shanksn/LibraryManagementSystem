import tkinter as tk
from tkinter import messagebox

users = {
    "admin": {"password": "adminpass", "role": "Admin"},
    "user1": {"password": "userpass1", "role": "User"}
}

def show_page(name):
    for frame in pages.values():
        frame.place_forget()
    pages[name].place(relx=0.5, rely=0.5, anchor="center")

root = tk.Tk()
root.title("Library Management System")
root.geometry("1100x700")
root.configure(bg="#f3f4f6")
root.resizable(False, False)

pages = {}

# ---- LOGIN PAGE -----
login_frame = tk.Frame(root, bg="#f3f4f6")
pages["login"] = login_frame

header_login = tk.Frame(login_frame, bg="#393943", height=200, width=900)
header_login.pack(pady=(60, 35))
header_login.pack_propagate(False)
title_label = tk.Label(header_login, text="Library Management System", font=("Arial", 32, "bold"), bg="#393943", fg="white")
title_label.pack(pady=(32, 5))
subtitle_label = tk.Label(header_login, text="Login to manage your library operations", font=("Arial", 14), bg="#393943", fg="#e1e1e6")
subtitle_label.pack()

form = tk.Frame(login_frame, bg="#f3f4f6")
form.pack(pady=15)
tk.Label(form, text="Username:", font=("Arial", 16), bg="#f3f4f6").grid(row=0, column=0, padx=10, pady=8, sticky="e")
tk.Label(form, text="Password:", font=("Arial", 16), bg="#f3f4f6").grid(row=1, column=0, padx=10, pady=8, sticky="e")
entry_username = tk.Entry(form, font=("Arial", 14), width=20)
entry_password = tk.Entry(form, font=("Arial", 14), show="*", width=20)
entry_username.grid(row=0, column=1, padx=10, pady=8)
entry_password.grid(row=1, column=1, padx=10, pady=8)

def do_login():
    username = entry_username.get()
    password = entry_password.get()
    if username in users and users[username]['password'] == password:
        role = users[username]['role']
        show_page(role.lower())
        messagebox.showinfo("Login Successful", f"Welcome {role} {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

login_btn = tk.Button(login_frame, text="Login", font=("Arial", 14, "bold"),
                      bg="#5c65e4", fg="white", width=18, command=do_login)
login_btn.pack(pady=(15, 0))

# ---- ADMIN DASHBOARD -----
admin_frame = tk.Frame(root, bg="#f3f4f6")
pages["admin"] = admin_frame

header = tk.Frame(admin_frame, bg="#393943", height=180, width=1100)
header.pack()
header.pack_propagate(False)
tk.Label(header, text="Library Management System", font=("Arial", 28, "bold"), bg="#393943", fg="white").pack(pady=(32, 3))
tk.Label(header, text="Manage your library operations efficiently and effectively", font=("Arial", 14), bg="#393943", fg="#e1e1e6").pack()

cards_frame = tk.Frame(admin_frame, bg="#f3f4f6")
cards_frame.pack(pady=48)

def open_books_from_admin():
    show_page("books")

card_defs = [
    ("Books", "Manage and view information about books in your library catalog.", "View Books", open_books_from_admin),
    ("Members", "Manage library members and their membership information.", "View Members", lambda: messagebox.showinfo("Members", "Members Page")),
    ("Transactions", "Track book borrowing and returns with complete history.", "View Transactions", lambda: messagebox.showinfo("Transactions", "Transactions Page")),
    ("Reports", "View library usage and inventory statistics.", "View Reports", lambda: messagebox.showinfo("Reports", "Reports Page"))
]

for i, (heading, desc, btn_label, cmd) in enumerate(card_defs):
    card = tk.Frame(cards_frame, bg="white", padx=38, pady=36, bd=1, relief="solid", width=210, height=210)
    card.grid(row=0, column=i, padx=20)
    card.grid_propagate(False)
    tk.Label(card, text=heading, font=("Arial", 16, "bold"), bg="white").pack()
    tk.Label(card, text=desc, font=("Arial", 10), wraplength=180, fg="#4b4d53", bg="white", pady=8).pack()
    tk.Button(card, text=btn_label, font=("Arial", 11, "bold"), fg="#5c65e4", bg="#f3f4f6", bd=1, relief="ridge", width=15, command=cmd).pack(pady=4)

tk.Button(admin_frame, text="Logout", command=lambda: show_page("login"), font=("Arial", 12, "bold"), bg="#ab1d1d", fg="white", width=10).pack(pady=34)

# ---- USER DASHBOARD -----
user_frame = tk.Frame(root, bg="#f3f4f6")
pages["user"] = user_frame

header2 = tk.Frame(user_frame, bg="#393943", height=180, width=1100)
header2.pack()
header2.pack_propagate(False)
tk.Label(header2, text="Library Management System", font=("Arial", 28, "bold"), bg="#393943", fg="white").pack(pady=(32, 3))
tk.Label(header2, text="Welcome to the Library", font=("Arial", 14), bg="#393943", fg="#e1e1e6").pack()

cards2_frame = tk.Frame(user_frame, bg="#f3f4f6")
cards2_frame.pack(pady=70)

def open_books_from_user():
    show_page("books")

card2 = tk.Frame(cards2_frame, bg="white", padx=38, pady=36, bd=1, relief="solid", width=210, height=210)
card2.pack()
card2.grid_propagate(False)
tk.Label(card2, text="Books", font=("Arial", 16, "bold"), bg="white").pack()
tk.Label(card2, text="Manage and view information about books in your library catalog.", font=("Arial", 10), wraplength=180, fg="#4b4d53", bg="white", pady=8).pack()
tk.Button(card2, text="View Books", font=("Arial", 11, "bold"), fg="#5c65e4", bg="#f3f4f6", bd=1, relief="ridge", width=15, command=open_books_from_user).pack(pady=4)

tk.Button(user_frame, text="Logout", command=lambda: show_page("login"), font=("Arial", 12, "bold"), bg="#ab1d1d", fg="white", width=10).pack(pady=34)

# ---- BOOKS PAGE -----
books_frame = tk.Frame(root, bg="#f3f4f6")
pages["books"] = books_frame

header_books = tk.Frame(books_frame, bg="#393943", height=100, width=1100)
header_books.pack()
header_books.pack_propagate(False)
tk.Label(header_books, text="Books List", font=("Arial", 28, "bold"), bg="#393943", fg="white").pack(pady=30)

# Sample books list
books_list = [
    "The Great Gatsby",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Catcher in the Rye"
]

listbox = tk.Listbox(books_frame, font=("Arial", 14), width=40, height=10)
listbox.pack(pady=20)
for book in books_list:
    listbox.insert(tk.END, book)

def back_from_books():
    # Based on user role, go back to correct dashboard
    username = entry_username.get()
    if username in users:
        role = users[username]["role"]
        show_page(role.lower())
    else:
        show_page("login")

btn_back = tk.Button(books_frame, text="Back", font=("Arial", 12, "bold"), bg="#5c65e4", fg="white", width=10, command=back_from_books)
btn_back.pack(pady=15)


show_page("login")
root.mainloop()
