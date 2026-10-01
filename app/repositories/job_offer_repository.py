from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.job_offer import JobOffer


class JobOfferRepository:

    def __init__(self, session: Session):
        self.session = session

    def save(self, job_offer: JobOffer) -> JobOffer:
        self.session.add(job_offer)
        self.session.commit()
        self.session.refresh(job_offer)

        return job_offer

    def find_all(self) -> list[JobOffer]:
        statement = select(JobOffer).order_by(JobOffer.discovered_at.desc())

        return list(self.session.scalars(statement).all())

    def find_by_url(self, url: str) -> JobOffer | None:
        statement = select(JobOffer).where(JobOffer.url == url)

        return self.session.scalar(statement)

    def exists_by_url(self, url: str) -> bool:
        return self.find_by_url(url) is not None

    def delete(self, job_offer: JobOffer) -> None:
        self.session.delete(job_offer)
        self.session.commit()