from tkinter import *
from tkinter import ttk
import time


def traitement():
    print("on lance")
    time.sleep(10)
    print("c'est fini")


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Launch compute", command=traitement).grid(column=1, row=0)
root.mainloop()
