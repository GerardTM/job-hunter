import asyncio
import logging
import sys

from PySide6.QtWidgets import QApplication
from qasync import QEventLoop

from app.bootstrap import create_application
from app.ui.main_window import MainWindow

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logging.getLogger("httpx").setLevel(logging.WARNING)


async def main():
    application_service = create_application()

    application_service.start()

    await asyncio.sleep(0)

    window = MainWindow(application_service)
    window.show()

    print("🚀 Job Hunter started")

    try:
        await asyncio.Event().wait()
    except asyncio.CancelledError:
        pass
    finally:
        await application_service.stop()


if __name__ == "__main__":
    qt_application = QApplication(sys.argv)

    event_loop = QEventLoop(qt_application)
    asyncio.set_event_loop(event_loop)

    with event_loop:
        event_loop.run_until_complete(main())