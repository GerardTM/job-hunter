from app.ui.styles.colors import Colors


def get_light_theme() -> str:
    return f"""
        QMainWindow {{
            background-color: {Colors.BACKGROUND};
        }}

        QWidget#centralWidget {{
            background-color: {Colors.BACKGROUND};
            color: {Colors.TEXT_PRIMARY};
        }}

        QStackedWidget#pages {{
            background-color: {Colors.BACKGROUND};
        }}

        QLabel {{
            color: {Colors.TEXT_PRIMARY};
        }}

        QLineEdit,
        QSpinBox {{
            background-color: {Colors.SURFACE};
            color: {Colors.TEXT_PRIMARY};
            border: 1px solid {Colors.BORDER_STRONG};
            border-radius: 8px;
            padding: 8px 10px;
        }}

        QLineEdit:focus,
        QSpinBox:focus {{
            border: 1px solid {Colors.BRAND_600};
        }}

        QPushButton {{
            color: {Colors.TEXT_PRIMARY};
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
            background-color: {Colors.BORDER_STRONG};
            border-radius: 4px;
            min-height: 30px;
        }}

        QScrollBar::handle:vertical:hover {{
            background-color: {Colors.TEXT_SUBTLE};
        }}

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {{
            height: 0;
        }}
    """