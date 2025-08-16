from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt

class BeansGui(QMainWindow):
    def __init__(self, code_path):
        super().__init__()
        self.setWindowTitle(f"BEANS 0.1.0 - {code_path}")
        self.setGeometry(400, 400, 800, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        top_layout = QHBoxLayout()




        operation_panel = QGroupBox("OPERATION")
        operation_layout = QVBoxLayout()
        operation_layout.setSpacing(2)
        operation_layout.setContentsMargins(5, 5, 5, 5)
        operation_panel.setLayout(operation_layout)

        self.label_last_op = QLabel("Last Operation: None")
        operation_layout.addWidget(self.label_last_op, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        self.label_last_args = QLabel("Last Arguments: [None, None]")
        operation_layout.addWidget(self.label_last_args, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        self.label_last_op_line = QLabel("Line: None / None")
        operation_layout.addWidget(self.label_last_op_line, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        self.label_last_op_time = QLabel("Time Taken: None")
        operation_layout.addWidget(self.label_last_op_time, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)


        top_layout.addWidget(operation_panel)



        memory_panel = QGroupBox("MEMORY")
        memory_layout = QVBoxLayout()
        memory_panel.setLayout(memory_layout)

        top_layout.addWidget(memory_panel)
        main_layout.addLayout(top_layout)



        module_panel = QGroupBox("I/O MODULES")
        module_layout = QVBoxLayout()
        module_panel.setLayout(module_layout)

        
        main_layout.addWidget(module_panel)



app = QApplication([])
win = BeansGui("path/to/file.beans")
win.show()
app.exec()
