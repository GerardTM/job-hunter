from app.collectors.base import JobOfferCollector
from app.services.job_offer_service import JobOfferService


class CollectionService:

    def __init__(self, job_offer_service: JobOfferService):
        self.job_offer_service = job_offer_service

    def collect(self, collector: JobOfferCollector) -> int:
        offers = collector.collect()

        new_offers = 0

        for offer in offers:
            saved_offer = self.job_offer_service.save_if_new(offer)

            if saved_offer is not None:
                new_offers += 1

        return new_offers