import sys
from PyQt6 import QtWidgets


if __name__ == "__main__":
    chuang = QtWidgets.QApplication(sys.argv)

    root = QtWidgets.QDialog()
    root.resize(480, 240)

    hbox = QtWidgets.QHBoxLayout()
    button =  QtWidgets.QPushButton("start")
    hbox.addWidget(button)
    root.setLayout(hbox)

    root.show()
    sys.exit(chuang.exec())