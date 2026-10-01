from datetime import UTC, datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models.job_offer import JobOffer
from app.repositories.job_offer_repository import JobOfferRepository


def create_test_session():
    engine = create_engine("sqlite:///:memory:")

    Base.metadata.create_all(engine)

    session_factory = sessionmaker(bind=engine)

    return session_factory()


def create_job_offer() -> JobOffer:
    return JobOffer(
        title="Fullstack Developer",
        company="Tech Company",
        location="Rennes",
        url="https://example.com/jobs/123",
        source="example",
        source_id="123",
        description="Fullstack Java / Angular developer",
        published_at=datetime.now(UTC),
    )


def test_save_job_offer():
    session = create_test_session()
    repository = JobOfferRepository(session)

    job_offer = create_job_offer()

    saved_offer = repository.save(job_offer)

    assert saved_offer.id is not None
    assert saved_offer.title == "Fullstack Developer"


def test_find_by_url():
    session = create_test_session()
    repository = JobOfferRepository(session)

    job_offer = create_job_offer()

    repository.save(job_offer)

    result = repository.find_by_url(
        "https://example.com/jobs/123"
    )

    assert result is not None
    assert result.id == job_offer.id


def test_exists_by_url():
    session = create_test_session()
    repository = JobOfferRepository(session)

    job_offer = create_job_offer()

    repository.save(job_offer)

    assert repository.exists_by_url(
        "https://example.com/jobs/123"
    )

    assert not repository.exists_by_url(
        "https://example.com/jobs/456"
    )


def test_find_all():
    session = create_test_session()
    repository = JobOfferRepository(session)

    first_offer = create_job_offer()

    second_offer = JobOffer(
        title="Java Developer",
        company="Another Company",
        location="Brest",
        url="https://example.com/jobs/456",
        source="example",
        source_id="456",
    )

    repository.save(first_offer)
    repository.save(second_offer)

    results = repository.find_all()

    assert len(results) == 2