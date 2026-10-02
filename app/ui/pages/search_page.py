from PySide6.QtWidgets import QVBoxLayout, QWidget

from app.config.search_repository import SearchConfigRepository
from app.system.paths import AppPaths
from app.ui.components.search_config_form import SearchConfigForm


class SearchPage(QWidget):

    def __init__(self):
        super().__init__()

        self.search_config_repository = SearchConfigRepository(
            AppPaths.search_config_path()
        )

        self.search_config = (
            self.search_config_repository.load()
        )

        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(24)

        self.search_config_form = SearchConfigForm(
            self.search_config
        )

        self.search_config_form.saved.connect(
            self._save_search_config
        )

        layout.addWidget(self.search_config_form)
        layout.addStretch()

    def _save_search_config(self, config) -> None:
        self.search_config_repository.save(config)
        self.search_config = config