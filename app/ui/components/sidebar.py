from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QButtonGroup,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.ui.styles.colors import Colors


class Sidebar(QWidget):
    page_changed = Signal(int)

    def __init__(self):
        super().__init__()

        self.setObjectName("sidebar")
        self.setFixedWidth(240)

        self._setup_ui()
        self._apply_styles()

    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 20, 16, 20)
        layout.setSpacing(8)

        logo = QLabel("Job Hunter")
        logo.setObjectName("sidebarLogo")

        subtitle = QLabel("Job monitoring")
        subtitle.setObjectName("sidebarSubtitle")

        layout.addWidget(logo)
        layout.addWidget(subtitle)

        layout.addSpacing(24)

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)
        self.button_group.idClicked.connect(self.page_changed.emit)

        self.dashboard_button = self._create_nav_button(
            "⌂  Dashboard",
            0,
        )

        self.jobs_button = self._create_nav_button(
            "▣  Offres",
            1,
        )

        self.search_button = self._create_nav_button(
            "⚙  Recherche",
            2,
        )

        layout.addWidget(self.dashboard_button)
        layout.addWidget(self.jobs_button)
        layout.addWidget(self.search_button)

        layout.addStretch()

        version = QLabel("Job Hunter v0.1.0")
        version.setObjectName("sidebarVersion")

        layout.addWidget(version)

        self.dashboard_button.setChecked(True)

    def _create_nav_button(
        self,
        text: str,
        page_index: int,
    ) -> QPushButton:
        button = QPushButton(text)

        button.setObjectName("sidebarButton")
        button.setCheckable(True)
        button.setCursor(Qt.CursorShape.PointingHandCursor)

        self.button_group.addButton(button, page_index)

        return button

    def _apply_styles(self) -> None:
        self.setStyleSheet(
            f"""
            QWidget#sidebar {{
                background-color: {Colors.SURFACE};
                border-right: 1px solid {Colors.BORDER};
            }}

            QLabel#sidebarLogo {{
                color: {Colors.TEXT_PRIMARY};
                font-size: 21px;
                font-weight: 800;
                padding-left: 8px;
            }}

            QLabel#sidebarSubtitle {{
                color: {Colors.TEXT_SUBTLE};
                font-size: 12px;
                padding-left: 8px;
            }}

            QPushButton#sidebarButton {{
                background-color: transparent;
                color: {Colors.TEXT_MUTED};
                border: none;
                border-radius: 10px;
                padding: 12px 14px;
                text-align: left;
                font-size: 14px;
                font-weight: 600;
            }}

            QPushButton#sidebarButton:hover {{
                background-color: {Colors.BRAND_SURFACE_HOVER};
                color: {Colors.BRAND_600};
            }}

            QPushButton#sidebarButton:checked {{
                background-color: {Colors.BRAND_SURFACE};
                color: {Colors.BRAND_600};
            }}

            QLabel#sidebarVersion {{
                color: {Colors.TEXT_SUBTLE};
                font-size: 11px;
                padding-left: 8px;
            }}
            """
        )