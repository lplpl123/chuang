from tkinter import *


class App:
    def __init__(self):
        root=Tk()
        self.text = Text(root)
        self.text.pack()
        self.button = Button(root, text="Get Selection", command=self.OnButton)
        self.button.pack()
        root.mainloop()

    def OnButton(self):
        data = self.text.selection_get()
        print(type(data))
        print(data)

app=App()