from abc import ABC, abstractmethod

from app.models.job_offer import JobOffer


class JobOfferCollector(ABC):

    @abstractmethod
    def collect(self) -> list[JobOffer]:
        """Collect job offers from an external source."""
        raise NotImplementedError