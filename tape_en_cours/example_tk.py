from tkinter import *
from tkinter import ttk
import time


def traitement():
    time.sleep(10)


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Click me", command=root.destroy).grid(column=1, row=0)
root.mainloop()
