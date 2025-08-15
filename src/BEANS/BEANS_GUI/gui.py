from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout

class beans_gui(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BEANS 0.1.0 - /path/to/file.bean")


app = QApplication([])
window = beans_gui()
window.show()
app.exec()