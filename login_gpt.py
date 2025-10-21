import tkinter as tk
from tkinter import messagebox

# ------------------------------
# Login Screen
# ------------------------------
def login():
    user = username.get()
    pwd = password.get()

    if user == "admin" and pwd == "1234":
        open_admin_page()
    elif user == "member" and pwd == "1234":
        open_member_page()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")

# ------------------------------
# Admin Page
# ------------------------------
def open_admin_page():
    login_window.destroy()
    admin = tk.Tk()
    admin.title("Library Management System - Admin")
    admin.geometry("800x500")
    admin.config(bg="#f4f6f9")

    tk.Label(admin, text="📚 Library Management System", font=("Helvetica", 22, "bold"), bg="#f4f6f9").pack(pady=30)
    tk.Label(admin, text="Welcome, Admin", font=("Arial", 14), bg="#f4f6f9").pack(pady=10)

    # Buttons for Admin
    button_frame = tk.Frame(admin, bg="#f4f6f9")
    button_frame.pack(pady=40)

    tk.Button(button_frame, text="Books", width=20, height=2, bg="#4a90e2", fg="white").grid(row=0, column=0, padx=20, pady=10)
    tk.Button(button_frame, text="Members", width=20, height=2, bg="#4a90e2", fg="white").grid(row=0, column=1, padx=20, pady=10)
    tk.Button(button_frame, text="Catalog", width=20, height=2, bg="#4a90e2", fg="white").grid(row=0, column=2, padx=20, pady=10)

    tk.Button(admin, text="Logout", width=15, bg="#d9534f", fg="white", command=admin.destroy).pack(pady=20)
    admin.mainloop()

# ------------------------------
# Member Page
# ------------------------------
def open_member_page():
    login_window.destroy()
    member = tk.Tk()
    member.title("Library Management System - Member")
    member.geometry("800x500")
    member.config(bg="#f4f6f9")

    tk.Label(member, text="📚 Library Management System", font=("Helvetica", 22, "bold"), bg="#f4f6f9").pack(pady=30)
    tk.Label(member, text="Welcome, Member", font=("Arial", 14), bg="#f4f6f9").pack(pady=10)

    tk.Button(member, text="View Book Catalog", width=25, height=2, bg="#4a90e2", fg="white").pack(pady=40)

    tk.Button(member, text="Logout", width=15, bg="#d9534f", fg="white", command=member.destroy).pack(pady=20)
    member.mainloop()

# ------------------------------
# Build Login Window
# ------------------------------
login_window = tk.Tk()
login_window.title("Library Management System - Login")
login_window.geometry("800x500")
login_window.config(bg="#f4f6f9")

tk.Label(login_window, text="Library Management System", font=("Helvetica", 22, "bold"), bg="#f4f6f9").pack(pady=50)
tk.Label(login_window, text="Login to Continue", font=("Arial", 14), bg="#f4f6f9").pack(pady=10)

frame = tk.Frame(login_window, bg="white", bd=2, relief="solid")
frame.pack(pady=20)

tk.Label(frame, text="Username:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=10, pady=10)
username = tk.Entry(frame, width=25)
username.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame, text="Password:", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=10, pady=10)
password = tk.Entry(frame, show="*", width=25)
password.grid(row=1, column=1, padx=10, pady=10)

tk.Button(login_window, text="Login", bg="#4a90e2", fg="white", width=15, height=1, command=login).pack(pady=20)

login_window.mainloop()
