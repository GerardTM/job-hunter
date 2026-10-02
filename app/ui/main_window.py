from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from app.services.application_service import ApplicationService
from app.services.job_hunter_service import JobHunterService
from app.ui.components.job_offer_card import JobOfferCard
from app.ui.components.stat_card import StatCard


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

        self._setup_ui()
        self._apply_styles()

    def _setup_ui(self) -> None:
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(24)

        header_layout = QVBoxLayout()
        header_layout.setSpacing(6)

        title = QLabel("Dashboard")
        title.setObjectName("pageTitle")

        subtitle = QLabel(
            "Surveillez les nouvelles offres d'emploi."
        )
        subtitle.setObjectName("pageSubtitle")

        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)

        layout.addLayout(header_layout)

        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(16)

        offer_count = StatCard(
            title="Offres trouvées",
            value=str(self.job_hunter_service.get_offer_count()),
            description="offres enregistrées",
        )

        monitoring_status = StatCard(
            title="Monitoring",
            value=(
                "Actif"
                if self.application_service.is_running
                else "Arrêté"
            ),
            description="surveillance des offres",
        )

        stats_layout.addWidget(offer_count)
        stats_layout.addWidget(monitoring_status)

        layout.addLayout(stats_layout)

        latest_offers_title = QLabel("Dernières offres")
        latest_offers_title.setObjectName("sectionTitle")

        layout.addWidget(latest_offers_title)

        latest_offers = self.job_hunter_service.get_latest_offers()

        scroll_area = QScrollArea()
        scroll_area.setObjectName("offersScrollArea")
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        offers_container = QWidget()
        offers_container.setObjectName("offersContainer")

        offers_layout = QVBoxLayout(offers_container)
        offers_layout.setContentsMargins(0, 0, 8, 0)
        offers_layout.setSpacing(8)

        if not latest_offers:
            empty_label = QLabel("Aucune offre trouvée.")
            empty_label.setObjectName("emptyLabel")

            offers_layout.addWidget(empty_label)
        else:
            for offer in latest_offers:
                offer_card = JobOfferCard(offer)
                offers_layout.addWidget(offer_card)

        offers_layout.addStretch()

        scroll_area.setWidget(offers_container)

        layout.addWidget(scroll_area)
        layout.addStretch()

        self.setCentralWidget(central_widget)

    def _apply_styles(self) -> None:
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #f8fafc;
            }

            QLabel#pageTitle {
                font-size: 28px;
                font-weight: 700;
                color: #0f172a;
            }

            QLabel#pageSubtitle {
                font-size: 14px;
                color: #64748b;
            }

            QLabel#sectionTitle {
                font-size: 18px;
                font-weight: 700;
                color: #0f172a;
                margin-top: 8px;
            }

            QScrollArea#offersScrollArea {
                background-color: transparent;
                border: none;
            }

            QWidget#offersContainer {
                background-color: transparent;
            }

            QFrame#jobOfferCard {
                background-color: white;
                border: 1px solid #e2e8f0;
                border-radius: 12px;
            }

            QLabel#jobOfferTitle {
                font-size: 15px;
                font-weight: 700;
                color: #0f172a;
            }

            QLabel#jobOfferCompany {
                font-size: 13px;
                color: #475569;
            }

            QLabel#jobOfferLocation {
                font-size: 12px;
                color: #94a3b8;
            }

            QPushButton#jobOfferButton {
                background-color: #e11d48;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 14px;
                font-size: 13px;
                font-weight: 600;
            }

            QPushButton#jobOfferButton:hover {
                background-color: #be123c;
            }

            QPushButton#jobOfferButton:pressed {
                background-color: #9f1239;
            }

            QLabel#emptyLabel {
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