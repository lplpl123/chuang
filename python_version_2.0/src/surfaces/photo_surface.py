import os
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from config import app, button_label
from tools.micro_cartoon import *
from tools.select_task_randomly import select_task_randomly
from surfaces.sub_surfaces.photo_edit_surface import PhotoEditSurface


class PhotoSurface:
    def __init__(self, root):
        # init params
        self.root = root
        self.play_index = 1
        self.output_imgs = "./resources/surfaces_imgs/photo_surface_imgs/camera.png"
        self.task, self.level = select_task_randomly("photo_surface")
        # init widgets
        root.bind("<Configure>", lambda event: self.photo_frame_auto_resize(event, root), add="+")
        self.photo_frame = Frame(root, width=app["width"], height=app["height"], bg='#F6F6F6')
        self.photo_frame.bind("<Configure>", lambda event: self.widgets_auto_resize(event))
        self.lb = Label(self.photo_frame, text='请拍下一张照片......', bd=0, bg="#F6F6F6",
                        fg="#b8d38f")
        # upload_button
        self.upload_button = Label(self.photo_frame, text='upload', bg="#F6F6F6", fg="#b8d38f", cursor='hand2')
        self.upload_button.bind('<Button-1>', self.upload_photo)
        self.upload_button.bind('<Enter>', lambda event: mouse_slip_on_widget(event, self.upload_button, 'black'))
        self.upload_button.bind('<Leave>', lambda event: mouse_slip_off_widget(event, self.upload_button, '#b8d38f'))
        # edit_button
        self.edit_button = Label(self.photo_frame, text='edit', bg="#F6F6F6", fg="#b8d38f", cursor='hand2')
        self.edit_button.bind('<Button-1>', self.edit_button_function)
        self.edit_button.bind('<Enter>', lambda event: mouse_slip_on_widget(event, self.edit_button, 'black'))
        self.edit_button.bind('<Leave>', lambda event: mouse_slip_off_widget(event, self.edit_button, '#b8d38f'))
        # exit_button
        self.exit_button = Label(self.photo_frame, text='exit', bg="#F6F6F6", fg="#b8d38f", cursor='hand2')
        self.exit_button.bind('<Button-1>', self.exit)
        self.exit_button.bind('<Enter>', lambda event: mouse_slip_on_widget(event, self.exit_button, 'black'))
        self.exit_button.bind('<Leave>', lambda event: mouse_slip_off_widget(event, self.exit_button, '#b8d38f'))
        self.decoration = Label(self.photo_frame, bd=0, width=60, height=60)
        with Image.open(self.output_imgs) as img:
            img = img.resize((int(self.decoration['width']), int(self.decoration['height'])))
            image = ImageTk.PhotoImage(img)
        self.decoration.config(image=image)
        self.decoration.img = image

    def blit_widgets(self):
        self.photo_frame.place(relx=0.0, rely=0.0, anchor='nw')
        self.photo_frame.tkraise()
        self.lb.place(relx=0.5, rely=0.0, anchor='n')
        self.upload_button.place(anchor='center', relx=0.4, rely=0.5)
        self.edit_button.place(anchor='center', relx=0.6, rely=0.5)
        self.exit_button.place(anchor='center', relx=0.2, rely=0.9)
        self.decoration.place(relx=0.90, rely=0.95, anchor='se')

    def upload_photo(self, event):
        # todo 得做个判断，是和任务相匹配的才能上传成功
        file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))
        if file_path:
            # 保存文件
            image = Image.open(file_path)
            image.save("")
            # todo 如果保存成功的话，需要退出这个界面，直接调用退出函数就好了exit

    def exit(self, event):
        self.photo_frame.place_forget()

    def photo_frame_auto_resize(self, event, root):
        self.photo_frame['width'] = root.winfo_width()
        self.photo_frame['height'] = root.winfo_height()

    def widgets_auto_resize(self, event):
        frame_width = self.photo_frame.winfo_width()
        frame_height = self.photo_frame.winfo_height()
        if frame_width <= frame_height:
            ratio = frame_width / 800
        else:
            ratio = frame_height / 600
        # auto resize widgets
        lb_config = button_label["text_size"]
        self.lb['font'] = ('微软雅黑', int(lb_config + lb_config * ratio), 'normal')
        self.upload_button['font'] = ('微软雅黑', int(lb_config + lb_config * ratio), 'normal')
        self.edit_button['font'] = ('微软雅黑', int(lb_config + lb_config * ratio), 'normal')
        self.exit_button['font'] = ('微软雅黑', int(lb_config + lb_config * ratio), 'normal')

    def edit_button_function(self, event):
        # init sub surfaces
        photo_edit_surface = PhotoEditSurface(self.root, self.task)
        self.root.withdraw()
        photo_edit_surface.blit_widgets()