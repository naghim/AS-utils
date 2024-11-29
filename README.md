# as-utils - A Collection of Utility Scripts

A collection of small, useful scripts for automating common tasks. These tools were designed to help with file management, subtitle processing, and more.

## Scripts

No installation required. Simply download the scripts and run them with Python. **Each script includes its own documentation and a list of required dependencies.**

### 1. [`auto_zipper.py`](auto_zipper/README.md)

A versatile Python script for managing archives. It:

- Extracts files from `.zip` and `.rar` archives.
- Sorts files in natural order (e.g., `1, 2, 10` instead of `1, 10, 2`).
- Renames files based on their content:
  - Adds or normalizes file extensions using magic header detection.
  - Pads single-digit numbers with leading zeros.
- Combines the renamed and sorted files into a new `.zip` archive.
- Treats all files as if they are in a single flat directory (no folder hierarchy is preserved).

This tool is ideal for organizing archives with inconsistent naming conventions or missing file extensions.

### 2. `rename_files.py`

This script renames image files in the current directory. It:

- Adds leading zeros to single-digit numbers for consistent naming (e.g., `1.png` becomes `01.png`).
- Normalizes file extensions to lowercase for uniformity.

This is an older and simpler version of the core functionality of the `auto_zipper.py` script.

### 3. [Fontos](https://github.com/naghim/fontos)

⚡ **Font Finder and Collector**  
This application helps manage fonts for `.ass` subtitle files. It:

- Checks whether the fonts used in a `.ass` subtitle file are installed on your system.
- Collects the required fonts into a directory for easy packaging or sharing.

> Note: **Fontos** now has its own dedicated repository.

### 4. [SubAssistant](https://github.com/naghim/subassistant)

✨ **Subtitle Translation Made Easy**  
A GUI-based desktop tool crafted specifically for `.ass` subtitle files. SubAssistant is designed for translators and proofreaders, offering features such as:

- Commenting out the original dialogue while writing translations alongside it.
- Allowing proofreaders to review both the original and translated versions within the same file.
- An option to delete the commented-out texts once translation is complete.
- **Fontos GUI Integration**: Includes tools to check if fonts used in a `.ass` subtitle file are installed on your system and to collect these fonts into a directory for packaging or sharing.

This tool streamlines the subtitle translation process, making it efficient and user-friendly.

> Note: **SubAssistant** also has its own dedicated repository.