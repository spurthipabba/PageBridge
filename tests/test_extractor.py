from pagebridge.extractor import extract_content


def test_extracts_main_text():
    html = """
    <html>
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