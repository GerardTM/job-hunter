from app.config.search_repository import SearchConfigRepository
from app.services.job_hunter_service import JobHunterService
from app.system.paths import AppPaths


def main():
    search_config_repository = SearchConfigRepository(
        AppPaths.search_config_path()
    )

    job_hunter_service = JobHunterService(
        search_config_repository
    )

    new_offers = job_hunter_service.collect_jobs()

    print(
        f"✅ Collection completed: {len(new_offers)} new offer(s)"
    )


if __name__ == "__main__":
    main()