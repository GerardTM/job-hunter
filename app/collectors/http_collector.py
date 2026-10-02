import httpx
from bs4 import BeautifulSoup

from app.collectors.base import JobOfferCollector
from app.models.job_offer import JobOffer


class HttpJobOfferCollector(JobOfferCollector):

    def __init__(
        self,
        url: str,
        client: httpx.Client | None = None,
    ):
        self.url = url
        self.client = client or httpx.Client(timeout=10)

    def collect(self) -> list[JobOffer]:
        response = self.client.get(self.url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        offers = []

        for element in soup.select("[data-job-offer]"):
            title = element.get("data-title")
            company = element.get("data-company")
            url = element.get("data-url")

            if not title or not company or not url:
                continue

            offers.append(
                JobOffer(
                    title=title,
                    company=company,
                    url=url,
                    source=self.url,
                )
            )

        return offers