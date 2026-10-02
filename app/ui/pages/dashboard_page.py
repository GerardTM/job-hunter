import asyncio

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
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

        self.application_service.collection_failed.connect(
            self._show_collection_error
        )

    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)

        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(24)

        header_layout = QHBoxLayout()
        header_layout.setSpacing(16)

        title_layout = QVBoxLayout()
        title_layout.setSpacing(6)

        title = QLabel("Dashboard")
        title.setObjectName("pageTitle")

        subtitle = QLabel(
            "Surveillez les nouvelles offres d'emploi."
        )
        subtitle.setObjectName("pageSubtitle")

        title_layout.addWidget(title)
        title_layout.addWidget(subtitle)

        header_layout.addLayout(title_layout)
        header_layout.addStretch()

        self.refresh_button = QPushButton("↻  Actualiser")
        self.refresh_button.setObjectName("refreshButton")
        self.refresh_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )
        self.refresh_button.clicked.connect(
            self._collect_now
        )

        header_layout.addWidget(self.refresh_button)

        layout.addLayout(header_layout)

        self.status_label = QLabel()
        self.status_label.setObjectName("collectionStatus")
        self.status_label.hide()

        layout.addWidget(self.status_label)

        self.stats_layout = QGridLayout()
        self.stats_layout.setSpacing(16)

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

        self.stats_layout.addWidget(
            self.offer_count_card,
            0,
            0,
        )

        self.stats_layout.addWidget(
            self.monitoring_status_card,
            0,
            1,
        )

        self.stats_layout.addWidget(
            self.last_collection_card,
            0,
            2,
        )

        for column in range(3):
            self.stats_layout.setColumnStretch(
                column,
                1,
            )

        layout.addLayout(self.stats_layout)

        self._update_stats_layout()

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

    def _update_stats_layout(self) -> None:
        width = self.width()

        if width < 700:
            columns = 1
        elif width < 1050:
            columns = 2
        else:
            columns = 3

        cards = [
            self.offer_count_card,
            self.monitoring_status_card,
            self.last_collection_card,
        ]

        for index, card in enumerate(cards):
            row = index // columns
            column = index % columns

            self.stats_layout.addWidget(
                card,
                row,
                column,
            )

        for column in range(3):
            self.stats_layout.setColumnStretch(
                column,
                1 if column < columns else 0,
            )

    def _show_collection_success(self) -> None:
        last_collection = (
            self.application_service.last_collection_at
        )

        if last_collection:
            time = last_collection.astimezone().strftime(
                "%H:%M:%S"
            )

            self.status_label.setText(
                f"✓ Dernière collecte réussie à {time}"
            )

        self.status_label.setObjectName(
            "collectionStatusSuccess"
        )
        self.status_label.style().unpolish(
            self.status_label
        )
        self.status_label.style().polish(
            self.status_label
        )
        self.status_label.show()


    def _show_collection_error(
        self,
        error: str,
    ) -> None:
        self.status_label.setText(
            f"⚠ Échec de la collecte : {error}"
        )

        self.status_label.setObjectName(
            "collectionStatusError"
        )
        self.status_label.style().unpolish(
            self.status_label
        )
        self.status_label.style().polish(
            self.status_label
        )
        self.status_label.show()

    def _refresh_dashboard(self) -> None:
        self._refresh_stats()
        self._refresh_offers()
        self._show_collection_success()

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

    def refresh_theme(self) -> None:
        self._apply_styles()

        for card in self.offers_container.findChildren(JobOfferCard):
            card._apply_styles()

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self._update_stats_layout() 

    def _collect_now(self) -> None:
        self.refresh_button.setEnabled(False)
        self.refresh_button.setText("↻  Actualisation...")

        asyncio.create_task(
            self._run_manual_collection()
        )


    async def _run_manual_collection(self) -> None:
        try:
            await self.application_service.collect_now()
        finally:
            self.refresh_button.setEnabled(True)
            self.refresh_button.setText("↻  Actualiser")

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

            QPushButton#refreshButton {{
                background-color: {colors.BRAND_600};
                color: {colors.SURFACE};
                border: none;
                border-radius: 8px;
                padding: 9px 14px;
                font-size: 13px;
                font-weight: 600;
            }}

            QPushButton#refreshButton:hover {{
                background-color: {colors.BRAND_700};
            }}

            QPushButton#refreshButton:pressed {{
                background-color: {colors.BRAND_700};
            }}

            QPushButton#refreshButton:disabled {{
                background-color: {colors.BORDER};
                color: {colors.TEXT_MUTED};
            }}

            QLabel#collectionStatus {{
                background-color: transparent;
                font-size: 13px;
                padding: 8px 0;
            }}

            QLabel#collectionStatusSuccess {{
                background-color: transparent;
                color: #16a34a;
                font-size: 13px;
                padding: 8px 0;
            }}

            QLabel#collectionStatusError {{
                background-color: transparent;
                color: #dc2626;
                font-size: 13px;
                padding: 8px 0;
            }}
            """
        )