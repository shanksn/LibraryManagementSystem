from tkinter import *
import tkinter as tk

#Creating Main Window
main = Tk()
main.title("Library Management System - List and Select Books Demo")
main.geometry('600x600+250+100')
main.resizable(0, 0)
ph=PhotoImage(file='lib1.png')
main.iconphoto(False,ph)    

scrollbar = tk.Scrollbar(main, orient="vertical")
listbox = tk.Listbox(main, selectmode=tk.MULTIPLE, yscrollcommand=scrollbar.set, width=40, height=10)
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

from tkinter import messagebox

def show_selected_books():
    selected_books = [listbox.get(i) for i in listbox.curselection()]
    if len(selected_books) > 3:
        messagebox.showerror("Selection Error", "You can select maximum 3 books only.")
        return
    if selected_books:
        print("Selected Books:")
        print(*selected_books, sep="\n")
    else:
        print("No books selected.")

#Creating a Command Button
cmdBtn=Button(main,text='Click Me!', command=show_selected_books,fg='Red',bg='Yellow')
cmdBtn.place(x=250,y=500)

main.mainloop()