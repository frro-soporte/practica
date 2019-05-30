

import tkinter as tk
from tkinter import ttk

DATA = [('180518-23', '23/06/18'),
        ('180618_24', '27/06/18')]
def invoice_selected(event):
    row_selected = event.widget.focus()
    values = event.widget.item(row_selected)['values']
    invoicenumber = values[0]
    print('invoice number', invoicenumber)

ROOT = tk.Tk()
header = ('Invoice', 'Due')
tree = ttk.Treeview(columns=header,
                    show="headings",
                    height=5)
tree.grid()
for col, text in enumerate(header):
    tree.heading(col, text=text)
tree.bind('<<TreeviewSelect>>', invoice_selected)

for record in DATA:
    tree.insert('', 'end', values=record)
ROOT.mainloop()