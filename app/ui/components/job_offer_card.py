from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
)

from app.models.job_offer import JobOffer
from app.ui.styles.colors import get_colors


class JobOfferCard(QFrame):

    def __init__(self, offer: JobOffer):
        super().__init__()

        self.offer = offer

        self.setObjectName("jobOfferCard")

        self._setup_ui()
        self._apply_styles()

    def _setup_ui(self) -> None:
        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(20)

        content_layout = QVBoxLayout()
        content_layout.setSpacing(5)

        title = QLabel(self.offer.title)
        title.setObjectName("jobOfferTitle")

        company = QLabel(self.offer.company)
        company.setObjectName("jobOfferCompany")

        location = QLabel(
            f"📍 {self.offer.location}"
            if self.offer.location
            else "📍 Localisation non renseignée"
        )
        location.setObjectName("jobOfferLocation")

        content_layout.addWidget(title)
        content_layout.addWidget(company)
        content_layout.addWidget(location)

        layout.addLayout(content_layout)
        layout.addStretch()

        open_button = QPushButton("Ouvrir →")
        open_button.setObjectName("jobOfferButton")
        open_button.setCursor(Qt.CursorShape.PointingHandCursor)
        open_button.clicked.connect(self._open_offer)

        layout.addWidget(open_button)

    def _open_offer(self) -> None:
        QDesktopServices.openUrl(QUrl(self.offer.url))

    def _apply_styles(self) -> None:
        colors = get_colors()
        self.setStyleSheet(
            f"""
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
            """
        )