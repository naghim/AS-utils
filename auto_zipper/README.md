# auto_zipper

## Overview

**auto_zipper** is a Python script designed to extract files from ZIP or RAR archives, sort them in natural order and rename them based on their content, then repackage them into a new ZIP archive. This tool simplifies the process of managing archives with inconsistent or missing file extensions and naming conventions.

## The Script Will

- **Extract the contents of the archive**:

  - Handles `.zip` and `.rar` files.
  - Extracts all non-directory files for processing.

- **Rename and sort files**:

  1. Files are sorted in natural order (e.g., `1, 2, 10` instead of `1, 10, 2`).
  2. Files are renamed according to the following rules:
     - Single-digit numbers are padded with leading zeros (e.g., `1.png` becomes `01.png`).
     - Text-based filenames are renamed based on their position in the sorted array.
     - File extensions are normalized to lowercase.
     - Missing file extensions are automatically added by detecting file types from their magic headers.
     - If a file's type cannot be determined, it will retain its original extension, and a warning will be logged.

- **Repackage the files**:
  - Combines the renamed and sorted files into a new `.zip` archive.
  - No folder hierarchy is preserved; all files are treated as if they were in a single flat directory before zipping.
  - The output archive defaults to `new_archive.zip` if no other name is provided.

## Prerequisites

1. **Python 3.x**: Ensure you have Python 3 installed.
2. **Dependencies**:

   - `natsort`: Install via `pip install natsort`
   - `rarfile`: Install via `pip install rarfile`

You can also install them via the [`requirements.txt`](requirements.txt).

## Usage

### Command-line Execution

Run the script:

```bash
./auto_zipper.py <input_archive> <output_archive>
```

### Arguments

`<input_archive>`: The path to the `.zip` or `.rar` file to process.
`<output_archive>` (optional): The name of the new archive to be created. Defaults to `new_archive.zip`.

## Notes

- Only `.zip` and `.rar` are supported. Other formats (e.g., `.7z`) are not handled.
- The script supports a limited set of file types (`.png`, `.jpg`, `.webp`). Unsupported types will retain their original extensions.
