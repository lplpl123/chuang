import os
import time
from tkinter import *
from config import app, button_label
from tools.micro_cartoon import *


class TextEditSurface():
    def __init__(self, farther_root, task):
        # init params
        self.farther_root = farther_root
        self.task = task
        self.path = './data/user_private_data/text_surface_data/'
        # init root
        self.root = Tk()
        self.root.title(task)
        self.root.geometry('{}x{}'.format(self.farther_root.winfo_width(),
                                          self.farther_root.winfo_height()))
        self.root.protocol('WM_DELETE_WINDOW', self.exit_edit_surface)
        # init widgets
        self.root.bind("<Configure>", lambda event: self.text_inputs_frame_auto_resize(event, self.root), add="+")
        self.text_inputs_frame = Frame(self.root, width=app["width"], height=app["height"], bg='white')
        self.text_inputs_frame.bind("<Configure>", lambda event: self.widgets_auto_resize(event))
        self.text_inputs = Text(self.text_inputs_frame)
        self.scroll = Scrollbar(self.text_inputs_frame)
        self.text_inputs.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.text_inputs.yview)
        self.text_inputs.bind("<Button-3>", self.popup)
        # done_button
        self.done_button = Label(self.text_inputs_frame, text='done', bg="white", fg="black", cursor='hand2')
        self.done_button.bind('<Button-1>', self.done_button_function)
        self.done_button.bind('<Enter>', lambda event: expand(event, self.done_button), add="+")
        self.done_button.bind('<Leave>', lambda event: reduce(event, self.done_button), add="+")
        # menu
        self.text_inputs_menu = Menu(self.root, activebackground='blue')
        self.file_functions = Menu(self.text_inputs_menu, tearoff="off")
        self.edit_functions = Menu(self.text_inputs_menu, tearoff="off")
        # file
        self.text_inputs_menu.add_cascade(label='file', menu=self.file_functions)
        self.text_inputs_menu.add_cascade(label='edit', font=('微软雅黑', 15, 'normal'), menu=self.edit_functions)
        self.file_functions.add_command(label="new", font=('微软雅黑', 10, 'normal'), command=self.new_file)
        self.file_functions.add_command(label="open", font=('微软雅黑', 10, 'normal'), command=self.open_file)
        self.file_functions.add_command(label="save", font=('微软雅黑', 10, 'normal'), command=self.save_file)
        self.file_functions.add_separator()
        self.file_functions.add_command(label="exit", font=('微软雅黑', 10, 'normal'), command=self.exit_edit_surface)
        # edit
        self.edit_functions.add_command(label='cut', command=self.cut)
        self.edit_functions.add_command(label='copy', command=self.copy)
        self.edit_functions.add_command(label='paste', command=self.paste)

    def blit_widgets(self):
        self.root.deiconify()
        self.root.config(menu=self.text_inputs_menu)
        self.text_inputs_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.text_inputs_frame.tkraise()
        self.text_inputs.place(relx=0.0, rely=0.0, anchor='nw', relwidth=0.98)
        self.scroll.place(relx=0.98, rely=0.0, anchor='nw',
                          relwidth=0.02, relheight=1)
        self.done_button.place(relx=0.85, rely=0.90, anchor='center')
        self.root.mainloop()

    def done_button_function(self, event):
        # 保存文件
        text_data = self.text_inputs.get("1.0", "end")
        if text_data.strip():
            current_time = time.ctime().split(" ")
            current_time.pop(3)
            current_time = "-".join(current_time)
            if not os.path.isdir(self.path + current_time):
                os.mkdir(self.path + current_time)
            with open(self.path + '{}/{}.txt'.format(current_time, self.task),
                      mode='w', encoding='utf-8') as file:
                file.write(text_data)
        # 还原根窗口
        self.farther_root.deiconify()
        # 摧毁text_edit界面
        self.root.config(menu="")
        self.root.destroy()

    def text_inputs_frame_auto_resize(self, event, root):
        self.text_inputs_frame['width'] = root.winfo_width()
        self.text_inputs_frame['height'] = root.winfo_height()

    def widgets_auto_resize(self, event):
        frame_width = self.text_inputs_frame.winfo_width()
        frame_height = self.text_inputs_frame.winfo_height()
        if frame_width <= frame_height:
            ratio = frame_width / 800
        else:
            ratio = frame_height / 600
        # auto resize widgets
        lb_config = button_label["text_size"]
        self.done_button['font'] = ('微软雅黑', int(lb_config + lb_config * ratio), 'normal')

    def new_file(self):
        pass

    def open_file(self):
        pass

    def save_file(self):
        pass

    def exit_edit_surface(self):
        pass

    def cut(self):
        pass

    def copy(self):
        pass

    def paste(self):
        pass

    def popup(self, event):
        self.edit_functions.post(event.x_root, event.y_root)
