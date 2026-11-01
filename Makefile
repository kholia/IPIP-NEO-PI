# IPIP-NEO-PI build and test entry points. Everything except browser-check
# runs inside digest-pinned Docker containers with networking disabled.
#
#   make                 release builds -> dist/ (Windows, macOS, Linux + Windows ZIP)
#   make test            Go unit tests (Go 1.10.8 and current Go) + parity test
#                        against the original Python version
#   make browser-check   render the results charts in local headless Chrome
#   make upstream-check  compare against fixtures recorded from a LOCAL copy of
#                        Dr. Johnson's scripts (see ipipneo/tests/upstream_check.py)
#   make clean

HOST_OS := $(shell uname -s)
HOST_ARCH := $(shell uname -m)

ifeq ($(HOST_OS),Darwin)
  ifeq ($(HOST_ARCH),arm64)
    NATIVE := dist/macos/IPIP-NEO-PI-macOS-AppleSilicon
  else
    NATIVE := dist/macos/IPIP-NEO-PI-macOS-Intel
  endif
else
  ifeq ($(HOST_ARCH),x86_64)
    NATIVE := dist/linux/IPIP-NEO-PI-Linux-x64
  else
    NATIVE := dist/linux/IPIP-NEO-PI-Linux-arm64
  endif
endif

.PHONY: all build test browser-check upstream-check clean

all: build

build:
	ipipneo/build.sh

test:
	ipipneo/build.sh test
	ipipneo/tests/run_parity.sh

browser-check: build
	python3 ipipneo/tests/browser_check.py $(NATIVE)

upstream-check: build
	python3 ipipneo/tests/upstream_check.py check --program $(NATIVE)

clean:
	rm -rf dist
