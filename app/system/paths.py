import os
import platform
from pathlib import Path

APP_NAME = "JobHunter"


class AppPaths:

    @staticmethod
    def data_dir() -> Path:
        system = platform.system()

        if system == "Windows":
            base_dir = Path(
                os.environ.get(
                    "APPDATA",
                    Path.home() / "AppData" / "Roaming",
                )
            )
        elif system == "Darwin":
            base_dir = (
                Path.home()
                / "Library"
                / "Application Support"
            )
        else:
            base_dir = Path(
                os.environ.get(
                    "XDG_DATA_HOME",
                    Path.home() / ".local" / "share",
                )
            )

        path = base_dir / APP_NAME
        path.mkdir(parents=True, exist_ok=True)

        return path

    @classmethod
    def database_path(cls) -> Path:
        return cls.data_dir() / "job_hunter.db"

    @classmethod
    def search_config_path(cls) -> Path:
        return cls.data_dir() / "search.json"