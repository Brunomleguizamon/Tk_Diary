from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Diary: CRM")

conn = sqlite3.connect("crm.db")
c = conn.cursor()

c.execute("""
        CREATE TABLE if not exists client(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            company TEXT NOT NULL
        );
""")


def render_clients():
    rows = c.execute("SELECT * FROM client").fetchall()
    tree.delete(*tree.get_children())

    for row in rows:
        tree.insert('', END, row[0], values=(row[1], row[2], row[3]))


def insert(client):
    c.execute("""
            INSERT INTO client (name, phone, company) VALUES(?, ?, ?)
            """, (client['name'], client['phone'], client['company']))
    conn.commit()
    render_clients()


def newClient():
    def save():
        if not name.get():
            messagebox.showerror('Error', 'Name is required')
            return
        if not phone.get():
            messagebox.showerror('Error', 'Phone is required')
            return
        if not company.get():
            messagebox.showerror('Error', 'Company is required')
            return

        client = {
            'name': name.get(),
            'phone': phone.get(),
            'company': company.get(),
        }

        insert(client)
        top.destroy()

    top = Toplevel()
    top.title('New Client')

    lname = Label(top, text='Name')
    name = Entry(top, width=40)
    lname.grid(row=0, column=0)
    name.grid(row=0, column=1)

    lphone = Label(top, text='Phone')
    phone = Entry(top, width=40)
    lphone.grid(row=1, column=0)
    phone.grid(row=1, column=1)

    lcompany = Label(top, text='Company')
    company = Entry(top, width=40)
    lcompany.grid(row=2, column=0)
    company.grid(row=2, column=1)

    btn = Button(top, text='Save', command=save)
    btn.grid(row=3, column=1)


def deleteClient():
    id = tree.selection()[0]
    c.execute("DELETE FROM client WHERE id = ?", (id, ))
    conn.commit()
    render_clients()


btn = Button(root, text='New client', command=newClient)
btn.grid(row=0, column=0)

btn_delete = Button(root, text='Delete client', command=deleteClient)
btn_delete.grid(row=0, column=1)


tree = ttk.Treeview(root)
tree['columns'] = ('Name', 'Phone', 'Company')
tree.column('#0', width=0, stretch=0)
tree.column('Name')
tree.column('Phone')
tree.column('Company')

tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Company', text='Company')
tree.grid(row=1, column=0, columnspan=2)

render_clients()
root.mainloop()
