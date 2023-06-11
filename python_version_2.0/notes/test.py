from tkinter import *

def f(event):
    frame2 = Frame(root, bg="blue", width=480, height=240)
    frame2.place(relx=0.0, rely=0.0, anchor='nw')
    lb2 = Label(frame2, text='请开始你的chang......', bd=0, bg="#171841", fg="white")
    lb2.bind('<Button-1>', f1)
    lb2.place(relx=0.0, rely=0.0, anchor='nw')

def f1(event):
    frame1.place(relx=0.0, rely=0.0, anchor='nw')


root = Tk()
frame1 = Frame(root, bg="red", width=480, height=240)
frame1.place(relx=0.0, rely=0.0, anchor='nw')
lb1 = Label(frame1, text='请开始你的创作......', bd=0, bg="#171841", fg="white")
lb1.bind('<Button-1>', f)
lb1.place(relx=0.0, rely=0.0, anchor='nw')

root.mainloop()