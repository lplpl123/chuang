from tkinter import *

root = Tk()
root.config(background='#00B66D')
x = Label(root, text='hello')
x.pack()
print(x['width'])
root.mainloop()

