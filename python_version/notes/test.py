from tkinter import *

root = Tk()
root.geometry('480x240')
start_button = Label(root, text='start', relief=FLAT, bd=0, cursor='hand2', height="60", width="80", bg="blue")
end_button = Label(root, text="end")
start_button.place(relx=0.5, rely=0.0, anchor='center')
end_button.pack()
root.mainloop()