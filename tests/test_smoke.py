# SPDX-FileCopyrightText: 2026 Your Name
# SPDX-License-Identifier: GPL-3.0-or-later
"""Smoke test: the manifest is valid and SlideMage's own loader loads the plugin.

Run against a SlideMage checkout: PYTHONPATH=<SlideMage>/src:. python -m pytest -q
"""
from __future__ import annotations

from pathlib import Path

import pytest

loader = pytest.importorskip("slidemage.plugins.loader")
from slidemage.plugins.manifest import matches, read_manifest  # noqa: E402
from slidemage.plugins.registry import Registrar  # noqa: E402
from slidemage.version import VERSION_NUMBER  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(autouse=True)
def isolated(tmp_path, monkeypatch):
    """No installed plugins and a fresh enabled/disabled state: only this folder is loaded."""
    monkeypatch.setattr(loader.project, "config_dir", lambda: tmp_path / "config")
    monkeypatch.setattr(loader, "plugins_dir", lambda: tmp_path / "plugins")
    monkeypatch.setenv(loader.PATH_ENV, str(ROOT))


def test_the_manifest_is_valid_and_matches_this_slidemage():
    manifest = read_manifest(ROOT)
    assert matches(manifest.requires_slidemage, VERSION_NUMBER)


def test_slidemages_loader_loads_the_plugin():
    manifest = read_manifest(ROOT)
    plugins = {p.id: p for p in loader.load_all(Registrar)}
    plugin = plugins[manifest.id]
    assert plugin.state == "loaded", plugin.reason
