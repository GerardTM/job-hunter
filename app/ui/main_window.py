from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QStackedWidget,
    QWidget,
)

from app.services.application_service import ApplicationService
from app.services.job_hunter_service import JobHunterService
from app.ui.components.sidebar import Sidebar
from app.ui.pages.dashboard_page import DashboardPage
from app.ui.pages.jobs_page import JobsPage
from app.ui.pages.search_page import SearchPage
from app.ui.styles.theme import get_light_theme


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
        self.resize(1100, 700)

        self._setup_ui()

    def _setup_ui(self) -> None:
        central_widget = QWidget()
        central_widget.setObjectName("centralWidget")

        layout = QHBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.sidebar = Sidebar()

        self.pages = QStackedWidget()
        self.pages.setObjectName("pages")

        self.dashboard_page = DashboardPage(
            application_service=self.application_service,
            job_hunter_service=self.job_hunter_service,
        )

        self.search_page = SearchPage()

        self.pages.addWidget(self.dashboard_page)

        self.jobs_page = JobsPage(
            application_service=self.application_service,
            job_hunter_service=self.job_hunter_service,
        )

        self.pages.addWidget(self.jobs_page)

        self.pages.addWidget(self.search_page)

        self.sidebar.page_changed.connect(
            self._change_page
        )

        layout.addWidget(self.sidebar)
        layout.addWidget(self.pages)

        self.setCentralWidget(central_widget)

        self._apply_styles()

    def _change_page(self, page_index: int) -> None:
        self.pages.setCurrentIndex(page_index)


    def _apply_styles(self) -> None:
        self.setStyleSheet(get_light_theme())