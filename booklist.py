import tkinter as tk
from tkinter import messagebox

def show_selected_books():
    selected_indices = listbox.curselection()  # get indices of selected items
    selected_books = [listbox.get(i) for i in selected_indices]
    if selected_books:
        print("Selected Books:")
        for book in selected_books:
            print(book)
    else:
        print("No books selected.")

root = tk.Tk()
root.title("Multi-select Listbox Example")
root.geometry("400x300")

# Frame for listbox and scrollbar
frame = tk.Frame(root)
frame.pack(pady=20)

scrollbar = tk.Scrollbar(frame, orient="vertical")
listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, yscrollcommand=scrollbar.set, width=40, height=10)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side="right", fill="y")
listbox.pack(side="left", fill="both")

books = [
    "The Great Gatsby",
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Catcher in the Rye",
    "Moby-Dick",
    "War and Peace",
    "Ulysses",
    "The Odyssey",
    "Hamlet"
]

for book in books:
    listbox.insert(tk.END, book)

button = tk.Button(root, text="Show Selected Books", command=show_selected_books)
button.pack(pady=10)

root.mainloop()
