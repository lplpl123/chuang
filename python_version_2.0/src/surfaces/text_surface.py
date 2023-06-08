from tkinter import *
from tkinter import filedialog
from config import app


class TextSurface:
    def __init__(self, root):
        self.text_frame = Frame(root, width=app["width"], height=app["height"])
        self.upload_button = Label(self.text_frame, text='upload', bg="#171841", fg="white", cursor='hand2')
        self.upload_button.bind('<Button-1>', self.upload_text)

    def upload_text(self, event):
        # todo 得做个判断，是和任务相匹配的才能上传成功
        file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser('H:/')))