

# 感觉这里就是text的主界面了
def create_text_inputs(btn, Text, root, Button):
    global text
    global save_button
    global user_inputs
    global exit_button
    # 隐藏start按钮
    btn.pack_forget()
    # 生成text输入框
    user_inputs = Text(root, height=13)
    user_inputs.pack()
    # save
    save_button = Button(root, text='save', command=save_text_inputs)
    save_button.place(anchor='center', relx=0.1, rely=0.9)
    # exit
    exit_button = Button(root, text='exit', command=lambda : exit_text_inputs(btn))
    exit_button.place(anchor='center', relx=0.2, rely=0.9)

def save_text_inputs():
    # save功能
    text = user_inputs.get("1.0", "end")
    # 把text保存到项目文件里面
    with open("./user data/text.txt", mode='a', encoding='utf-8') as file:
        file.write(text)
    # save and exit功能

def exit_text_inputs(btn):
    # 隐藏组件
    user_inputs.pack_forget()
    save_button.place_forget()
    exit_button.place_forget()
    # 显示组件
    btn.pack()

