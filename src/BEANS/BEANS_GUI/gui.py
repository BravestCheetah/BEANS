from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox

class SectionedGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI with Sections")
        self.setGeometry(400, 400, 800, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        top_layout = QHBoxLayout()



        operation_panel = QGroupBox("OPERATION")
        top_layout.addWidget(operation_panel)



        memory_panel = QGroupBox("MEMORY")
        top_layout.addWidget(memory_panel)
        main_layout.addLayout(top_layout)



        module_panel = QGroupBox("I/O MODULES")
        main_layout.addWidget(module_panel)



app = QApplication([])
win = SectionedGUI()
win.show()
app.exec()
