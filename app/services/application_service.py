import asyncio

from app.services.collection_runner import CollectionRunner
from app.services.scheduler_service import SchedulerService


class ApplicationService:

    def __init__(
        self,
        collection_runner: CollectionRunner,
        interval_seconds: float = 900,
    ):
        self.collection_runner = collection_runner
        self.scheduler = SchedulerService(
            task=self.collection_runner.run,
            interval_seconds=interval_seconds,
        )
        self._scheduler_task: asyncio.Task[None] | None = None

    @property
    def is_running(self) -> bool:
        return self.scheduler.is_running

    def start(self) -> None:
        if self._scheduler_task is not None:
            return

        self._scheduler_task = asyncio.create_task(
            self.scheduler.run()
        )

    async def stop(self) -> None:
        if self._scheduler_task is None:
            return

        self.scheduler.stop()

        await self._scheduler_task

        self._scheduler_task = None