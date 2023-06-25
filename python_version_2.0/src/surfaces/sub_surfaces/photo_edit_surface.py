import os
import time
from tkinter import *


class PhotoEditSurface():
    def __int__(self, farther_root, task):
        # init params
        self.farther_root = farther_root
        self.task = task
        self.path = './data/user_private_data/photo_surface_data/'
        # init root
        self.root = Tk()
        self.root.title(task)
        self.root.geometry('{}x{}'.format(self.farther_root.winfo_width(),
                                          self.farther_root.winfo_height()))
        self.root.protocol('WM_DELETE_WINDOW', self.exit_edit_surface)