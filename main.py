from tkinter import *
from text_tools import text_tools


# 生成root窗口
root = Tk()
root.title('窗')
root.geometry('480x240')
# 写一段提示语
lb = Label(root, text='请写下你此时的心情......')
lb.pack()
# start按钮
btn = Button(root,
             text='start',
             command=lambda : text_tools.create_text_inputs(btn, Text, root, Button))
btn.pack()
# 运行程序
root.mainloop()