import sys

from pagebridge.reader import read_website


def main():
    if len(sys.argv) != 2:
        print('Usage: python main.py "https://example.com"')
        return

    try:
        result = read_website(sys.argv[1])

        print("\nPAGEBRIDGE")
        print("=" * 50)
        print("URL:", result.url)
        print("\nCONTENT")
        print(result.content)

    except (ValueError, OSError) as error:
        print("PageBridge error:", error)

    except Exception as error:
        print("Unexpected error:", error)


if __name__ == "__main__":
    main()