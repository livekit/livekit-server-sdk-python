# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2023-05-01

### Changed

- Updated LiveKit protocol to v1.5.4
- **BREAKING**: Reorganized the package into submodules.
  The new modules are friendlier re-exports of everything from the protocol, e.g. `livekit.models`.
  The twirp servers and clients (such as `EgressServer`) can be found in `livekit.twirp`.
- **BREAKING**: `DataPacketKind` removed in favour of `models.DataPacket.Kind` directly from the protocol models.
  Use the constants `DataPacket.RELIABLE` and `DataPacket.LOSSY`.
- **BREAKING**: `livekit.utils` has been made private (by renaming it to `_utils`)

### Meta

- Updated pre-commit hooks
- Add GitHub Actions for isort and black

## [0.4.1] - 2022-12-16

### Changed

- Updated LiveKit protocol to v1.3.0

## [0.4.0] - 2022-12-01

### Added

- Added `name` argument to `AccessToken`. This is assigned by LiveKit to the `name` of the `ParticipantInfo` object.
  (See [#1](https://github.com/tradablebits/livekit-server-sdk-python/issues/1))

### Changed

- Updated LiveKit protocol to v1.2.3

### Meta

- Use a git submodule for `protocol` to pin a specific LiveKit protocol release.
- add `pre-commit` dev dependency

## [0.3.2] - 2022-05-27

### Fixed

- Actually fix proto and twirp modules not importing correctly :^)

## [0.3.1] - 2022-05-27 (yanked)

### Fixed

- fix proto and twirp modules not importing correctly

## [0.3.0] - 2022-05-27 (yanked)

### Changed

- Updated LiveKit protocol to v0.13.2

### Meta

- Changed build system from flit to setuptools
- Added [pre-commit](https://pre-commit.com/) hooks
- Fix tox issue from setuptools

## [0.2.4] - 2022-03-17

### Changed

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

[Unreleased]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v1.0.0...HEAD

[1.0.0]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.4.1...v1.0.0

[0.4.1]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.4.0...v0.4.1

[0.4.0]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.3.2...v0.4.0

[0.3.2]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.3.1...v0.3.2

[0.3.1]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.3.0...v0.3.1

[0.3.0]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.2.4...v0.3.0

[0.2.4]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.2.3...v0.2.4

[0.2.3]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.2.2...v0.2.3

[0.2.2]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.2.1...v0.2.2

[0.2.1]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.2.0...v0.2.1

[0.2.0]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.1.1...v0.2.0

[0.1.1]: https://github.com/tradablebits/livekit-server-sdk-python/compare/v0.1.0...v0.1.1

[0.1.0]: https://github.com/tradablebits/livekit-server-sdk-python/releases/tag/v0.1.0
