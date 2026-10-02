from app.ui.styles.colors import get_colors


def get_light_theme() -> str:
    colors = get_colors()
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


def get_dark_theme() -> str:
    return """
        QMainWindow {
            background-color: #0f172a;
        }

        QWidget#centralWidget {
            background-color: #0f172a;
            color: #f8fafc;
        }

        QStackedWidget#pages {
            background-color: #0f172a;
        }

        QLabel {
            color: #f8fafc;
        }

        QLineEdit,
        QSpinBox {
            background-color: #1e293b;
            color: #f8fafc;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 8px 10px;
        }

        QLineEdit:focus,
        QSpinBox:focus {
            border: 1px solid #f43f5e;
        }

        QPushButton {
            color: #f8fafc;
        }

        QScrollArea {
            background-color: transparent;
            border: none;
        }

        QScrollBar:vertical {
            background-color: transparent;
            width: 8px;
            margin: 4px 0 4px 4px;
        }

        QScrollBar::handle:vertical {
            background-color: #475569;
            border-radius: 4px;
            min-height: 30px;
        }

        QScrollBar::handle:vertical:hover {
            background-color: #64748b;
        }

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {
            height: 0;
        }
    """