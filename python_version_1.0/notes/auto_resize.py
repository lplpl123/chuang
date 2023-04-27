from tkinter import *

i = 12

def config(event):
    global i
    i = 12
    w = root.winfo_width()
    h = root.winfo_height()
    k = min(w, h) / 200
    i = int(i + i*k)
    print(i)
    my_label['font'] = ('Calibri', i)


root= Tk()
root.geometry('200x200')

root.bind("<Configure>", config)

my_label= Label(root, text= 'Hello World!', font= ('Calibri', i))
my_label.place(relx= 0.5, rely= 0.5, anchor= CENTER)

root.mainloop()