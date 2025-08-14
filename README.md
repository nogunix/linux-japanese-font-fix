# Linux Japanese Font Fix

[![GitHub last commit](https://img.shields.io/github/last-commit/nogunix/linux-japanese-font-fix)](https://github.com/nogunix/linux-japanese-font-fix/commits/main) [![GitHub license](https://img.shields.io/github/license/nogunix/linux-japanese-font-fix)](#license)

English | [日本語](README.ja.md)

A robust Fontconfig setting to fix common Japanese font rendering issues (e.g., the "Chinese font problem") on Fedora systems, particularly when using a non-Japanese locale.

## The Problem

On a fresh installation of Fedora with a non-Japanese locale (e.g., English), the system may default to using Chinese fonts to display Japanese characters. This happens because the default font priority is not optimized for Japanese, leading to incorrect character shapes (e.g., `直` or `骨`).

This issue has been confirmed on **Fedora 38 and newer** (including Fedora 42).
It occurs because the default Noto CJK font package includes glyphs for Japanese, Chinese, and Korean in a single variable font file.
For systems with a non-Japanese locale, Fontconfig can easily select the incorrect glyphs for Japanese text.

For more background, see the [Fedora Project Wiki: Noto CJK Variable Fonts](https://fedoraproject.org/wiki/Changes/Noto_CJK_Variable_Fonts).

## Before and After

**Before (Chinese glyphs being used for Japanese text):**

![Fedora rendering Japanese text with incorrect Chinese glyphs](./images/before.png)

**After (Correct Japanese glyphs being used):**

![Fedora rendering Japanese text with correct Japanese glyphs](./images/after.png)

## The Solution

This configuration (`50-user-jp-fonts.conf`) forces the system to use the high-quality Noto CJK JP fonts for Japanese rendering.

- **For Web Browsing:** Assigns `Noto Sans CJK JP` and `Noto Serif CJK JP` to the generic `sans-serif` and `serif` families, ensuring stable rendering in browsers.
- **For Developers:** Sets up a sophisticated `monospace` configuration that prioritizes `Noto Sans Mono` for code (maximum readability of Latin characters and symbols) and seamlessly falls back to `Noto Sans Mono CJK JP` for Japanese comments.

> **Note:** This configuration is optimized for systems where `Noto Sans Mono` is the default monospace font (common on Fedora).
> You can check by running:
> ```bash
> fc-match monospace
> ```
> If the output is different (e.g., `DejaVu Sans Mono`), change the `Noto Sans Mono` entries in `50-user-jp-fonts.conf` accordingly.

## Prerequisites

This configuration is intended for **Fedora 38+**.
You need to have the Noto CJK variable fonts installed.

**On Fedora:**
```bash
sudo dnf install google-noto-sans-cjk-vf-fonts google-noto-serif-cjk-vf-fonts google-noto-sans-mono-fonts google-noto-sans-mono-cjk-vf-fonts
```

## Installation

### For General Users (Recommended)

The easiest way is to download just the configuration file using `wget`.

1.  Copy and paste the following command into your terminal and run it:

    ```bash
    mkdir -p ~/.config/fontconfig/conf.d && wget -O ~/.config/fontconfig/conf.d/50-user-jp-fonts.conf https://raw.githubusercontent.com/nogunix/linux-japanese-font-fix/main/50-user-jp-fonts.conf
    ```

2.  Rebuild the font cache:
    ```bash
    fc-cache -fv ~/.config/fontconfig
    ```
    *(Specifying the directory speeds up the cache rebuild compared to scanning the whole system.)*

3.  Restart your applications (or log out and log back in) to apply the changes.

### For Developers (git clone)

If you prefer to clone the entire repository to inspect or modify the configuration:

1.  Clone this repository and navigate into the directory:
    ```bash
    test -d linux-japanese-font-fix || git clone https://github.com/nogunix/linux-japanese-font-fix.git
    cd linux-japanese-font-fix
    ```

2.  Create the configuration directory if it doesn't exist:
    ```bash
    mkdir -p ~/.config/fontconfig/conf.d
    ```

3.  Copy the font configuration file:
    ```bash
    cp 50-user-jp-fonts.conf ~/.config/fontconfig/conf.d/
    ```

4.  Rebuild the font cache:
    ```bash
    fc-cache -fv ~/.config/fontconfig
    ```

5.  Restart your applications (or log out and log back in) to apply the changes.

## Verification

To confirm the fonts are applied correctly:
```bash
fc-match 'sans:lang=ja'
fc-match 'serif:lang=ja'
fc-match 'monospace:lang=ja'
```

Expected output examples:
```
NotoSansCJK-VF.ttc: "Noto Sans CJK JP" "Regular"
NotoSerifCJK-VF.ttc: "Noto Serif CJK JP" "Regular"
NotoSansMonoCJK-VF.ttc: "Noto Sans Mono CJK JP" "Regular"
```

You can also check the fallback order:
```bash
fc-match -s 'monospace:lang=ja' | head -n 5
```
## Uninstallation

If you want to remove this configuration:

1. Delete the configuration file from your Fontconfig directory:
   ```bash
   rm -f ~/.config/fontconfig/conf.d/50-user-jp-fonts.conf
   ```

2. Rebuild the font cache:
   ```bash
   fc-cache -fv ~/.config/fontconfig
   ```

3. Restart your applications (or log out and log back in) to revert to the default font selection.

## License

This project is licensed under the MIT License.
