import httpx

from pagebridge.extractor import extract_content
from pagebridge.models import PageResult
from pagebridge.security import validate_url


def read_website(url):
    validate_url(url)

    with httpx.Client(
        timeout=15,
        follow_redirects=False,
        headers={"User-Agent": "PageBridge/0.1"},
    ) as client:

        current_url = url

        for _ in range(6):
            validate_url(current_url)

            response = client.get(current_url)

            if response.is_redirect:
                location = response.headers.get("location")

                if not location:
                    raise ValueError("Redirect has no destination.")

                current_url = str(
                    response.url.join(location)
                )
                continue

            response.raise_for_status()

            content_type = response.headers.get(
                "content-type", ""
            )

            if "text/html" not in content_type.lower():
                raise ValueError("The URL did not return HTML.")

            html = response.text
            content = extract_content(html)

            if not content:
                raise ValueError("No readable content was found.")

            return PageResult(
                url=str(response.url),
                title=str(response.url),
                content=content,
            )

        raise ValueError("Too many redirects.")