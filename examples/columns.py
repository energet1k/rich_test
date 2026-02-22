"""
This example shows how to display content in columns.

The data is pulled from https://randomuser.me
"""

import json
import urllib.parse
from urllib.request import urlopen

from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel


def get_content(user):
    """Extract text from user dict."""
    country = user["location"]["country"]
    name = f"{user['name']['first']} {user['name']['last']}"
    return f"[b]{name}[/b]\n[yellow]{country}"


console = Console()


def _safe_urlopen(url: str):
    """
    Open a URL only if it uses an allowed scheme (http or https).
    This mitigates Bandit B310 warnings about unrestricted URL schemes.
    """
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"Disallowed URL scheme: {parsed.scheme}")
    return urlopen(url)

users = json.loads(_safe_urlopen("https://randomuser.me/api/?results=30").read())["results"]
console.print(users, overflow="ignore", crop=False)
user_renderables = [Panel(get_content(user), expand=True) for user in users]
console.print(Columns(user_renderables))
