from app.config.search_repository import SearchConfigRepository
from app.notifications.desktop import DesktopNotificationService
from app.services.application_service import ApplicationService
from app.services.collection_runner import CollectionRunner
from app.services.job_hunter_service import JobHunterService
from app.system.paths import AppPaths


def create_application() -> ApplicationService:
    search_config_repository = SearchConfigRepository(
        AppPaths.search_config_path()
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