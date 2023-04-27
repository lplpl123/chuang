from tkinter import *
from tools import play_gif


class textInputsSurface():

    def __init__(self, lb, btn, root):
        self.lb = lb
        self.btn = btn
        self.root = root
        self.user_inputs = Text(self.root)
        self.save_button = Label(self.root, text='save', bg="#171841", fg="white", cursor='hand2')
        self.save_button.bind("<Button-1>", self.save_text_inputs)
        self.complete_button = Label(self.root, text='complete', bg="#171841", fg="white", cursor='hand2')
        self.complete_button.bind('<Button-1>', self.complete_task)
        self.show_button = Label(self.root, text='show', bg="#171841", fg="white", cursor='hand2')  # todo
        self.show_button.bind('<Button-1>', self.show_text_history)
        self.exit_button = Label(self.root, text='exit', bg="#171841", fg="white", cursor='hand2')
        self.exit_button.bind('<Button-1>', self.exit_text_inputs)
        self.scroll = Scrollbar()

    def create_surface(self):
        # 停止播放上一个界面的动画
        self.root.after_cancel(play_gif.playgif)
        # 隐藏主界面的组件
        self.btn.place_forget()
        # 更改提示语
        self.lb.config(text='请写下你此时的心情......')
        self.user_inputs.place(relx=0.5, rely=0.1, anchor='n')
        self.scroll.pack(side=RIGHT, fill=Y) # todo 放置在user_inputs.info的这个位置
        self.scroll.config(command=self.user_inputs.yview)
        self.user_inputs.config(yscrollcommand=self.scroll.set)
        self.save_button.place(anchor='center', relx=0.1, rely=0.9)
        self.complete_button.place(anchor='center', relx=0.5, rely=0.9)
        self.exit_button.place(anchor='center', relx=0.3, rely=0.9)

    def save_text_inputs(self, event):
        # save功能
        text = self.user_inputs.get("1.0", "end")
        # 把text保存到项目文件里面
        with open("./user data/text.txt", mode='a', encoding='utf-8') as file:
            file.write(text)
        # save and exit功能 todo

    def exit_text_inputs(self, event):
        # 停止播放动画
        play_gif.playgif(1, self.root, self.btn, play_or_not=False)
        # 更改提示语
        self.lb.config(text='请开始你的创作......')
        # 隐藏组件
        self.user_inputs.place_forget()
        self.scroll.pack_forget()
        self.save_button.place_forget()
        self.exit_button.place_forget()
        self.complete_button.place_forget()
        self.show_button.place_forget()
        # 显示组件
        self.btn.place(relx=0.5, rely=0.5, anchor='center')
        i = 1
        play_gif.playgif(i, self.root, self.btn)

    def complete_task(self, event):
        # 直接调用存储函数
        self.save_text_inputs(event)
        # 隐藏按钮
        self.save_button.place_forget()
        self.complete_button.place_forget()
        # show按钮
        self.show_button.place(anchor='center', relx=0.1, rely=0.9)

    def show_text_history(self, event):
        # 删除inputs里面的内容
        self.user_inputs.delete("1.0", "end")
        # 显示历史内容
        with open('./user data/text.txt', encoding='utf-8') as file:
            data = file.read()
            self.user_inputs.insert("1.0", data)


