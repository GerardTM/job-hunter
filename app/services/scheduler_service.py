import asyncio
import logging
from collections.abc import Awaitable, Callable

logger = logging.getLogger(__name__)


class SchedulerService:

    def __init__(
        self,
        task: Callable[[], Awaitable[None]],
        interval_seconds: float,
    ):
        if interval_seconds <= 0:
            raise ValueError("interval_seconds must be greater than 0")

        self.task = task
        self.interval_seconds = interval_seconds
        self._running = False
        self._stop_event = asyncio.Event()

    @property
    def is_running(self) -> bool:
        return self._running

    async def run(self) -> None:
        self._running = True
        self._stop_event.clear()

        try:
            while self._running:
                try:
                    await self.task()
                except Exception:
                    logger.exception("Scheduled task failed")

                if self._running:
                    await self._wait_for_next_run()
        finally:
            self._running = False

    async def _wait_for_next_run(self) -> None:
        try:
            await asyncio.wait_for(
                self._stop_event.wait(),
                timeout=self.interval_seconds,
            )
        except TimeoutError:
            pass

    def stop(self) -> None:
        self._running = False
        self._stop_event.set()