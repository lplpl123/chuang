from tkinter import *


class textInputsSurface():

    def __init__(self, lb, btn, root):
        self.lb = lb
        self.btn = btn
        self.root = root

    def create_text_inputs(self):
        # 隐藏上一界面的组件
        self.btn.place_forget()
        # 更改提示语
        self.lb.config(text='请写下你此时的心情......')
        # 生成text输入框
        self.user_inputs = Text(self.root, height=13)
        self.scroll = Scrollbar()
        self.scroll.pack(side=RIGHT, fill=Y)
        self.scroll.config(command=self.user_inputs.yview)
        self.user_inputs.config(yscrollcommand=self.scroll.set)
        self.user_inputs.pack()
        # save
        self.save_button = Button(self.root, text='save', command=self.save_text_inputs)
        self.save_button.place(anchor='center', relx=0.1, rely=0.9)
        # complete
        self.complete_button = Button(self.root, text='complete', command=self.complete_task)
        self.complete_button.place(anchor='center', relx=0.33, rely=0.9)
        # show
        self.show_button = Button(self.root, text='show', command=self.show_text_history)  # todo
        # exit
        self.exit_button = Button(self.root, text='exit', command=lambda : self.exit_text_inputs())
        self.exit_button.place(anchor='center', relx=0.2, rely=0.9)

    def save_text_inputs(self):
        # save功能
        text = self.user_inputs.get("1.0", "end")
        # 把text保存到项目文件里面
        with open("./user data/text.txt", mode='a', encoding='utf-8') as file:
            file.write(text)
        # save and exit功能 todo

    def exit_text_inputs(self):
        # 更改提示语
        self.lb.config(text='请开始你的创作......')
        # 隐藏组件
        self.user_inputs.pack_forget()
        self.save_button.place_forget()
        self.exit_button.place_forget()
        self.complete_button.place_forget()
        self.show_button.place_forget()
        # 显示组件
        self.btn.place(relx=0.5, rely=0.5, anchor='center')

    def complete_task(self):
        # 直接调用存储函数
        self.save_text_inputs()
        # 隐藏按钮
        self.save_button.place_forget()
        self.complete_button.place_forget()
        # show按钮
        self.show_button.place(anchor='center', relx=0.1, rely=0.9)

    def show_text_history(self):
        # 删除inputs里面的内容
        self.user_inputs.delete("1.0", "end")
        # 显示历史内容
        with open('./user data/text.txt', encoding='utf-8') as file:
            data = file.read()
            self.user_inputs.insert("1.0", data)


