#!/usr/bin/env bash
set -euo pipefail

cd "$( dirname "$( dirname "${BASH_SOURCE[0]}" )" )"
source bin/lib.sh

MODULE_ROOT="livekit"
PYTHON_OUT_DIR="$MODULE_ROOT/_proto"
TWIRP_OUT_DIR="$MODULE_ROOT/_twirp"
PROTO_DIR="protocol"  # where the .proto files are

# check for dependencies
if ! command -v protoc > /dev/null; then
  die "protoc not found"
fi
if ! command -v protoc-gen-twirpy > /dev/null; then
  die "protoc-gen-twirpy not found"
fi
if ! command -v black > /dev/null; then
  die "black not found"
fi
if ! command -v isort > /dev/null; then
  die "isort not found"
fi

if [ -d "$PYTHON_OUT_DIR" ]; then
  log_info "Cleaning directory $PYTHON_OUT_DIR"
  rm -rf "$PYTHON_OUT_DIR"
fi
if [ -d "$TWIRP_OUT_DIR" ]; then
  log_info "Cleaning directory $TWIRP_OUT_DIR"
  rm -rf "$TWIRP_OUT_DIR"
fi

PROTO_VERSION="$(git -C "$PROTO_DIR" describe --tags)"
log_info "protocol version: $PROTO_VERSION"

mkdir -p "$PYTHON_OUT_DIR" "$TWIRP_OUT_DIR"

log_info "Building proto files"
protoc -I "$PROTO_DIR" --python_out="$PYTHON_OUT_DIR" --pyi_out="$PYTHON_OUT_DIR" --twirpy_out="$TWIRP_OUT_DIR" "$PROTO_DIR"/*.proto
touch -a "$PYTHON_OUT_DIR/__init__.py"
touch -a "$TWIRP_OUT_DIR/__init__.py"

log_info "Fixing import lines"
for f in "$PYTHON_OUT_DIR"/*.py; do
  echo " - $f"
  sed -i -r 's|^(import livekit)|from . \0|' "$f"
done

log_info "Formatting"
black .

log_info "Sorting imports"
isort .
