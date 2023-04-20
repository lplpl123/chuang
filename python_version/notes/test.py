from tkinter import *

root = Tk()
root.title("Label Demo")
root.geometry("200x100")
Label(root, text="Cursor Hand2", relief="raised",
      bg="lightyellow", padx=5, pady=10,
      cursor="hand2").pack()    # 悬停时鼠标手形
Label(root, text="Cursor heart", relief="raised",
      bg="lightblue", padx=5, pady=10,
      cursor="heart").pack()    # 悬停时鼠标心形
root.mainloop()