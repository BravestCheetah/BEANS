from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGroupBox

class SectionedGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI with Sections")
        self.setGeometry(400, 400, 800, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Left sidebar
        sidebar = QVBoxLayout()
        sidebar_widget = QGroupBox("Sidebar")
        sidebar_widget.setLayout(sidebar)
        sidebar.addWidget(QPushButton("Button 1"))
        sidebar.addWidget(QPushButton("Button 2"))
        sidebar.addStretch()  # Pushes buttons to the top
        main_layout.addWidget(sidebar_widget)

        # Main content area
        content = QVBoxLayout()
        content_widget = QGroupBox("Main Content")
        content_widget.setLayout(content)
        content.addWidget(QLabel("Welcome to the main area!"))
        content.addWidget(QPushButton("Action 1"))
        main_layout.addWidget(content_widget)


app = QApplication([])
win = SectionedGUI()
win.show()
app.exec()
