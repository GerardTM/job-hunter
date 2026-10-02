from PySide6.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget

from app.services.application_service import ApplicationService


class MainWindow(QMainWindow):

    def __init__(self, application_service: ApplicationService):
        super().__init__()

        self.application_service = application_service

        self.setWindowTitle("Job Hunter")
        self.resize(900, 600)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        title = QLabel("Job Hunter")
        status = QLabel(self._get_status_text())

        layout.addWidget(title)
        layout.addWidget(status)

        self.setCentralWidget(central_widget)

    def _get_status_text(self) -> str:
        if self.application_service.is_running:
            return "● Monitoring is running"

        return "● Monitoring is stopped"