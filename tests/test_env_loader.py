"""Tests for OpenClaw .env loading."""

from __future__ import annotations

import os

from env_loader import load_dotenv_file


def test_load_dotenv_does_not_override_existing(tmp_path, monkeypatch):
    env_file = tmp_path / ".env"
    env_file.write_text("SLACK_WEBHOOK_URL=from_file\nFOO=bar\n")
    monkeypatch.setenv("SLACK_WEBHOOK_URL", "from_shell")
    n = load_dotenv_file(env_file)
    assert n == 1
    assert os.environ["SLACK_WEBHOOK_URL"] == "from_shell"
    assert os.environ["FOO"] == "bar"
