from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from app.services.application_service import ApplicationService
from app.services.job_hunter_service import JobHunterService
from app.ui.components.job_offer_card import JobOfferCard
from app.ui.components.stat_card import StatCard
from app.ui.styles.colors import get_colors


class DashboardPage(QWidget):

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
            self._refresh_dashboard
        )

    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)

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

        self.offer_count_card = StatCard(
            title="Offres trouvées",
            value=str(
                self.job_hunter_service.get_offer_count()
            ),
            description="offres enregistrées",
        )

        self.monitoring_status_card = StatCard(
            title="Monitoring",
            value=(
                "Actif"
                if self.application_service.is_running
                else "Arrêté"
            ),
            description="surveillance des offres",
        )

        self.last_collection_card = StatCard(
            title="Dernière collecte",
            value="Jamais",
            description="dernière vérification",
        )

        stats_layout.addWidget(self.offer_count_card)
        stats_layout.addWidget(self.monitoring_status_card)
        stats_layout.addWidget(self.last_collection_card)

        stats_layout.setStretch(0, 1)
        stats_layout.setStretch(1, 1)
        stats_layout.setStretch(2, 1)

        layout.addLayout(stats_layout)

        latest_offers_title = QLabel("Dernières offres")
        latest_offers_title.setObjectName("sectionTitle")

        layout.addWidget(latest_offers_title)

        scroll_area = QScrollArea()
        scroll_area.setObjectName("offersScrollArea")
        scroll_area.setWidgetResizable(True)

        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        self.offers_container = QWidget()
        self.offers_container.setObjectName("offersContainer")

        self.offers_layout = QVBoxLayout(
            self.offers_container
        )

        self.offers_layout.setContentsMargins(
            0,
            0,
            8,
            0,
        )

        self.offers_layout.setSpacing(8)

        self._refresh_offers()

        scroll_area.setWidget(self.offers_container)

        layout.addWidget(scroll_area)
        layout.addStretch()

    def _refresh_dashboard(self) -> None:
        self._refresh_stats()
        self._refresh_offers()

    def _refresh_stats(self) -> None:
        self.offer_count_card.set_value(
            str(
                self.job_hunter_service.get_offer_count()
            )
        )

        self.monitoring_status_card.set_value(
            "Actif"
            if self.application_service.is_running
            else "Arrêté"
        )

        last_collection = (
            self.application_service.last_collection_at
        )

        self.last_collection_card.set_value(
            last_collection.astimezone().strftime(
                "%H:%M:%S"
            )
            if last_collection
            else "Jamais"
        )

    def _refresh_offers(self) -> None:
        while self.offers_layout.count():
            item = self.offers_layout.takeAt(0)

            if item.widget() is not None:
                item.widget().deleteLater()

        latest_offers = (
            self.job_hunter_service.get_latest_offers()
        )

        if not latest_offers:
            empty_label = QLabel(
                "Aucune offre trouvée."
            )

            empty_label.setObjectName("emptyLabel")

            self.offers_layout.addWidget(
                empty_label
            )

        else:
            for offer in latest_offers:
                offer_card = JobOfferCard(offer)

                self.offers_layout.addWidget(
                    offer_card
                )

        self.offers_layout.addStretch()

    def _apply_styles(self) -> None:
        colors = get_colors()
        self.setStyleSheet(
            f"""
            QWidget {{
                background-color: {colors.BACKGROUND};
                color: {colors.TEXT_PRIMARY};
            }}

            QLabel#pageTitle {{
                background-color: transparent;
                font-size: 28px;
                font-weight: 700;
                color: {colors.TEXT_PRIMARY};
            }}

            QLabel#pageSubtitle {{
                background-color: transparent;
                font-size: 14px;
                color: {colors.TEXT_MUTED};
            }}

            QLabel#sectionTitle {{
                background-color: transparent;
                font-size: 18px;
                font-weight: 700;
                color: {colors.TEXT_PRIMARY};
                margin-top: 8px;
            }}

            QFrame#statCard {{
                background-color: {colors.SURFACE};
                border: 1px solid {colors.BORDER};
                border-radius: 8px;
            }}

            QLabel#statCardTitle {{
                background-color: transparent;
                font-size: 13px;
                font-weight: 600;
                color: {colors.TEXT_SECONDARY};
            }}

            QLabel#statCardValue {{
                background-color: transparent;
                font-size: 24px;
                font-weight: 700;
                color: {colors.TEXT_PRIMARY};
            }}

            QLabel#statCardDescription {{
                background-color: transparent;
                font-size: 12px;
                color: {colors.TEXT_MUTED};
            }}

            QScrollArea#offersScrollArea {{
                background-color: transparent;
                border: none;
            }}

            QScrollArea#offersScrollArea > QWidget > QWidget {{
                background-color: transparent;
            }}

            QWidget#offersContainer {{
                background-color: transparent;
            }}

            QFrame#jobOfferCard {{
                background-color: {colors.SURFACE};
                border: 1px solid {colors.BORDER};
                border-radius: 12px;
            }}

            QLabel#jobOfferTitle {{
                background-color: transparent;
                font-size: 15px;
                font-weight: 700;
                color: {colors.TEXT_PRIMARY};
            }}

            QLabel#jobOfferCompany {{
                background-color: transparent;
                font-size: 13px;
                color: {colors.TEXT_SECONDARY};
            }}

            QLabel#jobOfferLocation {{
                background-color: transparent;
                font-size: 12px;
                color: {colors.TEXT_SUBTLE};
            }}

            QPushButton#jobOfferButton {{
                background-color: {colors.BRAND_600};
                color: {colors.SURFACE};
                border: none;
                border-radius: 8px;
                padding: 8px 14px;
                font-size: 13px;
                font-weight: 600;
            }}

            QPushButton#jobOfferButton:hover {{
                background-color: {colors.BRAND_700};
            }}

            QPushButton#jobOfferButton:pressed {{
                background-color: {colors.BRAND_700};
            }}

            QLabel#emptyLabel {{
                background-color: transparent;
                padding: 24px;
                font-size: 14px;
                color: {colors.TEXT_SUBTLE};
            }}
            """
        )