from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from app.services.application_service import ApplicationService
from app.services.job_hunter_service import JobHunterService


class MainWindow(QMainWindow):

    def __init__(
        self,
        application_service: ApplicationService,
        job_hunter_service: JobHunterService,
    ):
        super().__init__()

        self.application_service = application_service
        self.job_hunter_service = job_hunter_service

        self.setWindowTitle("Job Hunter")
        self.resize(900, 600)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        title = QLabel("Job Hunter")
        status = QLabel(self._get_status_text())

        offer_count = QLabel(
            f"Total offers: {self.job_hunter_service.get_offer_count()}"
        )

        layout.addWidget(title)
        layout.addWidget(status)
        layout.addWidget(offer_count)

        latest_offers = self.job_hunter_service.get_latest_offers()

        for offer in latest_offers:
            label = QLabel(
                f"{offer.title} — {offer.company}"
            )

            layout.addWidget(label)

        self.setCentralWidget(central_widget)

    def _get_status_text(self) -> str:
        if self.application_service.is_running:
            return "● Monitoring is running"

        return "● Monitoring is stopped"