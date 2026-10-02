from datetime import datetime

import httpx

from app.collectors.base import JobOfferCollector
from app.models.job_offer import JobOffer


class AdzunaCollector(JobOfferCollector):

    BASE_URL = "https://api.adzuna.com/v1/api/jobs"

    def __init__(
        self,
        app_id: str,
        app_key: str,
        country: str = "fr",
        page: int = 1,
        results_per_page: int = 20,
        what: str | None = None,
        where: str | None = None,
        client: httpx.Client | None = None,
    ):
        self.app_id = app_id
        self.app_key = app_key
        self.country = country
        self.page = page
        self.results_per_page = results_per_page
        self.what = what
        self.where = where
        self.client = client or httpx.Client(timeout=10)

    def collect(self) -> list[JobOffer]:
        url = (
            f"{self.BASE_URL}/"
            f"{self.country}/search/"
            f"{self.page}"
        )

        params = {
            "app_id": self.app_id,
            "app_key": self.app_key,
            "results_per_page": self.results_per_page,
            "content-type": "application/json",
        }

        if self.what:
            params["what"] = self.what

        if self.where:
            params["where"] = self.where

        response = self.client.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        return [
            self._map_job_offer(job)
            for job in data.get("results", [])
        ]

    def _map_job_offer(self, job: dict) -> JobOffer:
        location = job.get("location") or {}
        company = job.get("company") or {}

        published_at = None

        if job.get("created"):
            published_at = datetime.fromisoformat(job["created"])

        return JobOffer(
            title=job["title"],
            company=company.get("display_name", "Unknown"),
            location=location.get("display_name"),
            url=job["redirect_url"],
            source="adzuna",
            source_id=str(job["id"]),
            description=job.get("description"),
            published_at=published_at,
        )