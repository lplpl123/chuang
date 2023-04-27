from tkinter import Tk
from config import app


def setup():
    root = Tk()
    root.config(background=app["background"])
    root.title(app["name"])
    root.geometry('{}x{}'.format(app["width"], app["height"]))
    return root

def run(root):
    root.mainloop()