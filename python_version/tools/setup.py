from tkinter import Tk


def setup():
    # 生成root窗口
    root = Tk()
    root.config(background="#171841")
    root.title('窗')
    root.geometry('480x240')
    return root

def run(root):
    root.mainloop()