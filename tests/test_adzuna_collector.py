import httpx

from app.collectors.adzuna_collector import AdzunaCollector
from app.config.search import SearchConfig


def create_http_client(response_data: dict) -> httpx.Client:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            status_code=200,
            json=response_data,
        )

    transport = httpx.MockTransport(handler)

    return httpx.Client(transport=transport)


def test_collect_maps_adzuna_jobs():
    response_data = {
        "results": [
            {
                "id": 123,
                "title": "Fullstack Developer",
                "company": {
                    "display_name": "Tech Company",
                },
                "location": {
                    "display_name": "Rennes",
                },
                "description": "Java / Angular developer",
                "created": "2026-10-01T10:30:00Z",
                "redirect_url": "https://example.com/jobs/123",
            }
        ]
    }

    client = create_http_client(response_data)

    collector = AdzunaCollector(
        app_id="test-id",
        app_key="test-key",
        search_config=SearchConfig(
            keywords=["fullstack developer"],
            locations=["Rennes"],
        ),
        client=client,
    )

    offers = collector.collect()

    assert len(offers) == 1

    offer = offers[0]

    assert offer.title == "Fullstack Developer"
    assert offer.company == "Tech Company"
    assert offer.location == "Rennes"
    assert offer.url == "https://example.com/jobs/123"
    assert offer.source == "adzuna"
    assert offer.source_id == "123"
    assert offer.description == "Java / Angular developer"
    assert offer.published_at is not None


def test_collect_returns_empty_list_when_no_results():
    response_data = {
        "results": []
    }

    client = create_http_client(response_data)

    collector = AdzunaCollector(
        app_id="test-id",
        app_key="test-key",
        search_config=SearchConfig(),
        client=client,
    )

    offers = collector.collect()

    assert offers == []


def test_collect_supports_missing_optional_fields():
    response_data = {
        "results": [
            {
                "id": 123,
                "title": "Developer",
                "company": {},
                "location": {},
                "redirect_url": "https://example.com/jobs/123",
            }
        ]
    }

    client = create_http_client(response_data)

    collector = AdzunaCollector(
        app_id="test-id",
        app_key="test-key",
        search_config=SearchConfig(),
        client=client,
    )

    offers = collector.collect()

    assert len(offers) == 1
    assert offers[0].title == "Developer"
    assert offers[0].company == "Unknown"
    assert offers[0].location is None
    assert offers[0].published_at is None