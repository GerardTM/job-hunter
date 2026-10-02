from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from app.services.application_service import ApplicationService
from app.services.job_hunter_service import JobHunterService
from app.ui.components.job_offer_card import JobOfferCard


class JobsPage(QWidget):

    def __init__(
        self,
        application_service: ApplicationService,
        job_hunter_service: JobHunterService,
    ):
        super().__init__()

        self.application_service = application_service
        self.job_hunter_service = job_hunter_service

        self._setup_ui()
        self._apply_styles()

        self.application_service.collection_completed.connect(
            self._refresh_jobs
        )

    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(24)

        title = QLabel("Offres d'emploi")
        title.setObjectName("pageTitle")

        subtitle = QLabel(
            "Consultez les dernières offres détectées."
        )
        subtitle.setObjectName("pageSubtitle")

        layout.addWidget(title)
        layout.addWidget(subtitle)

        self.scroll_area = QScrollArea()
        self.scroll_area.setObjectName("jobsScrollArea")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        self.jobs_container = QWidget()
        self.jobs_container.setObjectName("jobsContainer")

        self.jobs_layout = QVBoxLayout(self.jobs_container)
        self.jobs_layout.setContentsMargins(0, 0, 8, 0)
        self.jobs_layout.setSpacing(10)

        self.scroll_area.setWidget(self.jobs_container)

        layout.addWidget(self.scroll_area)

        self._refresh_jobs()

    def _refresh_jobs(self) -> None:
        while self.jobs_layout.count():
            item = self.jobs_layout.takeAt(0)

            if item.widget() is not None:
                item.widget().deleteLater()

        offers = self.job_hunter_service.get_latest_offers(
            limit=100
        )

        if not offers:
            empty_label = QLabel(
                "Aucune offre d'emploi trouvée."
            )
            empty_label.setObjectName("emptyLabel")
            self.jobs_layout.addWidget(empty_label)
        else:
            for offer in offers:
                self.jobs_layout.addWidget(
                    JobOfferCard(offer)
                )

        self.jobs_layout.addStretch()

    def _apply_styles(self) -> None:
        self.setStyleSheet(
            """
            QWidget {
                background-color: #f8fafc;
                color: #0f172a;
            }

            QLabel#pageTitle {
                background-color: transparent;
                font-size: 28px;
                font-weight: 700;
                color: #0f172a;
            }

            QLabel#pageSubtitle {
                background-color: transparent;
                font-size: 14px;
                color: #64748b;
            }

            QScrollArea#jobsScrollArea {
                background-color: transparent;
                border: none;
            }

            QScrollArea#jobsScrollArea > QWidget > QWidget {
                background-color: transparent;
            }

            QWidget#jobsContainer {
                background-color: transparent;
            }

            QLabel#emptyLabel {
                background-color: transparent;
                padding: 24px;
                font-size: 14px;
                color: #94a3b8;
            }

            QScrollBar:vertical {
                background-color: transparent;
                width: 8px;
                margin: 4px 0 4px 4px;
            }

            QScrollBar::handle:vertical {
                background-color: #cbd5e1;
                border-radius: 4px;
                min-height: 30px;
            }

            QScrollBar::handle:vertical:hover {
                background-color: #94a3b8;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                height: 0;
            }
            """
        )