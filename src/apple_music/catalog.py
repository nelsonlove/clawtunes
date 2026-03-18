"""Search and open from Apple Music catalog using iTunes Search API."""

import json
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

ITUNES_SEARCH_URL = "https://itunes.apple.com/search"


def search_catalog(query: str, limit: int = 10) -> list[dict[str, Any]]:
    """Search Apple Music catalog using iTunes Search API.

    Returns list of song dicts with trackId, trackName, artistName, collectionName, trackViewUrl.
    """
    params = urllib.parse.urlencode(
        {
            "term": query,
            "media": "music",
            "entity": "song",
            "limit": limit,
        }
    )
    url = f"{ITUNES_SEARCH_URL}?{params}"

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
            results: list[dict[str, Any]] = data.get("results", [])
            return results
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError):
        return []


def format_catalog_results(results: list[dict[str, Any]]) -> list[tuple[str, str]]:
    """Convert API results to (trackViewUrl, display_text) tuples."""
    formatted = []
    for item in results:
        track_url = item.get("trackViewUrl", "")
        track_name = item.get("trackName", "Unknown")
        artist = item.get("artistName", "Unknown")
        album = item.get("collectionName", "Unknown")
        display = f"{track_name} - {artist} ({album})"
        formatted.append((track_url, display))
    return formatted


def open_catalog_track(track_url: str) -> bool:
    """Open a track URL in the Music app."""
    try:
        music_url = track_url.replace("https://", "music://")
        result = subprocess.run(
            ["open", music_url],
            capture_output=True,
            text=True,
        )
        return result.returncode == 0
    except Exception:
        return False
