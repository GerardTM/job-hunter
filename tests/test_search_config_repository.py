from pathlib import Path

from app.config.search import SearchConfig
from app.config.search_repository import SearchConfigRepository


def test_save_and_load_search_config(tmp_path: Path):
    path = tmp_path / "search.json"

    repository = SearchConfigRepository(path)

    config = SearchConfig(
        keywords=[
            "fullstack developer",
            "java developer",
        ],
        locations=[
            "Rennes",
            "Brest",
        ],
        results_per_page=20,
    )

    repository.save(config)

    loaded_config = repository.load()

    assert loaded_config == config


def test_load_returns_default_config_when_file_does_not_exist(
    tmp_path: Path,
):
    path = tmp_path / "search.json"

    repository = SearchConfigRepository(path)

    config = repository.load()

    assert config == SearchConfig()