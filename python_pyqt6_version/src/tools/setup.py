import sys
from PyQt6 import QtWidgets
from config import app


class Run():
    def __init__(self):
        self.setup()

    def setup(self):
        self.chuang = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle(app["name"])
        self.window.setStyleSheet(f'background-color:{app["background"]}')
        self.window.resize(app["width"], app["height"])

    def run(self):
        self.window.show()
        sys.exit(self.chuang.exec()) # 如果不加这个就会导致只出现一次，马上就结束了


# def setup():
    # root.resize(480, 240)
    # return root, chuang

# def run(root, chuang):
#     root.show()
#     sys.exit(chuang.exec())