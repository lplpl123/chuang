from tkinter import *

root = Tk()
x = Label(root, text='hello')
x.pack()
print(x['width'])
root.mainloop()

