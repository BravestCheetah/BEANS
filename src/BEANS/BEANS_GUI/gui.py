from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget

class beans_gui(QMainWindow):
    def __init__(self, code_path):
        super().__init__()

        self.setWindowTitle(f"BEANS 0.1.0 -  {code_path}")
        self.setGeometry(400, 400, 600, 300)

        central = QWidget()
        self.setCentralWidget(central)

        grid = QGridLayout()
        central.setLayout(grid)

        for i in range(1, 5):
            for j in range(1, 5):
                grid.addWidget(QPushButton("B" + str(i) + str(j)), i, j)



app = QApplication([])
win = beans_gui("Path/to/code.bean")
win.show()
app.exec()