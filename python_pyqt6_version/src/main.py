from PyQt6 import QtWidgets
from tools import setup

if __name__ == "__main__":

    run = setup.Run()
    run.run()

    # root, chuang = setup.setup()
    # hbox = QtWidgets.QHBoxLayout()
    # button = QtWidgets.QPushButton("start")
    # hbox.addWidget(button)
    # root.setLayout(hbox)
    # setup.run(root, chuang)
