from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout


class StatCard(QFrame):

    def __init__(
        self,
        title: str,
        value: str,
        description: str,
    ):
        super().__init__()

        self.setObjectName("statCard")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 18, 20, 18)
        layout.setSpacing(6)

        title_label = QLabel(title)
        title_label.setObjectName("statCardTitle")

        value_label = QLabel(value)
        value_label.setObjectName("statCardValue")

        description_label = QLabel(description)
        description_label.setObjectName("statCardDescription")

        layout.addWidget(title_label)
        layout.addWidget(value_label)
        layout.addWidget(description_label)