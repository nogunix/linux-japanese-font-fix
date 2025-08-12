# Linux Japanese Font Fix

A robust Fontconfig setting to fix common Japanese font rendering issues (e.g., the "Chinese font problem") on Fedora systems, particularly when using a non-Japanese locale.

## The Problem

On a fresh installation of Fedora with a non-Japanese locale (e.g., English), the system may default to using Chinese fonts to display Japanese characters. This happens because the default font priority is not optimized for Japanese, leading to incorrect character shapes (e.g., `直` or `骨`).

This issue has been confirmed on **Fedora 42**. It occurs because the default Noto CJK font package includes glyphs for Japanese, Chinese, and Korean in a single file. For systems with a non-Japanese locale, Fontconfig can easily select the incorrect glyphs for Japanese text.

## Before and After

**Before (Incorrect Chinese Glyphs):**

![Incorrect font rendering for Japanese characters](./images/before.png)

**After (Correct Japanese Glyphs):**

![Correct font rendering for Japanese characters](./images/after.png)

## The Solution

This configuration (`50-user-jp-fonts.conf`) forces the system to use the high-quality Noto CJK JP fonts for Japanese rendering.

-   **For Web Browsing:** It assigns `Noto Sans CJK JP` and `Noto Serif CJK JP` to the generic `sans-serif` and `serif` families, ensuring stable rendering in browsers.
-   **For Developers:** It sets up a sophisticated `monospace` configuration that prioritizes `Noto Sans Mono` for code (for maximum readability of Latin characters and symbols) and seamlessly falls back to `Noto Sans Mono CJK JP` for Japanese comments.

## Prerequisites

This configuration is intended for **Fedora 42**. You need to have the Noto CJK variable fonts installed.

**On Fedora:**
```bash
# Install the necessary Noto fonts.
sudo dnf install \
  google-noto-sans-cjk-vf-fonts \   # For sans-serif Japanese text
  google-noto-serif-cjk-vf-fonts \  # For serif Japanese text
  google-noto-sans-mono-fonts \     # For Latin/symbol monospace (code)
  google-noto-mono-cjk-fonts        # For Japanese monospace (code comments)
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