from PySide6.QtCore import QPropertyAnimation, Qt, Signal
from PySide6.QtWidgets import (
    QButtonGroup,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.ui.styles.colors import get_colors


class Sidebar(QWidget):
    page_changed = Signal(int)
    theme_toggle_requested = Signal()

    def __init__(self):
        super().__init__()

        self.setObjectName("sidebar")
        self.setFixedWidth(240)

        self._compact = False

        self._width_animation = QPropertyAnimation(
            self,
            b"minimumWidth",
            self,
        )
        self._width_animation.setDuration(180)

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

        self.theme_button = QPushButton("☾  Mode sombre")
        self.theme_button.setObjectName("themeButton")
        self.theme_button.setCheckable(False)
        self.theme_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.theme_button.clicked.connect(
            self.theme_toggle_requested.emit
        )

        layout.addWidget(self.theme_button)

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

    def set_dark_mode(self, dark: bool) -> None:
        if self._compact:
            self.theme_button.setText("☀" if dark else "☾")
        else:
            self.theme_button.setText(
                "☀  Mode clair" if dark else "☾  Mode sombre"
            )

        self._apply_styles()

    def set_compact(self, compact: bool) -> None:
        if self._compact == compact:
            return

        self._compact = compact

        target_width = 72 if compact else 240

        self._width_animation.stop()
        self._width_animation.setStartValue(self.width())
        self._width_animation.setEndValue(target_width)
        self._width_animation.start()

        self.setMinimumWidth(target_width)
        self.setMaximumWidth(target_width)

        layout = self.layout()

        if layout is not None:
            layout.setContentsMargins(
                8 if compact else 16,
                20,
                8 if compact else 16,
                20,
            )

        self.dashboard_button.setText(
            "⌂" if compact else "⌂  Dashboard"
        )
        self.jobs_button.setText(
            "▣" if compact else "▣  Offres"
        )
        self.search_button.setText(
            "⚙" if compact else "⚙  Recherche"
        )

        self._apply_styles()

    def _apply_styles(self) -> None:
        colors = get_colors()
        self.setStyleSheet(
            f"""
            QWidget#sidebar {{
                background-color: {colors.SURFACE};
                border-right: 1px solid {colors.BORDER};
            }}

            QLabel#sidebarLogo {{
                color: {colors.TEXT_PRIMARY};
                font-size: 21px;
                font-weight: 800;
                padding-left: 8px;
            }}

            QLabel#sidebarSubtitle {{
                color: {colors.TEXT_SUBTLE};
                font-size: 12px;
                padding-left: 8px;
            }}

            QPushButton#sidebarButton {{
                background-color: transparent;
                color: {colors.TEXT_MUTED};
                border: none;
                border-radius: 10px;
                padding: 12px 14px;
                text-align: left;
                font-size: 14px;
                font-weight: 600;
            }}

            QPushButton#sidebarButton:hover {{
                background-color: {colors.BRAND_SURFACE_HOVER};
                color: {colors.BRAND_600};
            }}

            QPushButton#sidebarButton:checked {{
                background-color: {colors.BRAND_SURFACE};
                color: {colors.BRAND_600};
            }}

            QPushButton#themeButton {{
                background-color: transparent;
                color: {colors.TEXT_MUTED};
                border: none;
                border-radius: 10px;
                padding: 12px 14px;
                text-align: left;
                font-size: 14px;
                font-weight: 600;
            }}

            QPushButton#themeButton:hover {{
                background-color: {colors.BRAND_SURFACE_HOVER};
                color: {colors.BRAND_600};
            }}

            QLabel#sidebarVersion {{
                color: {colors.TEXT_SUBTLE};
                font-size: 11px;
                padding-left: 8px;
            }}

            QPushButton#sidebarButton,
            QPushButton#themeButton {{
                min-height: 42px;
            }}
            """
        )