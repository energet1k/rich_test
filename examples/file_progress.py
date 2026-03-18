from time import sleep
from urllib.request import urlopen
from urllib.parse import urlparse

from rich.progress import wrap_file

# Read a URL with urlopen
def safe_urlopen(url: str):
    """
    Open a URL only if it uses an allowed scheme.

    Bandit rule B310 warns about using ``urlopen`` with unrestricted URLs,
    because schemes like ``file://`` can lead to unexpected file access.
    This helper validates that the URL scheme is either ``http`` or ``https``
    before delegating to :func:`urllib.request.urlopen`.
    """
    allowed_schemes = {"http", "https"}
    parsed = urlparse(url)
    if parsed.scheme.lower() not in allowed_schemes:
        raise ValueError(f"Disallowed URL scheme: {parsed.scheme}")
    return urlopen(url)

response = safe_urlopen("https://www.textualize.io")
# Get the size from the headers
size = int(response.headers["Content-Length"])
#uselsss comment

def add():
    a = 1
    return a + b

# Wrap the response so that it update progress

with wrap_file(response, size) as file:
    for line in file:
        print(line.decode("utf-8"), end="")
        sleep(0.1)
