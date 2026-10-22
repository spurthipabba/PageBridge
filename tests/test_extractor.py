
from pagebridge.extractor import extract_content, extract_title


def test_extracts_main_text():
    html = """
    <html>
        <head><title>PageBridge Test</title></head>
        <body>
            <main>
                <h1>PageBridge Test</h1>
                <p>This is readable content.</p>
            </main>
        </body>
    </html>
    """

    result = extract_content(html)

    assert "readable content" in result


def test_extracts_title():
    html = "<html><head><title>My Website</title></head></html>"

    assert extract_title(html) == "My Website"


def test_title_falls_back_to_heading():
    html = "<html><body><h1>Welcome</h1></body></html>"

    assert extract_title(html) == "Welcome"
