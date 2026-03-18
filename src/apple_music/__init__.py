"""Apple Music — Python library for controlling Apple Music on macOS."""

from .client import MusicClient
from .status import NowPlaying

__all__ = ["MusicClient", "NowPlaying"]
