from app.notifications.base import NotificationService


class ConsoleNotificationService(NotificationService):

    def notify(
        self,
        title: str,
        message: str,
        url: str | None = None,
    ) -> None:
        print(f"🔔 {title}")
        print(f"   {message}")

        if url:
            print(f"   URL: {url}")