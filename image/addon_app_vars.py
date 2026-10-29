"""
Start Music Assistant with the app variables configured in the add-on options.

Official Music Assistant images bundle shared API credentials (such as the Spotify
client id). This self-built test image has none, so the add-on lets the user supply
their own: they are written to the plaintext app vars file Music Assistant reads via
MASS_APP_VARS_FILE, then the regular entrypoint takes over.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

OPTIONS_FILE = Path("/data/options.json")
APP_VARS_FILE = Path(os.environ.get("MASS_APP_VARS_FILE", "/data/app_vars.json"))
ENTRYPOINT = "/usr/local/bin/entrypoint.sh"
# add-on options that map directly to an app var of the same name
DIRECT_OPTIONS = ("spotify_client_id",)


def collect_app_vars(options: dict[str, object]) -> dict[str, str]:
    """
    Return the app vars defined by the add-on options.

    :param options: Parsed add-on options.
    """
    app_vars: dict[str, str] = {}
    for name in DIRECT_OPTIONS:
        value = str(options.get(name) or "").strip()
        if value:
            app_vars[name] = value
    extra = options.get("app_vars") or []
    if isinstance(extra, list):
        for entry in extra:
            name, separator, value = str(entry).partition("=")
            if separator and name.strip() and value.strip():
                app_vars[name.strip()] = value.strip()
            else:
                print(f"Ignoring malformed app_vars entry (expected name=value): {entry!r}")
    return app_vars


def main() -> None:
    """Write the app vars file and hand over to the Music Assistant entrypoint."""
    try:
        options = json.loads(OPTIONS_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        options = {}
    app_vars = collect_app_vars(options if isinstance(options, dict) else {})
    if app_vars:
        APP_VARS_FILE.write_text(json.dumps(app_vars), encoding="utf-8")
        print(f"Using custom app vars: {', '.join(sorted(app_vars))}")
    else:
        APP_VARS_FILE.unlink(missing_ok=True)
    os.execv(ENTRYPOINT, [ENTRYPOINT, *sys.argv[1:]])


if __name__ == "__main__":
    main()
