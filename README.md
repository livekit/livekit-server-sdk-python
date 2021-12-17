# LiveKit Server SDK

![https://pypi.org/project/livekit-server-sdk-python/](https://img.shields.io/pypi/v/livekit-server-sdk-python.svg)

API Reference: https://docs.livekit.io/guides/server-api

## Examples

### Generate Access Token for a Client

```py
from livekit import AccessToken, VideoGrant

grant = VideoGrant(room_join=True, room="My Cool Room")
access_token = AccessToken("<api key>", "<api secret>", grant=grant, identity="Bob")
token = access_token.to_jwt()
```

### Using `RoomServiceClient`

```py
from livekit import RoomServiceClient

client = RoomServiceClient("<host>", "<api key>", "<api secret>")
client.mute_published_track(room="<room name>", track="<track sid>")
```

## Local Development

### Dependencies

- golang >= 1.17
    - https://go.dev/doc/install
- protoc
    - Ubuntu: `sudo apt install protobuf-compiler`
- protoc-gen-twirpy
    - `go install github.com/verloop/twirpy/protoc-gen-twirpy@latest`
    - make sure `~/go/bin` is in your `$PATH`

### Environment Setup:

```sh
$ python3 -m venv env
$ source env/bin/activate
$ pip install flit
$ flit install --symlink
```

### Run tests:

The `RoomServiceClient` tests require a running LiveKit server.
See the [LiveKit Getting Started](https://docs.livekit.io/guides/getting-started/) page.

The tests use the following environment variables to locate the LiveKit server.

```sh
export LIVEKIT_HOST='http://localhost:7880'
export LIVEKIT_API_KEY='<api key>'
export LIVEKIT_API_SECRET='<api secret>'
```

Run the tests:

```sh
$ pytest
```

### Updating `protocol`

The `build.sh` script pulls the latest tag and builds

```sh
$ ./bin/build.sh
```
