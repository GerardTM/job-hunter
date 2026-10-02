from app.ui.styles.colors import DARK, LIGHT


def _build_theme(colors) -> str:
    return f"""
        QMainWindow {{
            background-color: {colors.BACKGROUND};
        }}

        QWidget#centralWidget {{
            background-color: {colors.BACKGROUND};
            color: {colors.TEXT_PRIMARY};
        }}

        QStackedWidget#pages {{
            background-color: {colors.BACKGROUND};
        }}

        QLabel {{
            color: {colors.TEXT_PRIMARY};
        }}

        QLineEdit,
        QSpinBox {{
            background-color: {colors.SURFACE};
            color: {colors.TEXT_PRIMARY};
            border: 1px solid {colors.BORDER_STRONG};
            border-radius: 8px;
            padding: 8px 10px;
        }}

        QLineEdit:focus,
        QSpinBox:focus {{
            border: 1px solid {colors.BRAND_600};
        }}

        QPushButton {{
            color: {colors.TEXT_PRIMARY};
        }}

        QScrollArea {{
            background-color: transparent;
            border: none;
        }}

        QScrollBar:vertical {{
            background-color: transparent;
            width: 8px;
            margin: 4px 0 4px 4px;
        }}

        QScrollBar::handle:vertical {{
            background-color: {colors.BORDER_STRONG};
            border-radius: 4px;
            min-height: 30px;
        }}

        QScrollBar::handle:vertical:hover {{
            background-color: {colors.TEXT_SUBTLE};
        }}

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {{
            height: 0;
        }}
    """


def get_light_theme() -> str:
    return _build_theme(LIGHT)


def get_dark_theme() -> str:
    return _build_theme(DARK)