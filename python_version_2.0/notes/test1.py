import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import copy

root = tk.Tk()

lb1 = Label(root, text='a')
lb2 = Label(root, text='a')

lb1.place(relx=0, rely=0.5)
lb2.place(relx=0.5, rely=0.5)


root.mainloop()