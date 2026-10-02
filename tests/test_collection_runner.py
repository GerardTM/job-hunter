import pytest

from app.services.collection_runner import CollectionRunner


class FakeJobHunterService:

    def __init__(self):
        self.call_count = 0

    def collect_jobs(self) -> int:
        self.call_count += 1
        return 3


@pytest.mark.asyncio
async def test_run_executes_job_collection():
    service = FakeJobHunterService()
    runner = CollectionRunner(service)

    await runner.run()

    assert service.call_count == 1