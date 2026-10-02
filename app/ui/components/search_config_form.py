from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from app.config.search import SearchConfig
from app.ui.styles.colors import get_colors


class SearchConfigForm(QWidget):

    saved = Signal(SearchConfig)

    def __init__(self, config: SearchConfig):
        super().__init__()

        self.config = config

        self._setup_ui()
        self._apply_styles()
        self._load_config()

    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setSpacing(20)

        title = QLabel("Configuration de la recherche")
        title.setObjectName("formTitle")

        subtitle = QLabel(
            "Définissez les critères utilisés pour rechercher les offres."
        )
        subtitle.setObjectName("formSubtitle")

        layout.addWidget(title)
        layout.addWidget(subtitle)

        form_layout = QFormLayout()
        form_layout.setSpacing(14)

        self.keywords_input = QLineEdit()
        self.keywords_input.setPlaceholderText(
            "Ex: fullstack developer, java developer"
        )

        self.locations_input = QLineEdit()
        self.locations_input.setPlaceholderText(
            "Ex: Brest, Rennes, Nantes"
        )

        self.results_input = QSpinBox()
        self.results_input.setRange(1, 100)
        self.results_input.setValue(20)

        form_layout.addRow("Mots-clés", self.keywords_input)
        form_layout.addRow("Localisations", self.locations_input)
        form_layout.addRow("Nombre de résultats", self.results_input)

        layout.addLayout(form_layout)

        buttons_layout = QHBoxLayout()

        self.save_button = QPushButton("Enregistrer")
        self.save_button.setObjectName("saveButton")

        self.save_button.clicked.connect(self._save)

        buttons_layout.addStretch()
        buttons_layout.addWidget(self.save_button)

        layout.addLayout(buttons_layout)
        layout.addStretch()

    def _load_config(self) -> None:
        self.keywords_input.setText(
            ", ".join(self.config.keywords)
        )

        self.locations_input.setText(
            ", ".join(self.config.locations)
        )

        self.results_input.setValue(
            self.config.results_per_page
        )

    def _save(self) -> None:
        config = SearchConfig(
            keywords=self._parse_values(
                self.keywords_input.text()
            ),
            locations=self._parse_values(
                self.locations_input.text()
            ),
            results_per_page=self.results_input.value(),
        )

        self.saved.emit(config)

    @staticmethod
    def _parse_values(value: str) -> list[str]:
        return [
            item.strip()
            for item in value.split(",")
            if item.strip()
        ]

    def _apply_styles(self) -> None:
        colors = get_colors()
        self.setStyleSheet(
            f"""
            QLabel#formTitle {{
                background-color: transparent;
                font-size: 22px;
                font-weight: 700;
                color: {colors.TEXT_PRIMARY};
            }}

            QLabel#formSubtitle {{
                background-color: transparent;
                font-size: 14px;
                color: {colors.TEXT_MUTED};
            }}

            QLineEdit,
            QSpinBox {{
                background-color: {colors.SURFACE};
                color: {colors.TEXT_PRIMARY};
                padding: 8px 10px;
                border: 1px solid {colors.BORDER_STRONG};
                border-radius: 8px;
            }}

            QLineEdit:focus,
            QSpinBox:focus {{
                border: 1px solid {colors.BRAND_600};
            }}

            QPushButton#saveButton {{
                background-color: {colors.BRAND_600};
                color: {colors.SURFACE};
                border: none;
                border-radius: 8px;
                padding: 9px 18px;
                font-size: 13px;
                font-weight: 600;
            }}

            QPushButton#saveButton:hover {{
                background-color: {colors.BRAND_700};
            }}

            QPushButton#saveButton:pressed {{
                background-color: {colors.BRAND_700};
            }}
            """
        )