import asyncio
import logging

from app.services.job_hunter_service import JobHunterService

logger = logging.getLogger(__name__)


class CollectionRunner:

    def __init__(self, job_hunter_service: JobHunterService):
        self.job_hunter_service = job_hunter_service

    async def run(self) -> None:
        logger.info("Starting job collection")

        new_offers = await asyncio.to_thread(
            self.job_hunter_service.collect_jobs
        )

        logger.info(
            "Job collection completed: %d new offer(s)",
            new_offers,
        )