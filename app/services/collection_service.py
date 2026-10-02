from app.collectors.base import JobOfferCollector
from app.models.job_offer import JobOffer
from app.services.job_offer_service import JobOfferService


class CollectionService:

    def __init__(self, job_offer_service: JobOfferService):
        self.job_offer_service = job_offer_service

    def collect(self, collector: JobOfferCollector) -> list[JobOffer]:
        offers = collector.collect()

        new_offers = []

        for offer in offers:
            saved_offer = self.job_offer_service.save_if_new(offer)

            if saved_offer is not None:
                new_offers.append(saved_offer)

        return new_offers