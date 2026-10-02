from PySide6.QtCore import QObject, Signal

from app.config.app_settings import AppSettings
from app.ui.styles.colors import set_theme
from app.ui.styles.theme import get_dark_theme, get_light_theme


class ThemeManager(QObject):
    theme_changed = Signal(bool)

    def __init__(self, settings: AppSettings):
        super().__init__()

        self.settings = settings

        self._dark = settings.load_dark_mode()

        set_theme(self._dark)

    @property
    def is_dark(self) -> bool:
        return self._dark

    def toggle(self) -> None:
        self.set_dark(not self._dark)

    def set_dark(self, dark: bool) -> None:
        if self._dark == dark:
            return

        self._dark = dark

        set_theme(dark)
        self.settings.save_dark_mode(dark)

        self.theme_changed.emit(dark)

    def stylesheet(self) -> str:
        return (
            get_dark_theme()
            if self._dark
            else get_light_theme()
        )