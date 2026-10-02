import asyncio

import pytest

from app.services.application_service import ApplicationService


class FakeCollectionRunner:

    def __init__(self):
        self.call_count = 0

    async def run(self) -> None:
        self.call_count += 1


@pytest.mark.asyncio
async def test_start_runs_scheduler():
    runner = FakeCollectionRunner()

    application = ApplicationService(
        collection_runner=runner,
        interval_seconds=60,
    )

    application.start()

    await asyncio.sleep(0)

    assert application.is_running
    assert runner.call_count == 1

    await application.stop()

    assert not application.is_running