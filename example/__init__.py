# SPDX-FileCopyrightText: 2026 Your Name
# SPDX-License-Identifier: GPL-3.0-or-later
"""Example: a SlideMage plugin. SlideMage imports this package and calls activate() once at start."""


def activate(host) -> None:
    """Register the plugin's contributions with SlideMage through host (see slidemage.plugin_api)."""
