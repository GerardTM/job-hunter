from PySide6.QtWidgets import QMainWindow

from app.config.search_repository import SearchConfigRepository
from app.services.application_service import ApplicationService
from app.services.job_hunter_service import JobHunterService
from app.system.paths import AppPaths
from app.ui.pages.dashboard_page import DashboardPage


class MainWindow(QMainWindow):

    def __init__(
        self,
        application_service: ApplicationService,
        job_hunter_service: JobHunterService,
    ):
        super().__init__()

        self.application_service = application_service
        self.job_hunter_service = job_hunter_service

        self.search_config_repository = SearchConfigRepository(
            AppPaths.search_config_path()
        )

        self.search_config = (
            self.search_config_repository.load()
        )

        self.setWindowTitle("Job Hunter")
        self.resize(900, 600)

        self.dashboard_page = DashboardPage(
            application_service=self.application_service,
            job_hunter_service=self.job_hunter_service,
        )

        self.setCentralWidget(self.dashboard_page)