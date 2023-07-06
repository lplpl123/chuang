import os
import time
from tkinter import *
from config import app, button_label
from tools.micro_cartoon import *


class PhotoEditSurface():
    def __init__(self, farther_root, task):
        # init params
        self.farther_root = farther_root
        self.task = task
        self.path = './data/user_private_data/photo_surface_data/'
        # init root
        self.root = Tk()
        self.root.title(task)
        self.root.geometry('{}x{}'.format(self.farther_root.winfo_width(),
                                          self.farther_root.winfo_height()))
        self.root.protocol('WM_DELETE_WINDOW', self.exit_edit_surface)
        # init widgets
        self.root.bind("<Configure>", lambda event: self.photo_edit_frame_auto_resize(event, self.root), add="+")
        self.photo_edit_frame = Frame(self.root, width=app["width"], height=app["height"], bg='white')
        self.photo_edit_frame.bind("<Configure>", lambda event: self.widgets_auto_resize(event))

        # done_button
        self.done_button = Label(self.photo_edit_frame, text='done', bg="white", fg="black", cursor='hand2')
        self.done_button.bind('<Button-1>', self.done_button_function)
        self.done_button.bind('<Enter>', lambda event: mouse_slip_on_widget(event, self.done_button, '#b8f1ed'),
                              add="+")
        self.done_button.bind('<Enter>', lambda event: expand(event, self.done_button), add="+")
        self.done_button.bind('<Leave>', lambda event: mouse_slip_off_widget(event, self.done_button, 'black'), add="+")
        self.done_button.bind('<Leave>', lambda event: reduce(event, self.done_button), add="+")

        # menu
        self.text_inputs_menu = Menu(self.root)
        self.file_functions = Menu(self.text_inputs_menu, tearoff="off")
        self.edit_functions = Menu(self.text_inputs_menu, tearoff="off")
        # file
        self.text_inputs_menu.add_cascade(label='file', menu=self.file_functions)
        self.text_inputs_menu.add_cascade(label='edit', menu=self.edit_functions)
        self.file_functions.add_command(label="new", command=self.new_file)
        self.file_functions.add_command(label="open", command=self.open_file)
        self.file_functions.add_command(label="save", command=self.save_file)
        self.file_functions.add_separator()
        self.file_functions.add_command(label="exit", command=self.exit_edit_surface)
        # edit
        self.edit_functions.add_command(label='cut', command=self.cut)
        self.edit_functions.add_command(label='copy', command=self.copy)
        self.edit_functions.add_command(label='paste', command=self.paste)

