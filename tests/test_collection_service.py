from datetime import UTC, datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.collectors.base import JobOfferCollector
from app.database import Base
from app.models.job_offer import JobOffer
from app.repositories.job_offer_repository import JobOfferRepository
from app.services.collection_service import CollectionService
from app.services.job_offer_service import JobOfferService


class FakeCollector(JobOfferCollector):

    def __init__(self, offers: list[JobOffer]):
        self.offers = offers

    def collect(self) -> list[JobOffer]:
        return self.offers


def create_collection_service() -> CollectionService:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    session_factory = sessionmaker(bind=engine)
    session = session_factory()

    repository = JobOfferRepository(session)
    job_offer_service = JobOfferService(repository)

    return CollectionService(job_offer_service)


def create_job_offer(url: str) -> JobOffer:
    return JobOffer(
        title="Fullstack Developer",
        company="Tech Company",
        location="Rennes",
        url=url,
        source="example",
        source_id=url.split("/")[-1],
        description="Fullstack Java / Angular developer",
        published_at=datetime.now(UTC),
    )


def test_collect_saves_new_offers():
    service = create_collection_service()

    offers = [
        create_job_offer("https://example.com/jobs/1"),
        create_job_offer("https://example.com/jobs/2"),
    ]

    collector = FakeCollector(offers)

    new_offers = service.collect(collector)

    assert new_offers == 2


def test_collect_ignores_duplicate_offers():
    service = create_collection_service()

    offer = create_job_offer("https://example.com/jobs/1")

    collector = FakeCollector([offer])

    first_collection = service.collect(collector)
    second_collection = service.collect(collector)

    assert first_collection == 1
    assert second_collection == 0


def test_collect_returns_zero_when_no_offers_are_found():
    service = create_collection_service()

    collector = FakeCollector([])

    new_offers = service.collect(collector)

    assert new_offers == 0