import httpx

from app.collectors.http_collector import HttpJobOfferCollector


def create_http_client(html: str) -> httpx.Client:
    transport = httpx.MockTransport(
        lambda request: httpx.Response(
            status_code=200,
            text=html,
        )
    )

    return httpx.Client(transport=transport)


def test_collect_job_offers():
    html = """
    <html>
        <body>
            <div
                data-job-offer
                data-title="Fullstack Developer"
                data-company="Tech Company"
                data-url="https://example.com/jobs/123"
            ></div>

            <div
                data-job-offer
                data-title="Java Developer"
                data-company="Another Company"
                data-url="https://example.com/jobs/456"
            ></div>
        </body>
    </html>
    """

    client = create_http_client(html)

    collector = HttpJobOfferCollector(
        url="https://example.com/jobs",
        client=client,
    )

    offers = collector.collect()

    assert len(offers) == 2

    assert offers[0].title == "Fullstack Developer"
    assert offers[0].company == "Tech Company"
    assert offers[0].url == "https://example.com/jobs/123"

    assert offers[1].title == "Java Developer"
    assert offers[1].company == "Another Company"


def test_collect_ignores_invalid_offers():
    html = """
    <html>
        <body>
            <div
                data-job-offer
                data-title="Valid Offer"
                data-company="Tech Company"
                data-url="https://example.com/jobs/123"
            ></div>

            <div
                data-job-offer
                data-title="Missing Company"
                data-url="https://example.com/jobs/456"
            ></div>
        </body>
    </html>
    """

    client = create_http_client(html)

    collector = HttpJobOfferCollector(
        url="https://example.com/jobs",
        client=client,
    )

    offers = collector.collect()

    assert len(offers) == 1
    assert offers[0].title == "Valid Offer"


def test_collect_raises_for_http_error():
    transport = httpx.MockTransport(
        lambda request: httpx.Response(
            status_code=500,
            text="Internal Server Error",
        )
    )

    client = httpx.Client(transport=transport)

    collector = HttpJobOfferCollector(
        url="https://example.com/jobs",
        client=client,
    )

    try:
        collector.collect()
        assert False, "Expected HTTPStatusError"
    except httpx.HTTPStatusError:
        pass