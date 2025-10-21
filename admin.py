import tkinter as tk
import subprocess

def open_add_user():
    subprocess.Popen(["python3.13", "add_user.py"])

root = tk.Tk()
root.title("Admin Page")
root.geometry("800x600")

buttons = ["Add User", "Delete User", "Browse Catalog", "Add Books", "Books Overdue", "Issue Book", "Update Returned Book"]
for btn in buttons:
    cmd = open_add_user if btn == "Add User" else None
    tk.Button(root, text=btn, width=25, height=2, command=open_add_user).pack(pady=5)

root.mainloop()
