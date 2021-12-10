# LiveKit Server SDK

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
from livekit import (
    AccessToken,
    Context,
    MuteRoomTrackRequest,
    RoomServiceClient,
    VideoGrant,
)

# Create AccessToken with the needed permissions.
grant = VideoGrant(room_admin=True)
access_token = AccessToken("<api key>", "<api secret>", grant=grant)

# Initialize the client.
client = RoomServiceClient("<host>")

# Make a request using the client.
ctx = Context(headers={"Authorization": f"Bearer: {access_token.to_jwt()}"})
request = MuteRoomTrackRequest(room="<room name>", track="<track sid>")
client.MutePublishedTrack(ctx=ctx, request=request)
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

```sh
$ tox
# or for a specific python version:
$ tox -e py38
```

### Updating `protocol`

The `build.sh` script pulls the latest tag and builds

```sh
$ ./bin/build.sh
```
