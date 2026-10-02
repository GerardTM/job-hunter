from pathlib import Path

from app.system.paths import AppPaths


def test_data_directory_exists():
    path = AppPaths.data_dir()

    assert isinstance(path, Path)
    assert path.exists()
    assert path.is_dir()


def test_database_path():
    path = AppPaths.database_path()

    assert path.name == "job_hunter.db"
    assert path.parent == AppPaths.data_dir()


def test_search_config_path():
    path = AppPaths.search_config_path()

    assert path.name == "search.json"
    assert path.parent == AppPaths.data_dir()