from tkinter import *
from surfaces.text_inputs_surface import textInputsSurface


if  __name__ == '__main__':
    # 生成root窗口
    root = Tk()
    root.title('窗')
    root.geometry('480x240')
    # 写一段提示语
    lb = Label(root, text='请开始你的创作......')
    lb.pack()
    # start按钮
    btn = Button(root,text='start')
    # 初始化各界面
    text_inputs_surface = textInputsSurface(lb, btn, root)
    btn.config(command=lambda : text_inputs_surface.create_text_inputs())
    btn.place(relx=0.5, rely=0.5, anchor='center')
    # 运行程序
    root.mainloop()