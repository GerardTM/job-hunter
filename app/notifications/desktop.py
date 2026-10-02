from notifypy import Notify

from app.notifications.base import NotificationService


class DesktopNotificationService(NotificationService):

    def notify(
        self,
        title: str,
        message: str,
        url: str | None = None,
    ) -> None:
        notification = Notify()

        notification.application_name = "Job Hunter"
        notification.title = title
        notification.message = message

        if url:
            notification.launch = url

        notification.send()