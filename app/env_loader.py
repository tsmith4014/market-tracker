"""Load optional dotenv-style files without extra dependencies."""
from __future__ import annotations

import os
from pathlib import Path


def load_dotenv_file(path: Path, *, override: bool = False) -> int:
    """Load KEY=VALUE lines into os.environ. Returns number of keys set."""
    if not path.is_file():
        return 0
    count = 0
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].strip()
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        if not key:
            continue
        if not override and key in os.environ:
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        os.environ[key] = value
        count += 1
    return count


def load_openclaw_env(*, override: bool = False) -> int:
    """Load ~/.openclaw/.env if present (OpenClaw local config)."""
    custom = os.getenv("OPENCLAW_ENV_FILE", "").strip()
    if custom:
        return load_dotenv_file(Path(custom).expanduser(), override=override)
    return load_dotenv_file(Path.home() / ".openclaw" / ".env", override=override)
