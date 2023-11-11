This repo has been deprecated, it's been superceded by https://github.com/livekit/python-sdks/

# LiveKit Server SDK

![https://pypi.org/project/livekit-server-sdk-python/](https://img.shields.io/pypi/v/livekit-server-sdk-python.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

API Reference: https://docs.livekit.io/guides/server-api

## Examples

### Generate Access Token for a Client

```py
import livekit

grant = livekit.VideoGrant(room_join=True, room="My Cool Room")
access_token = livekit.AccessToken("<api key>", "<api secret>", grant=grant, identity="bob", name="Bob")
token = access_token.to_jwt()
```

### Using `RoomServiceClient`

```py
import livekit

client = livekit.RoomServiceClient("<host>", "<api key>", "<api secret>")
client.mute_published_track(
    room="<room name>",
    identity="Bob",
    track_sid="<track sid>",
    muted=True,
)
```

## Local Development

Make sure you clone with submodules:
```sh
$ git clone --recurse-submodules https://github.com/tradablebits/livekit-server-sdk-python.git
```
Or if you have already cloned:
```sh
$ git submodule update --init
```

### Dependencies

- golang >= 1.17
    - https://go.dev/doc/install
- protoc
    - Ubuntu: `sudo apt install protobuf-compiler`
- protoc-gen-twirpy
    - `go install github.com/verloop/twirpy/protoc-gen-twirpy@latest`
    - make sure `~/go/bin` is in your `$PATH`
- [pre-commit](https://pre-commit.com/)

### Environment Setup

Set up the python virtual environment:

```sh
$ python3 -m venv env
$ source env/bin/activate
$ pip install --editable '.[dev]'
$ pre-commit install
```

### Run tests

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
