import tkinter as tk

def save():
    print("User saved!")

def reset():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Add User")
root.geometry("800x600")

# Create a center frame
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Member Name
tk.Label(frame, text="Member Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Member Age
tk.Label(frame, text="Member Age:").grid(row=1, column=0, padx=5, pady=5)
age_entry = tk.Entry(frame)
age_entry.grid(row=1, column=1, padx=5, pady=5)

# Member Address
tk.Label(frame, text="Member Address:").grid(row=2, column=0, padx=5, pady=5)
address_entry = tk.Entry(frame)
address_entry.grid(row=2, column=1, padx=5, pady=5)

# Phone Number
tk.Label(frame, text="Phone Number:").grid(row=3, column=0, padx=5, pady=5)
phone_entry = tk.Entry(frame)
phone_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons
tk.Button(frame, text="Save", command=save).grid(row=4, column=0, pady=10)
tk.Button(frame, text="Reset", command=reset).grid(row=4, column=1, pady=10)

root.mainloop()
