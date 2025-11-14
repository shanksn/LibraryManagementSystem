# login.py - Python Logic Explanation

**File**: `login.py`
**Purpose**: Entry point for the Library Management System - handles user authentication and redirects to appropriate interface

---

## Overview

This file creates the login screen for the library management system. It authenticates users against the MySQL database and opens either the admin or member interface based on user type.

---

## Import Statements

```python
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess
import sys
from PIL import Image, ImageTk
from config import db_config
```

- **tkinter**: Python's standard GUI library for creating windows, buttons, and input fields
- **messagebox**: For showing popup messages (success/error)
- **mysql.connector**: To connect and query the MySQL database
- **subprocess**: To launch other Python scripts (admin.py or member.py)
- **sys**: To pass command-line arguments to other scripts
- **PIL (Pillow)**: To load and display background images
- **config**: Custom module containing database credentials

---

## Main Function: `login()`

### Step 1: Get User Input
```python
username = username_entry.get().strip()
password = password_entry.get().strip()
```
- Retrieves text from username and password entry fields
- `.strip()` removes leading/trailing whitespace

### Step 2: Validate Input
```python
if not username or not password:
    messagebox.showerror("Error", "Enter username and password")
    return
```
- Checks if fields are empty
- Shows error message and exits function if validation fails

### Step 3: Database Connection
```python
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()
```
- Connects to MySQL using credentials from `config.py`
- `**db_config` unpacks dictionary as keyword arguments
- Creates cursor object to execute SQL queries

### Step 4: Query Database
```python
cursor.execute("SELECT user_id, full_name, user_type, status FROM users WHERE username=%s AND password=%s", (username, password))
result = cursor.fetchone()
conn.close()
```
- Executes parameterized SQL query (prevents SQL injection)
- `%s` are placeholders replaced with actual values
- `fetchone()` retrieves first matching row or None
- Closes database connection after query

### Step 5: Check Results
```python
if result and result[3] == 'active':
    user_id = result[0]
    user_name = result[1]
    user_type = result[2]
```
- `result[0]` = user_id
- `result[1]` = full_name
- `result[2]` = user_type ('admin' or 'member')
- `result[3]` = status ('active' or 'inactive')

### Step 6: Redirect to Appropriate Interface
```python
messagebox.showinfo("Success", f"Welcome, {user_name}!")
root.destroy()

if user_type == 'admin':
    subprocess.Popen([sys.executable, 'admin.py', str(user_id)])
else:
    subprocess.Popen([sys.executable, 'member.py', str(user_id)])
```
- Shows welcome message with user's name
- Closes login window with `root.destroy()`
- Opens admin.py or member.py based on user type
- Passes `user_id` as command-line argument for tracking

---

## GUI Setup

### Main Window
```python
root = tk.Tk()
root.title("Library Management System")
root.geometry("800x600")
root.resizable(False, False)
```
- Creates main application window
- Sets size to 800x600 pixels
- Disables window resizing

### Background Image
```python
bg_image = Image.open("library.jpeg").resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()
canvas.create_image(0, 0, image=bg_photo, anchor=tk.NW)
```
- Loads library.jpeg and resizes to fit window
- Converts to PhotoImage format for tkinter
- Creates canvas widget to hold background
- Places image at top-left corner (anchor=NW = North-West)

### Login Form
```python
frame = tk.Frame(canvas, bg="white")
canvas.create_window(400, 300, window=frame, width=350, height=250)
```
- Creates white frame for login form
- Centers frame at coordinates (400, 300)
- Frame dimensions: 350x250 pixels

### Input Fields
```python
username_entry = tk.Entry(frame, font=("Arial", 11), width=25)
password_entry = tk.Entry(frame, font=("Arial", 11), width=25, show="*")
```
- Two Entry widgets for text input
- Password field uses `show="*"` to hide characters

### Login Button
```python
tk.Button(frame, text="Login", font=("Arial", 11, "bold"), width=15, command=login).pack(pady=15)
```
- Button that calls `login()` function when clicked
- `command=login` connects button to function

### Enter Key Binding
```python
password_entry.bind('<Return>', lambda e: login())
```
- Allows user to press Enter key to login
- `<Return>` is the Enter key event
- `lambda e: login()` is anonymous function that calls login()

### Start Application
```python
root.mainloop()
```
- Starts the tkinter event loop
- Keeps window open and responsive to user actions

---

## CBSE Class XII Concepts Demonstrated

1. **Modular Programming**: Importing config.py for database settings
2. **Database Connectivity**: MySQL connection and queries
3. **GUI Programming**: Tkinter widgets and event handling
4. **String Operations**: `.strip()` method
5. **Conditional Statements**: if-else logic for user validation
6. **Functions**: Defining and calling the login() function
7. **Exception Handling**: Through messagebox error displays
8. **File Handling**: Loading images with PIL
9. **Parameterized Queries**: SQL injection prevention

---

## Security Notes

- **Important**: This implementation stores passwords in plain text (for educational purposes only)
- **Production systems** should use password hashing (bcrypt, SHA-256, etc.)
- **SQL Injection Protection**: Uses parameterized queries with `%s` placeholders
- **Config File**: Database credentials stored separately in config.py

---

## Flow Diagram

```
Start
  ↓
User enters username/password
  ↓
Click Login (or press Enter)
  ↓
Validate input fields
  ↓
Query database
  ↓
User found? → NO → Show error
  ↓ YES
User active? → NO → Show error
  ↓ YES
Show welcome message
  ↓
Close login window
  ↓
User type = admin? → YES → Open admin.py
  ↓ NO
Open member.py
  ↓
End
```
