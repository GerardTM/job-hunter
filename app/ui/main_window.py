from PySide6.QtWidgets import QMainWindow

from app.services.application_service import ApplicationService
from app.services.job_hunter_service import JobHunterService
from app.ui.pages.dashboard_page import DashboardPage
from app.ui.pages.search_page import SearchPage


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

        self.dashboard_page = DashboardPage(
            application_service=self.application_service,
            job_hunter_service=self.job_hunter_service,
        )

        self.search_page = SearchPage()

        self.setCentralWidget(self.dashboard_page)