import json
from pathlib import Path

from app.config.search import SearchConfig


class SearchConfigRepository:

    def __init__(self, path: Path):
        self.path = path

    def save(self, config: SearchConfig) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)

        self.path.write_text(
            config.model_dump_json(indent=2),
            encoding="utf-8",
        )

    def load(self) -> SearchConfig:
        if not self.path.exists():
            return SearchConfig()

        data = json.loads(
            self.path.read_text(encoding="utf-8")
        )

        return SearchConfig.model_validate(data)