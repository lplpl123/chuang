from tkinter import *

def show(event, ):
    if start_button.pack_info():
        print("packed")
    else:
        print("unpacked")

def f():
    start_button.pack_forget()

root = Tk()
root.geometry('480x240')
frame = Frame(root, width=400, height=200)
start_button = Button(frame, text='start', relief=FLAT, bd=0, cursor='hand2', height="6", width="8", bg="blue",
                      command=f)
end_button = Label(frame, text="end")
start_button.bind("<Configure>", lambda event: show(event))
start_button.pack()
end_button.pack()
frame.pack(side=LEFT)
root.mainloop()