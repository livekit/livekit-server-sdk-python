# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- BREAKING: added `RoomServiceClient` wrapper class
    - Wrapper around the generated twirp `RoomServiceClient`
    - Has nicer API which is more similar to the official JavaScript LiveKit Server SDK.
    - This is a breaking change because generated `RoomServiceClient` used to be exposed directly.

### Changed

- build: add check for isort command

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

[Unreleased]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.1.1...HEAD

[0.2.0]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.2.0...v0.1.1

[0.1.1]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.1.0...v0.1.1

[0.1.0]: https://github.com/tradablebits/livekit-server-sdk-python/releases/tag/v0.1.0
