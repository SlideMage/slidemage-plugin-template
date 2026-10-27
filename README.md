# SlideMage plugin template

A starting point for a [SlideMage](https://slidemage.org/) plugin. It has the layout,
the build and the release workflow the plugin catalogue expects; the
[conventions](https://slidemage.org/plugins/submit/) explain each rule.

> SlideMage doesn't load plugins yet. The plugin API (`slidemage.plugin_api`) will be documented with the
> first SlideMage release that supports plugins.

## Using this template

1. **Use this template → Create a new repository**, named `slidemage-plugin-<id>`. Choose an id that is
   2–32 lowercase letters, digits or hyphens, starting with a letter; it never changes.
2. Rename the package folder `example/` to your id, with hyphens as underscores (id `my-plugin`, folder
   `my_plugin/`).
3. Fill in `plugin.toml`: every field, including `needs` (what the user must have) and `network` (everything
   the plugin contacts). SlideMage shows both before a user installs the plugin.
4. Write the plugin in the package. Import only `slidemage.plugin_api`, the Python standard library, PySide6
   and your own modules, and keep it pure Python.
5. Replace the top of this README, up to the `## Development` heading, with what your plugin does: the
   website shows that part as the plugin's description. Keep a `## Development` section; everything from
   there on stays on GitHub.
6. Replace `website/icon.svg` (an SVG without scripts, or `website/icon.png`, square, at least 128 px), and
   add up to 6 screenshots as `website/screenshots/*.png` (at most 1 MB each), if you like.
7. Start `CHANGELOG.md` with your first version, and check that the license (`LICENSE`, GPL-3.0-or-later
   here) is the one you want; it must be GPL-compatible.

Then release (below) and [submit the plugin](https://slidemage.org/plugins/submit/).

## Development

`python build.py --check` checks the plugin against the catalogue's conventions: `plugin.toml`, the package
and its `activate(host)`, the imports, no compiled files, and a `CHANGELOG.md` entry for the version. The
**Check** workflow runs it on every push.

`python build.py` checks and then builds `dist/<id>-<version>.smplugin` (a zip of `plugin.toml`, `LICENSE`
and the package) and its `.sha256`. The build is reproducible: the same files always give the same hash.

### Releasing a version

1. Raise `version` in `plugin.toml` and add a line to the end of `CHANGELOG.md`:
   `v1.2.0 (2026-11-02, reason): What changed.`
2. Commit, then tag and push: `git tag v1.2.0 && git push origin v1.2.0`.
3. The **Release** workflow checks that the tag matches the version, builds the asset and publishes the
   GitHub release with it.

A published version never changes: never replace or delete its asset; a fix is a new version. Drafts and
pre-releases are not listed in the catalogue.
