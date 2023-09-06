# This is an app with pyqt, pandas, numpy
import sys

from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QImage, QKeySequence, QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QKeySequenceEdit, QMessageBox, QFileDialog, QApplication, QLabel, QMainWindow, QMenu, QAction, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QColorDialog


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AppToLearn")
        self.resize(1200, 800)
        self.move(100, 100)

        self.main_window()

    def main_window(self):
        self.btn1 = QPushButton()
        self.setCentralWidget(self.btn1)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())