import sys
import ctypes
from PyQt5.Qt import *
from config import app
from surfaces.main_surface import MainSurface


class Run():
    def __init__(self):
        self.setup()

    def setup(self):
        self.chuang = QApplication(sys.argv)
        self.main_window = QWidget()
        desktop = QApplication.desktop()
        x = int((desktop.width() - 1600) / 2)
        y = int((desktop.height() - 600) / 2)
        self.main_window.setGeometry(x, y, app["width"], app["height"])
        self.main_window.setWindowFlags(Qt.FramelessWindowHint)
        self.main_window.setWindowIcon(QIcon("./resources/title_frame_imgs/icon.png"))
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
        self.setup_main_surface()

    def run(self):
        self.main_window.show()
        sys.exit(self.chuang.exec_())

    def setup_main_surface(self):
        self.main_surface = MainSurface(self.chuang, self.main_window)