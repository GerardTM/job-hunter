from app.notifications.console import ConsoleNotificationService


def test_console_notification(capsys):
    notification_service = ConsoleNotificationService()

    notification_service.notify(
        title="New job offer",
        message="Fullstack Developer at Tech Company",
        url="https://example.com/job/123",
    )

    captured = capsys.readouterr()

    assert "🔔 New job offer" in captured.out
    assert "Fullstack Developer at Tech Company" in captured.out
    assert "https://example.com/job/123" in captured.out

def test_console_notification_without_url(capsys):
    notification_service = ConsoleNotificationService()

    notification_service.notify(
        title="New job offer",
        message="Fullstack Developer at Tech Company",
    )

    captured = capsys.readouterr()

    assert "🔔 New job offer" in captured.out
    assert "Fullstack Developer at Tech Company" in captured.out
    assert "URL:" not in captured.out