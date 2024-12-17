from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
def clicked():
    print("yeeeeees")
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,200,200)
    win.setWindowTitle("Test")

    label = QtWidgets.QLabel(win)
    label.setText("yoooo")
    label.move(50,30)
    button = QtWidgets.QPushButton(win)
    button.setText("Click")
    button.move(50,50)
    button.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())

window()