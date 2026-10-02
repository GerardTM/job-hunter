from app.collectors.adzuna_collector import AdzunaCollector
from app.collectors.base import JobOfferCollector
from app.config.search_repository import SearchConfigRepository
from app.config.settings import settings
from app.database import SessionLocal
from app.models.job_offer import JobOffer
from app.repositories.job_offer_repository import JobOfferRepository
from app.services.collection_service import CollectionService
from app.services.job_offer_service import JobOfferService


class JobHunterService:

    def __init__(
        self,
        search_config_repository: SearchConfigRepository,
    ):
        self.search_config_repository = search_config_repository

    def collect_jobs(self) -> list[JobOffer]:
        search_config = self.search_config_repository.load()

        collectors: list[JobOfferCollector] = [
            AdzunaCollector(
                app_id=settings.adzuna_app_id,
                app_key=settings.adzuna_app_key,
                search_config=search_config,
            )
        ]

        with SessionLocal() as session:
            repository = JobOfferRepository(session)
            job_offer_service = JobOfferService(repository)
            collection_service = CollectionService(job_offer_service)

            new_offers = []

            for collector in collectors:
                new_offers.extend(
                    collection_service.collect(collector)
                )

            return new_offers

    def get_offer_count(self) -> int:
        with SessionLocal() as session:
            repository = JobOfferRepository(session)
            job_offer_service = JobOfferService(repository)

            return job_offer_service.count()


    def get_latest_offers(self, limit: int = 10) -> list[JobOffer]:
        with SessionLocal() as session:
            repository = JobOfferRepository(session)
            job_offer_service = JobOfferService(repository)

            return job_offer_service.find_latest(limit)