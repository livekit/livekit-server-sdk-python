# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

## [0.2.4] - 2022-03-17

- updated LiveKit protocol to v0.11.13

## [0.2.3] - 2021-12-17

### Fixed

- permissions error for `get_participant`

## [0.2.2] - 2021-12-16

### Fixed

- permissions error for `remove_participant`

## [0.2.1] - 2021-12-15

### Changed

- add `metadata` parameter to `AccessToken` constructor

### Fixed

- add `room` permission for `update_participant` and `update_subscriptions` in `RoomServiceClient`.
  Fixes permissions denied error.

## [0.2.0] - 2021-12-14

### Added

- BREAKING: added `RoomServiceClient` wrapper class
    - Wrapper around the generated twirp `RoomServiceClient`
    - Has nicer API which is more similar to the official JavaScript LiveKit Server SDK.
    - This is a breaking change because generated `RoomServiceClient` used to be exposed directly.

### Changed

- build: add check for isort command
- AccessToken: make ttl not nullable and assert ttl > 0

### Meta

- test: add coverage and pytest-coverage. remove tox
- test: add tests for AccessToken

## [0.1.1] - 2021-12-10

### Fixed

- example: need to pass `headers` dictionary as keyword argument to `Context`

### Meta

- `dist` directory in `.gitignore`
- `LICENCE` file
- add `licence` to `pyproject.toml`
- add `python-requires` to `pyproject.toml`

## [0.1.0] - 2021-12-10

- Initial release
- [LiveKit protocol v0.11.0](https://github.com/livekit/protocol/releases/tag/v0.11.0)

[Unreleased]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.2.4...HEAD

[0.2.4]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.2.3...v0.2.4

[0.2.3]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.2.2...v0.2.3

[0.2.2]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.2.1...v0.2.2

[0.2.1]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.2.0...v0.2.1

[0.2.0]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.1.1...v0.2.0

[0.1.1]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.1.0...v0.1.1

[0.1.0]: https://github.com/tradablebits/livekit-server-sdk-python/releases/tag/v0.1.0
