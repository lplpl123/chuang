from tkinter import *


class WaitingInit:
    def __init__(self):
        self.root = Tk()
        self.root.overrideredirect(True)

    def run(self):
        self.root.mainloop()