# Project Instructions: linux-japanese-font-fix

This project provides Fontconfig settings to fix Japanese font rendering on Fedora.

## Release Process

When releasing a new version (e.g., to support new Fedora versions):

1.  **Update `linux-japanese-font-fix.spec`**:
    *   Increment the `baserelease` macro (used by `Release` and `Source0`).
    *   Update the `%changelog` section. Use the format `* Day Mon DD YYYY Name <email> - Version-Release`.
    *   Standardize version numbers in the changelog to use the `1.0.0-x` format.
2.  **Update `CHANGELOG.md`**:
    *   Add a new section for the release.
    *   Summarize the changes (e.g., "Added support for Fedora 44").
3.  **Update READMEs**:
    *   Update `README.md` and `README.ja.md` to reflect the supported Fedora versions if necessary.
4.  **Update Copr configuration**:
    *   Update `.copr/project.yaml` to include new chroots (e.g., `fedora-44-x86_64`).
5.  **Tag the release** after merging to `main`:
    *   Create and push the tag `v<Version>-<Release>` (e.g., `v1.0.0-7`). `Source0` downloads this tag's archive.

## Versioning Convention

- Follow `Version-Release` format.
- Current Version: `1.0.0`
- Current Release: `7`

## Build System

- The project uses a Makefile and a `.copr/Makefile` to generate SRPMs for Copr.
- To generate an SRPM locally, run `make srpm`.
