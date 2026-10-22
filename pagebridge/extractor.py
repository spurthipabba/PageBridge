
from bs4 import BeautifulSoup
import trafilatura


def extract_title(html):
    soup = BeautifulSoup(html, "html.parser")

    if soup.title and soup.title.string:
        return soup.title.string.strip()

    heading = soup.find("h1")

    if heading:
        return heading.get_text(" ", strip=True)

    return "Untitled page"


def extract_content(html):
    content = trafilatura.extract(html)

    if not content:
        return ""

    return content

