#!/bin/sh
# Hermetic builds of IPIP-NEO-PI, inside digest-pinned Docker images with
# networking disabled. Needs only Docker on the host.
#
#   ./build.sh            # release builds -> ../dist/{windows,macos,linux}/
#                         # (dist/windows also gets start-server.bat)
#   ./build.sh test       # also runs the Go unit tests with both toolchains
#                         # and builds host-arch Linux binaries of both for
#                         # tests/run_parity.sh -> ../dist/test/
#
# Two toolchains, one codebase:
#   Go 1.10.8 (legacy)  -> Windows XP, Vista, 7, 8, 8.1 (and newer)
#   Go 1.27.x (current) -> Windows 10/11, macOS, Linux
# All builds use CGO_ENABLED=0: no C toolchain, no libc / msvcrt dependency.

set -eu

# To update an image: docker pull <tag>, then copy its RepoDigest here.
LEGACY_IMAGE="golang:1.10.8@sha256:6d5e79878a3e4f1b30b7aa4d24fb6ee6184e905a9b172fc72593935633be4c46"
CURRENT_IMAGE="golang:1.27.3-trixie@sha256:c65ecfe613b539ac74c62a4c3b2c27e8f8a6076384c8f27e8a3c0f3be17cc385"

HERE=$(cd "$(dirname "$0")" && pwd)
REPO=$(dirname "$HERE")
OUT="$REPO/dist"
VERSION=${VERSION:-$(git -C "$REPO" describe --tags --always --dirty 2>/dev/null || echo dev)}

# The pinned digests are multi-arch; use the host's native variant (old Go
# toolchains crash under x86 emulation). Output does not depend on it.
case "$(uname -m)" in
    arm64|aarch64) PLATFORM=linux/arm64 ;;
    *)             PLATFORM=linux/amd64 ;;
esac

rm -rf "$OUT/windows" "$OUT/macos" "$OUT/linux" "$OUT/test" "$OUT/IPIP-NEO-PI-Windows.zip"
mkdir -p "$OUT/windows" "$OUT/macos" "$OUT/linux"

# run IMAGE SCRIPT: runs SCRIPT in a throwaway container with the repo
# mounted read-only and no network access.
run() {
    docker run --rm --network=none --platform "$PLATFORM" \
        --user "$(id -u):$(id -g)" \
        -e HOME=/tmp -e GOPATH=/tmp/gopath -e GOCACHE=/tmp/gocache \
        -e GOFLAGS= -e GOPROXY=off -e GOTOOLCHAIN=local -e CGO_ENABLED=0 \
        -e VERSION="$VERSION" \
        -v "$REPO:/src:ro" -v "$OUT:/out" \
        "$1" sh -euc "
            # Fixed build path so binaries are reproducible.
            mkdir -p /tmp/build && cd /tmp/build
            cp /src/ipipneo/*.go /src/ipipneo/go.mod .
            go run genassets.go /src/ipipneo/static /src/ipipneo/views
            $2"
}

LEGACY_BUILD='go build -ldflags "-s -w -X main.version=$VERSION"'
CURRENT_BUILD='go build -trimpath -buildvcs=false -ldflags "-s -w -buildid= -X main.version=$VERSION"'

echo ">> legacy toolchain (Go 1.10.8): Windows XP .. 8.1"
run "$LEGACY_IMAGE" "
    go version
    GOOS=windows GOARCH=386 $LEGACY_BUILD -o /out/windows/IPIP-NEO-PI-WinXP-Win7-x86.exe
"

echo ">> current toolchain: Windows 10/11, macOS, Linux"
run "$CURRENT_IMAGE" "
    go version
    go vet .
    GOOS=windows GOARCH=amd64 $CURRENT_BUILD -o /out/windows/IPIP-NEO-PI-Win10-x64.exe
    GOOS=windows GOARCH=386   $CURRENT_BUILD -o /out/windows/IPIP-NEO-PI-Win10-x86.exe
    GOOS=windows GOARCH=arm64 $CURRENT_BUILD -o /out/windows/IPIP-NEO-PI-Win10-arm64.exe
    GOOS=darwin  GOARCH=arm64 $CURRENT_BUILD -o /out/macos/IPIP-NEO-PI-macOS-AppleSilicon
    GOOS=darwin  GOARCH=amd64 $CURRENT_BUILD -o /out/macos/IPIP-NEO-PI-macOS-Intel
    GOOS=linux   GOARCH=amd64 $CURRENT_BUILD -o /out/linux/IPIP-NEO-PI-Linux-x64
    GOOS=linux   GOARCH=arm64 $CURRENT_BUILD -o /out/linux/IPIP-NEO-PI-Linux-arm64
"

if [ "${1:-}" = "test" ]; then
    echo ">> unit tests + host-arch Linux test binaries"
    mkdir -p "$OUT/test"
    run "$LEGACY_IMAGE" "go test . && GOOS=linux $LEGACY_BUILD -o /out/test/ipipneo-legacy"
    run "$CURRENT_IMAGE" "go test . && GOOS=linux $CURRENT_BUILD -o /out/test/ipipneo-current"
fi

# Ship the launcher with the Windows programs.
cp "$REPO/start-server.bat" "$REPO/start-browser.bat" "$OUT/windows/"

for d in windows macos linux; do
    (cd "$OUT/$d" && shasum -a 256 IPIP-NEO-PI-* > SHA256SUMS)
done

echo ">> Windows release ZIP"
run "$CURRENT_IMAGE" "
    cd /out/windows
    go run /tmp/build/mkzip.go /out/IPIP-NEO-PI-Windows.zip IPIP-NEO-PI \
        start-server.bat start-browser.bat SHA256SUMS IPIP-NEO-PI-*.exe /src/README.md
"
(cd "$OUT" && shasum -a 256 IPIP-NEO-PI-Windows.zip */IPIP-NEO-PI-*)
