import asyncio
from datetime import UTC, datetime

from PySide6.QtCore import QObject, Signal

from app.services.collection_runner import CollectionRunner
from app.services.job_hunter_service import JobHunterService
from app.services.scheduler_service import SchedulerService


class ApplicationService(QObject):

    collection_completed = Signal()

    def __init__(
        self,
        collection_runner: CollectionRunner,
        interval_seconds: float = 900,
    ):
        super().__init__()

        self.collection_runner = collection_runner

        self.scheduler = SchedulerService(
            task=self._run_collection,
            interval_seconds=interval_seconds,
        )

        self._scheduler_task: asyncio.Task[None] | None = None

        self._last_collection_at: datetime | None = None

    @property
    def is_running(self) -> bool:
        return self.scheduler.is_running

    @property
    def last_collection_at(self) -> datetime | None:
        return self._last_collection_at

    @property
    def job_hunter_service(self) -> JobHunterService:
        return self.collection_runner.job_hunter_service

    async def _run_collection(self) -> None:
        await self.collection_runner.run()

        self._last_collection_at = datetime.now(UTC)

        self.collection_completed.emit()

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