import asyncio

from app.services.job_hunter_service import JobHunterService


class CollectionRunner:

    def __init__(self, job_hunter_service: JobHunterService):
        self.job_hunter_service = job_hunter_service

    async def run(self) -> None:
        await asyncio.to_thread(
            self.job_hunter_service.collect_jobs
        )