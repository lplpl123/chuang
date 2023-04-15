import sys
from PyQt6 import QtWidgets


def setup():
    chuang = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QDialog()
    root.resize(480, 240)
    return root, chuang

def run(root, chuang):
    root.show()
    sys.exit(chuang.exec())