from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton

class NestedGridGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nested Grid Example")
        self.setGeometry(400, 400, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_grid = QGridLayout()
        central_widget.setLayout(main_grid)

        for i in range(2):
            for j in range(2):

                cell_widget = QWidget()
                cell_layout = QGridLayout()
                cell_widget.setLayout(cell_layout)

                for x in range(2):
                    for y in range(2):
                        cell_layout.addWidget(QPushButton(f"B{i}{j}-{x}{y}"), x, y)

                main_grid.addWidget(cell_widget, i, j)


app = QApplication([])
win = NestedGridGUI()
win.show()
app.exec()