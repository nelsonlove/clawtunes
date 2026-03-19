# apple-music-py

Python library and CLI for controlling Apple Music on macOS.

## Features

- Play songs, albums, and playlists by name with interactive selection
- Playback controls: pause, resume, next, previous
- Now-playing status with progress bar
- Volume control with relative adjustments, mute/unmute
- Shuffle and repeat mode control
- Search local library and Apple Music catalog
- Love/dislike tracks
- Playlist management: create, add songs, remove songs
- AirPlay device selection
- Non-interactive mode (`-N`) and auto-select first match (`-1`)

## Installation

```bash
pip install apple-music-py  # or: pipx install apple-music-py
```

Requires macOS with Apple Music and Python 3.10+.

## CLI

```bash
apple-music --help
apple-music play song "Bohemian Rhapsody"
apple-music play album "Abbey Road"
apple-music play playlist "Chill Vibes"
apple-music status
apple-music pause
apple-music resume
apple-music next
apple-music prev
apple-music volume          # show current
apple-music volume 50       # set to 50%
apple-music volume +10      # relative adjust
apple-music mute
apple-music unmute
apple-music shuffle on
apple-music repeat all      # off | all | one
apple-music search "yesterday" -p  # include playlists
apple-music love
apple-music playlists
apple-music playlist create "Road Trip"
apple-music playlist add "Road Trip" "Kickstart My Heart"
apple-music airplay
apple-music airplay "HomePod"
apple-music catalog search "Bowie Heroes"
apple-music -1 play song "love"   # auto-select first match
```

## Python API

```python
from apple_music import MusicClient

client = MusicClient()
now = client.now_playing()          # NowPlaying | None
songs = client.search_songs("query")  # list of (id, display_text)
client.pause()
client.resume()
client.set_volume(75)
client.mute()
playlists = client.list_playlists()
devices = client.airplay_devices()
```

## Development

```bash
git clone https://github.com/nelsonlove/apple-music-py.git
cd apple-music-py
uv sync --extra dev
uv run pytest
uv run apple-music --help
```

## License

MIT
