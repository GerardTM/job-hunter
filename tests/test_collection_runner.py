import pytest

from app.services.collection_runner import CollectionRunner


class FakeJobHunterService:

    def __init__(self, offers=None):
        self.call_count = 0
        self.offers = offers or []

    def collect_jobs(self) -> list:
        self.call_count += 1
        return self.offers


class FakeNotificationService:

    def __init__(self):
        self.notifications = []

    def notify(
        self,
        title: str,
        message: str,
        url: str | None = None,
    ) -> None:
        self.notifications.append(
            {
                "title": title,
                "message": message,
                "url": url,
            }
        )


def create_job_offer():
    return type(
        "JobOffer",
        (),
        {
            "title": "Fullstack Developer",
            "company": "Tech Company",
            "url": "https://example.com/jobs/1",
        },
    )()


@pytest.mark.asyncio
async def test_run_executes_job_collection():
    job_hunter_service = FakeJobHunterService(
        offers=[create_job_offer()]
    )
    notification_service = FakeNotificationService()

    runner = CollectionRunner(
        job_hunter_service,
        notification_service,
    )

    await runner.run()

    assert job_hunter_service.call_count == 1
    assert len(notification_service.notifications) == 1

    notification = notification_service.notifications[0]

    assert notification["title"] == "New job offer"
    assert notification["message"] == (
        "Fullstack Developer at Tech Company"
    )
    assert notification["url"] == "https://example.com/jobs/1"


@pytest.mark.asyncio
async def test_run_does_not_notify_when_no_new_offers():
    job_hunter_service = FakeJobHunterService()
    notification_service = FakeNotificationService()

    runner = CollectionRunner(
        job_hunter_service,
        notification_service,
    )

    await runner.run()

    assert job_hunter_service.call_count == 1
    assert notification_service.notifications == []