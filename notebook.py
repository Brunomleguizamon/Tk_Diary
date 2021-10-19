from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Diary")

conn = sqlite3.connect("crm.db")
c = conn.cursor()

c.execute("""
        CREATE TABLE if not exists cliente(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            empresa TEXT NOT NULL
        );
""")


def newClient():
    pass


def deleteClient():
    pass


btn = Button(root, text='New client', command=newClient)
btn.grid(column=0, row=0)

btn_delete = Button(root, text='Delete client', command=deleteClient)
btn_delete.grid(column=1, row=0)


root.mainloop()
