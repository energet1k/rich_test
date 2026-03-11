from time import sleep
from urllib.request import urlopen
from urllib.parse import urlparse

from rich.progress import wrap_file

# Helper to ensure only safe URL schemes are used with urlopen
def _safe_urlopen(url: str, allowed_schemes: tuple = ("http", "https")):
    """
    Open a URL only if its scheme is in the allowed list.

    Args:
        url: The URL to open.
        allowed_schemes: Tuple of permitted URL schemes (default http, https).

    Returns:
        The response object from urllib.request.urlopen.

    Raises:
        ValueError: If the URL scheme is not permitted.
    """
    scheme = urlparse(url).scheme
    if scheme not in allowed_schemes:
        raise ValueError(f"Disallowed URL scheme: {scheme}")
    return urlopen(url)

# Read a URL with urlopen
response = _safe_urlopen("https://www.textualize.io")
# Get the size from the headers
size = int(response.headers["Content-Length"])

# Wrap the response so that it update progress

with wrap_file(response, size) as file:
    for line in file:
        print(line.decode("utf-8"), end="")
        sleep(0.1)
