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