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


class JobOfferCard(QFrame):

    def __init__(self, offer: JobOffer):
        super().__init__()

        self.offer = offer

        self.setObjectName("jobOfferCard")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(20)

        content_layout = QVBoxLayout()
        content_layout.setSpacing(5)

        title = QLabel(offer.title)
        title.setObjectName("jobOfferTitle")

        company = QLabel(offer.company)
        company.setObjectName("jobOfferCompany")

        location = QLabel(
            f"📍 {offer.location}"
            if offer.location
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