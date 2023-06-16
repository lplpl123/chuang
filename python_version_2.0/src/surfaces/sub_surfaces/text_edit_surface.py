from tkinter import *
from config import app, button_label


class TextEditSurface():
    def __init__(self, frame):
        self.root = frame

        self.text_inputs_frame = Frame(frame, width=app["width"], height=app["height"], bg='white')
        self.text_inputs = Text(self.text_inputs_frame)
        self.scroll = Scrollbar(self.text_inputs_frame)
        self.text_inputs.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.text_inputs.yview)
        self.done_button = Label(self.text_inputs_frame, text='done', bg="white", fg="black", cursor='hand2')
        self.done_button.bind('<Button-1>', self.done_button_function)


    def blit_widgets(self):
        self.text_inputs_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.text_inputs_frame.tkraise()
        self.text_inputs.place(relx=0.0, rely=0.0, anchor='nw', relwidth=0.98)
        self.scroll.place(relx=0.98, rely=0.0, anchor='nw',
                          relwidth=0.02, relheight=1)
        self.done_button.place(relx=0.90, rely=0.90, anchor='nw')

    def done_button_function(self, event):
        # 保存文件
        self.text_inputs_frame.destroy()
