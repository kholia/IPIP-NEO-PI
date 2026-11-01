### IPIP-NEO

This project is a port of Dr. John's IPIP-NEO software that runs offline
(disconnected from the internet). It is a single program with no installation
and no Python required, for Windows XP through Windows 11, macOS, and Linux.

IPIP-NEO-120 is an IPIP version of the NEO-PI-R test.

"The IPIP-NEO is not identical to the original NEO PI-R, but in my opinion it
is close enough to serve as a good substitute. More and more people are
beginning to use it in published research, so its acceptance is growing." - Dr.
Johnson

#### Upstream Resources

* [Current home of the original web-based test](https://drj.virtualave.net/IPIP/index.html) (originally hosted at Penn State)
* Dr John A. Johnson (j5j [at] psu [dot] edu) - [homepage](https://sites.psu.edu/drj5j/)

#### Installation on Windows

1. Download the `IPIP-NEO-PI-Windows.zip` file from the [Releases page](https://github.com/kholia/IPIP-NEO-PI/releases)
   and extract it.

2. Double-click `start-server.bat`.

   It detects your Windows version (XP, Vista, 7, 8, 8.1, 10, or 11), starts
   the right program, and opens the test in your web browser. Keep the black
   console window open while taking the test, and close it when you are done.

That's it! If you closed the browser window, double-click `start-browser.bat`
or open http://localhost:8888 manually.

Which program does `start-server.bat` pick? You can also double-click the
program directly:

| Windows version                | Program                            |
| ------------------------------ | ---------------------------------- |
| XP, Vista, 7, 8, 8.1           | `IPIP-NEO-PI-WinXP-Win7-x86.exe`   |
| 10, 11 (64-bit, most PCs)      | `IPIP-NEO-PI-Win10-x64.exe`        |
| 10, 11 (32-bit)                | `IPIP-NEO-PI-Win10-x86.exe`        |
| 10, 11 (ARM, e.g. Snapdragon)  | `IPIP-NEO-PI-Win10-arm64.exe`      |

The `WinXP-Win7` program also works on Windows 10 and 11, but prefer the
`Win10` programs there: they are built with a currently supported (and
security-patched) version of the Go toolchain.

[OPTIONAL] We recommend using the `Firefox` web browser. Firefox can be
downloaded from the https://www.mozilla.org/ website. On Windows XP, use
Firefox 52 ESR, the last version that supports XP.

#### Installation on macOS and Linux

Download the program for your system from the [Releases page](https://github.com/kholia/IPIP-NEO-PI/releases)
and run it from a terminal:

```
chmod +x IPIP-NEO-PI-Linux-x64
./IPIP-NEO-PI-Linux-x64
```

| System                       | Program                            |
| ---------------------------- | ---------------------------------- |
| macOS (Apple Silicon, M1+)   | `IPIP-NEO-PI-macOS-AppleSilicon`   |
| macOS (Intel)                | `IPIP-NEO-PI-macOS-Intel`          |
| Linux (x86-64)               | `IPIP-NEO-PI-Linux-x64`            |
| Linux (ARM64, e.g. Pi 4/5)   | `IPIP-NEO-PI-Linux-arm64`          |

The macOS programs are not signed by Apple. If macOS refuses to open the
program, run `xattr -d com.apple.quarantine IPIP-NEO-PI-macOS-*` once.

Options (all platforms): `-port 8899` to use a different port, `-no-browser`
to not open a web browser, and `-data <file>` to choose where results are
saved.

#### Reporting

The test results are saved in a `results.csv` file next to the program. (If
that folder is read-only, e.g. inside `Program Files`, the file goes to
`%APPDATA%\IPIP-NEO-PI\results.csv` instead. The console window shows the
exact location.) This file opens directly in Excel or LibreOffice Calc.

Columns: `Timestamp`, `Sex` (sex assigned at birth), `Age`, `Nick`, `Country`,
`Responses` (the 120 answers), `GenderIdentity`, and `OtherGenderIdentity`.
Files from earlier versions are upgraded automatically: their header is
updated and the old rows are kept.

The test asks for sex assigned at birth (male, female, or intersex) and
current gender identity, like the official online version. Reports use the
2021 norms, which are separate for males and females by age group, so no
report can be produced yet for intersex respondents. Their responses are still
saved. (The official online version has since moved to a single comparison
group of over two million people, but those norms are not available here.)

To view historical tests, click [here](http://localhost:8888/reporting). Doing
so opens the http://localhost:8888/reporting page in your browser. That page
also has a link to download the CSV file.

**Moving results from the old Python version**: the old version saved results
in `app\results.db` (SQLite). To convert them, put the `results.csv` file next
to the new program after running:

```
sqlite3 -header -csv app/results.db "SELECT * FROM RESULTS" > results.csv
```

#### Old Python version

The original Python version is still in the `app` folder. `start-server.bat`
falls back to it when no program file is found. It needs `Python 3.8.10 32-bit`
([download](https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe), select
`Add Python 3.8 to PATH` when installing), or `Python 3.4.4` on Windows XP
([download](https://www.python.org/ftp/python/3.4.4/python-3.4.4.msi), select
`Install for all users`).

#### Building from source

All builds are hermetic: they run inside digest-pinned Docker containers with
networking disabled, so the only requirement is Docker. Builds are
reproducible (same source, same binaries, byte for byte).

```
make            # or: ipipneo/build.sh
```

The programs go to `dist/windows/`, `dist/macos/`, and `dist/linux/`, each with
a `SHA256SUMS` file, plus `dist/IPIP-NEO-PI-Windows.zip` (the Windows programs,
`start-server.bat`, and `start-browser.bat`) ready to upload to a GitHub release.

Two Go toolchains build the same code (the `ipipneo` folder):

* Go 1.10.8 builds the Windows XP to 8.1 program. It is the last Go version
  that supports Windows XP. Go stopped supporting Windows 7 and 8 after Go
  1.20.

* The current Go version builds everything else.

The Go code must therefore keep compiling with Go 1.10: use only the
standard library, and no `embed`, generics, or newer APIs. `build.sh` checks
this on every build. All programs are built with `CGO_ENABLED=0`, so they
depend on no C runtime (no `libc` or `msvcrt.dll`).

#### Testing

```
make test             # unit tests + parity test (hermetic, Docker only)
make browser-check    # charts render correctly (uses your local Chrome)
make upstream-check   # compare with Dr. Johnson's scripts (see below)
```

`make test` runs:

* The Go unit tests, with both Go 1.10.8 and the current Go. They include a
  test that sends thousands of random and malformed requests to every page
  and fails if the server ever crashes (panics) or returns a server error.

* `ipipneo/tests/run_parity.sh`, which checks the Go programs against the
  original Python version. It runs both inside a pinned `python:3.8` container
  with no network, sends the same 3,300 random test submissions to each, and
  checks that the scores, the reports, and the saved data match exactly.

`make browser-check` renders a report in headless Chrome and checks that all
five charts are drawn with the right scores.

`ipipneo/tests/upstream_check.py` checks our scores against Dr. Johnson's
official scripts. It never contacts the live site, which stores every
completed test in his research database. Instead, it runs random tests
through a local copy of his CGI scripts, saves the official results as
fixture files, and then compares our program against those fixtures offline.
See the top of the script for usage.

#### Updating the pages from the official site

The intro and item pages (`ipipneo/views/index.html` and `shortipipneo.html`)
are generated from saved copies of the official pages by
`ipipneo/tools/upstream_views.py`. The top of that script explains how to save
the pages and lists every deliberate difference from the official site.

#### Internal Components

* Go (standard library only)

* jQuery 3.7.1 (the newest version that still runs in the browsers available
  on Windows XP, such as Firefox 52 ESR)

* jqPlot 1.0.9.d96a669 (charts; this is its last release)

* Bottle 0.12.19 (old Python version)

#### Credits

* Dr John A. Johnson

* Dhiru Kholia

* Dr KJ Divina Kumar

#### Notes

All development work happens on Linux (Ubuntu).

For testing, we run Windows XP, 7, and 10 Virtual Machines using VirtualBox.

For testing the old Python version against the upstream website, use the
`time python3 randomized_combo_tester_v4.py` command.

#### License

Public Domain. See https://ipip.ori.org/newPermission.htm for more information.

#### Resources

* http://personality-project.org/pmc.html

* https://ipip.ori.org/

* https://ipip.ori.org/newneofacetskey.htm

* http://personality-project.org/r/psych/

* https://www.sapa-project.org/

* https://personality-project.org/r/book/

* https://openpsychometrics.org/

* https://en.wikipedia.org/wiki/Revised_NEO_Personality_Inventory

* https://en.wikipedia.org/wiki/International_Personality_Item_Pool
