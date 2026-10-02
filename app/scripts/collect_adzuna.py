from pathlib import Path

from app.config.search_repository import SearchConfigRepository
from app.services.job_hunter_service import JobHunterService

SEARCH_CONFIG_PATH = Path("search.json")


def main():
    search_config_repository = SearchConfigRepository(
        SEARCH_CONFIG_PATH
    )

    job_hunter_service = JobHunterService(
        search_config_repository
    )

    new_offers = job_hunter_service.collect_jobs()

    print(f"✅ Collection completed: {new_offers} new offer(s)")


if __name__ == "__main__":
    main()