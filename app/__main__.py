import asyncio
import logging

from app.bootstrap import create_application

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


async def main():
    application = create_application()

    application.start()

    print("🚀 Job Hunter started")

    try:
        await asyncio.Event().wait()
    except (KeyboardInterrupt, asyncio.CancelledError):
        pass
    finally:
        await application.stop()


if __name__ == "__main__":
    asyncio.run(main())