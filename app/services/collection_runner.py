import asyncio
import logging

from app.notifications.base import NotificationService
from app.services.job_hunter_service import JobHunterService

logger = logging.getLogger(__name__)


class CollectionRunner:

    def __init__(
        self,
        job_hunter_service: JobHunterService,
        notification_service: NotificationService,
    ):
        self.job_hunter_service = job_hunter_service
        self.notification_service = notification_service

    async def run(self) -> None:
        logger.info("Starting job collection")

        new_offers = await asyncio.to_thread(
            self.job_hunter_service.collect_jobs
        )

        logger.info(
            "Job collection completed: %d new offer(s)",
            len(new_offers),
        )

        for offer in new_offers:
            self.notification_service.notify(
                title="New job offer",
                message=f"{offer.title} at {offer.company}",
                url=offer.url,
            )