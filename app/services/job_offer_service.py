from app.models.job_offer import JobOffer
from app.repositories.job_offer_repository import JobOfferRepository


class JobOfferService:

    def __init__(self, repository: JobOfferRepository):
        self.repository = repository

    def save_if_new(self, job_offer: JobOffer) -> JobOffer | None:
        if (
            job_offer.source_id is not None
            and self.repository.find_by_source_id(
                job_offer.source,
                job_offer.source_id,
            )
        ):
            return None

        if self.repository.exists_by_url(job_offer.url):
            return None

        return self.repository.save(job_offer)

    def find_all(self) -> list[JobOffer]:
        return self.repository.find_all()

    def find_by_url(self, url: str) -> JobOffer | None:
        return self.repository.find_by_url(url)

    def count(self) -> int:
        return len(self.repository.find_all())

    def find_latest(self, limit: int = 10) -> list[JobOffer]:
        return self.repository.find_all()[:limit]