import tkinter as tk
from tkinter import messagebox
import mysql.connector
import bcrypt
from PIL import Image, ImageTk

# MySQL connection config - replace with real values
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'invasion',
    'database': 'library_management_system',
}

def get_connection():
    return mysql.connector.connect(**db_config)

def validate_login(username, password):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT password_hash FROM members WHERE member_name = %s", (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            stored_hash = result[0].encode('utf-8')
            # bcrypt check
            return bcrypt.checkpw(password.encode('utf-8'), stored_hash)
        else:
            return False
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return False

def on_login():
    user = entry_username.get()
    pwd = entry_password.get()
    if validate_login(user, pwd):
        messagebox.showinfo("Login Successful", f"Welcome, {user}!")
        show_books_page()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def show_books_page():
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text="Books", font=("Arial", 24, "bold")).pack(pady=30)
    tk.Label(root, text="Welcome, you are logged in!", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Logout", command=show_login_page).pack(pady=20)

def show_login_page():
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text="Username", font=("Arial", 14)).pack(pady=10)
    global entry_username
    entry_username = tk.Entry(root, font=("Arial", 14))
    entry_username.pack(pady=5)
    tk.Label(root, text="Password", font=("Arial", 14)).pack(pady=10)
    global entry_password
    entry_password = tk.Entry(root, show="*", font=("Arial", 14))
    entry_password.pack(pady=5)
    tk.Button(root, text="Login", font=("Arial", 14), command=on_login).pack(pady=20)

root = tk.Tk()
root.title("Library Management System")

root.geometry("1200x800")

# Load and resize your image
image = Image.open("lib.jpg")
image = image.resize((1000, 800))  # Set your desired size
bg_image = ImageTk.PhotoImage(image)

# Create a Label with the image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=50, y=50, relwidth=1, relheight=1)

show_login_page()
root.mainloop()
