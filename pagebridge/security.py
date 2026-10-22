import ipaddress
import socket
from urllib.parse import urlparse


def validate_url(url):
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        raise ValueError("Only HTTP and HTTPS URLs are allowed.")

    if not parsed.hostname:
        raise ValueError("The URL must include a hostname.")

    if parsed.username or parsed.password:
        raise ValueError("URLs containing credentials are not allowed.")

    host = parsed.hostname

    try:
        addresses = socket.getaddrinfo(host, None)
    except socket.gaierror:
        raise ValueError("The hostname could not be resolved.")

    for address in addresses:
        ip = ipaddress.ip_address(address[4][0])

        if not ip.is_global:
            raise ValueError("The URL resolves to a non-public IP address.")

    return url