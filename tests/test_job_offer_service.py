from datetime import UTC, datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models.job_offer import JobOffer
from app.repositories.job_offer_repository import JobOfferRepository
from app.services.job_offer_service import JobOfferService


def create_test_service() -> JobOfferService:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    session_factory = sessionmaker(bind=engine)
    session = session_factory()

    repository = JobOfferRepository(session)

    return JobOfferService(repository)


def create_job_offer(url: str = "https://example.com/jobs/123") -> JobOffer:
    return JobOffer(
        title="Fullstack Developer",
        company="Tech Company",
        location="Rennes",
        url=url,
        source="example",
        source_id="123",
        description="Fullstack Java / Angular developer",
        published_at=datetime.now(UTC),
    )


def test_save_if_new_saves_new_offer():
    service = create_test_service()
    job_offer = create_job_offer()

    saved_offer = service.save_if_new(job_offer)

    assert saved_offer is not None
    assert saved_offer.id is not None
    assert saved_offer.url == job_offer.url


def test_save_if_new_rejects_duplicate_offer():
    service = create_test_service()

    first_offer = create_job_offer()
    second_offer = create_job_offer()

    first_saved = service.save_if_new(first_offer)
    second_saved = service.save_if_new(second_offer)

    assert first_saved is not None
    assert second_saved is None


def test_find_all():
    service = create_test_service()

    service.save_if_new(create_job_offer("https://example.com/jobs/123"))
    service.save_if_new(create_job_offer("https://example.com/jobs/456"))

    offers = service.find_all()

    assert len(offers) == 2


def test_find_by_url():
    service = create_test_service()

    job_offer = create_job_offer()
    service.save_if_new(job_offer)

    result = service.find_by_url(job_offer.url)

    assert result is not None
    assert result.url == job_offer.url


def test_find_by_url_returns_none_for_unknown_url():
    service = create_test_service()

    result = service.find_by_url("https://example.com/jobs/unknown")

    assert result is None