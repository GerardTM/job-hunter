from pathlib import Path

from app.config.search_repository import SearchConfigRepository
from app.notifications.desktop import DesktopNotificationService
from app.services.application_service import ApplicationService
from app.services.collection_runner import CollectionRunner
from app.services.job_hunter_service import JobHunterService

SEARCH_CONFIG_PATH = Path("search.json")


def create_application() -> ApplicationService:
    search_config_repository = SearchConfigRepository(
        SEARCH_CONFIG_PATH
    )

    job_hunter_service = JobHunterService(
        search_config_repository
    )

    notification_service = DesktopNotificationService()

    collection_runner = CollectionRunner(
        job_hunter_service,
        notification_service,
    )

    return ApplicationService(
        collection_runner=collection_runner,
        interval_seconds=900,
    )