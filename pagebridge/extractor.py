import trafilatura


def extract_content(html):
    content = trafilatura.extract(html)

    if not content:
        return ""

    return content