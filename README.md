# Linux Japanese Font Fix

A robust Fontconfig setting to fix common Japanese font rendering issues (e.g., the "Chinese font problem") on Fedora systems, particularly when using a non-Japanese locale.

## The Problem

On a fresh installation of Fedora with a non-Japanese locale (e.g., English), the system may default to using Chinese fonts to display Japanese characters. This happens because the default font priority is not optimized for Japanese, leading to incorrect character shapes (e.g., `直` or `骨`).

While this is typically not an issue when using a Japanese locale from the start, it can be a significant problem for developers or users who work in a multilingual environment on a system set to another language.

This configuration file solves this issue with a clean and robust approach.

## The Solution

This configuration (`50-user-jp-fonts.conf`) forces the system to use the high-quality Noto CJK JP fonts for Japanese rendering.

-   **For Web Browsing:** It assigns `Noto Sans CJK JP` and `Noto Serif CJK JP` to the generic `sans-serif` and `serif` families, ensuring stable rendering in browsers.
-   **For Developers:** It sets up a sophisticated `monospace` configuration that prioritizes `Noto Sans Mono` for code (for maximum readability of Latin characters and symbols) and seamlessly falls back to `Noto Sans Mono CJK JP` for Japanese comments.

## Prerequisites

You need to have the Noto CJK fonts installed.

**On Fedora:**
```bash
sudo dnf install google-noto-cjk-fonts
```

## Installation

You can install this configuration for a single user.

1.  Create the configuration directory if it doesn't exist:
    ```bash
    mkdir -p ~/.config/fontconfig/conf.d
    ```

2.  Copy the font configuration file:
    ```bash
    cp 50-user-jp-fonts.conf ~/.config/fontconfig/conf.d/
    ```

3.  Rebuild the font cache:
    ```bash
    fc-cache -fv
    ```

4.  Restart your applications (or log out and log back in) to see the changes.

## License

This project is licensed under the MIT License.