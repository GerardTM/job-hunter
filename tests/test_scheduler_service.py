
import pytest

from app.services.scheduler_service import SchedulerService


@pytest.mark.asyncio
async def test_scheduler_executes_task():
    executions = 0

    async def task():
        nonlocal executions
        executions += 1

        if executions >= 2:
            scheduler.stop()

    scheduler = SchedulerService(
        task=task,
        interval_seconds=0.01,
    )

    await scheduler.run()

    assert executions == 2
    assert not scheduler.is_running


@pytest.mark.asyncio
async def test_scheduler_can_be_stopped():
    async def task():
        scheduler.stop()

    scheduler = SchedulerService(
        task=task,
        interval_seconds=0.01,
    )

    await scheduler.run()

    assert not scheduler.is_running


@pytest.mark.asyncio
async def test_scheduler_continues_after_task_error():
    executions = 0

    async def task():
        nonlocal executions
        executions += 1

        if executions == 1:
            raise RuntimeError("Test error")

        scheduler.stop()

    scheduler = SchedulerService(
        task=task,
        interval_seconds=0.01,
    )

    await scheduler.run()

    assert executions == 2
    assert not scheduler.is_running


def test_scheduler_rejects_invalid_interval():
    async def task():
        pass

    with pytest.raises(ValueError):
        SchedulerService(
            task=task,
            interval_seconds=0,
        )