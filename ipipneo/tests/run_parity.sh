#!/bin/sh
# Compares the Go builds against the original Python app, offline, inside a
# digest-pinned python:3.8 container. Run ../build.sh test first.

set -eu

PYTHON_IMAGE="python:3.8-slim@sha256:1d52838af602b4b5a831beb13a0e4d073280665ea7be7f69ce2382f29c5a613f"

HERE=$(cd "$(dirname "$0")" && pwd)
REPO=$(dirname "$(dirname "$HERE")")

case "$(uname -m)" in
    arm64|aarch64) PLATFORM=linux/arm64 ;;
    *)             PLATFORM=linux/amd64 ;;
esac

docker run --rm --network=none --platform "$PLATFORM" \
    -v "$REPO:/src:ro" \
    "$PYTHON_IMAGE" \
    python3 /src/ipipneo/tests/parity_test.py /src/app \
        /src/dist/test/ipipneo-legacy /src/dist/test/ipipneo-current
