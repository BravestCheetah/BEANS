from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout

class beans_gui(QMainWindow):
    def __init__(self, code_path):
        super().__init__()

        self.setWindowTitle(f"BEANS 0.1.0 -  {code_path}")


app = QApplication([])
win = beans_gui("Path/to/code.bean")
win.show()
app.exec()