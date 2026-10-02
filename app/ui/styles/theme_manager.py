from PySide6.QtCore import QObject, Signal

from app.ui.styles.colors import set_theme
from app.ui.styles.theme import get_dark_theme, get_light_theme


class ThemeManager(QObject):
    theme_changed = Signal(bool)

    def __init__(self):
        super().__init__()

        self._dark = False

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

        self.theme_changed.emit(dark)

    def stylesheet(self) -> str:
        return (
            get_dark_theme()
            if self._dark
            else get_light_theme()
        )