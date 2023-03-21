from tkinter import *


def create_text_inputs():
    global text
    global user_inputs
    global save_button
    # 隐藏start按钮
    btn.pack_forget()
    # 生成text输入框
    user_inputs = Text(root, height=10)
    user_inputs.pack()
    # save
    save_button = Button(root, text='save', command=save_text_inputs)
    save_button.pack()

def save_text_inputs():
    # 获取文本内容
    text = user_inputs.get("1.0", "end")
    # 把text保存到项目文件里面
    with open("./user data/text.txt", mode='a', encoding='utf-8') as file:
        file.write(text)
    # 隐藏组件
    user_inputs.pack_forget()
    save_button.pack_forget()


# 生成root窗口
root = Tk()
root.title('窗')
root.geometry('480x240')
# 写一段提示语
lb = Label(root, text='请写下你此时的心情......')
lb.pack()
# start按钮
btn = Button(root, text='start', command=create_text_inputs)
btn.pack()
# 运行程序
root.mainloop()