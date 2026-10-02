from pathlib import Path

from app.collectors.adzuna_collector import AdzunaCollector
from app.config.search_repository import SearchConfigRepository
from app.config.settings import settings
from app.database import SessionLocal
from app.repositories.job_offer_repository import JobOfferRepository
from app.services.collection_service import CollectionService
from app.services.job_offer_service import JobOfferService

SEARCH_CONFIG_PATH = Path("search.json")


def main():
    search_config_repository = SearchConfigRepository(
        SEARCH_CONFIG_PATH
    )

    search_config = search_config_repository.load()

    collector = AdzunaCollector(
        app_id=settings.adzuna_app_id,
        app_key=settings.adzuna_app_key,
        search_config=search_config,
    )

    with SessionLocal() as session:
        repository = JobOfferRepository(session)
        job_offer_service = JobOfferService(repository)
        collection_service = CollectionService(job_offer_service)

        new_offers = collection_service.collect(collector)

    print(f"✅ Collection completed: {new_offers} new offer(s)")


if __name__ == "__main__":
    main()