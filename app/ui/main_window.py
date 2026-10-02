from PySide6.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Job Hunter")
        self.resize(900, 600)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        title = QLabel("Job Hunter")
        status = QLabel("● Monitoring is running")

        layout.addWidget(title)
        layout.addWidget(status)

        self.setCentralWidget(central_widget)