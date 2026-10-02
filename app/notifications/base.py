from abc import ABC, abstractmethod


class NotificationService(ABC):

    @abstractmethod
    def notify(
        self,
        title: str,
        message: str,
        url: str | None = None,
    ) -> None:
        """Send a desktop notification."""
        raise NotImplementedError