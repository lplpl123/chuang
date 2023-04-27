from tkinter import *

root = Tk()
root.geometry('480x240')
frame = Frame(root, width=400, height=200)
start_button = Label(frame, text='start', relief=FLAT, bd=0, cursor='hand2', height="6", width="8", bg="blue")
end_button = Label(frame, text="end")
start_button.pack()
end_button.pack()
frame.pack(side=LEFT)
root.mainloop()