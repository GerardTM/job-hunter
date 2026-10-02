import json
from pathlib import Path


class AppSettings:
    def __init__(self, path: Path):
        self.path = path

    def load_dark_mode(self) -> bool:
        if not self.path.exists():
            return False

        try:
            data = json.loads(
                self.path.read_text(encoding="utf-8")
            )
        except json.JSONDecodeError:
            return False

        return bool(data.get("dark_mode", False))

    def save_dark_mode(self, dark: bool) -> None:
        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.path.write_text(
            json.dumps(
                {"dark_mode": dark},
                indent=2,
            ),
            encoding="utf-8",
        )