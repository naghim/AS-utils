#!/usr/bin/env python3
import os
import zipfile
import rarfile
import sys
from natsort import natsorted

""" 
This script extracts files from ZIP or RAR archives, 
sorts them in natural order and renames them based 
on their content, then repackages them 
into a new ZIP archive.
"""

magic_header_to_extension = {
    b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A': '.png',
    b'\xFF\xD8\xFF': '.jpg',
    b'\x52\x49\x46\x46': '.webp'
}


def find_extension(data):
    for header, ext in magic_header_to_extension.items():
        if data.startswith(header):
            return ext

    return None


def extract_archive(archive_path):
    if archive_path.endswith('.zip'):
        archive_type = zipfile.ZipFile
    elif archive_path.endswith('.rar'):
        archive_type = rarfile.RarFile
    else:
        raise ValueError("Unsupported archive format")
    
    with archive_type(archive_path, 'r') as zip_ref:
        return [[os.path.basename(info.filename), zip_ref.read(info)] for info in zip_ref.infolist() if not info.is_dir()]


def sort_files(files):
    # Rename files based on their content
    for file in files:
        ext = find_extension(file[1])

        if ext:
            file[0] = f"{os.path.splitext(file[0])[0]}{ext}"
        else:
            print(f"WARNING: Could not determine extension for {file[0]}")

    # Sort files by their name in natural order
    sorted_files = natsorted(files, key=lambda x: x[0])

    # Rename the files in order
    for i, file in enumerate(sorted_files):
        sorted_files[i][0] = f"{(i + 1):02d}{os.path.splitext(file[0])[1]}"

    return sorted_files


def create_zip(output_filename, files):
    # Ensure the output filename has .zip extension
    output_filename = f'{os.path.splitext(output_filename)[0]}.zip'

    # Create a zip file, but only add the files (not the folder structure)
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for filename, data in files:
            zipf.writestr(filename, data)

    print(f"Created zip archive: {output_filename}")


def main():
    try:
        archive_name = sys.argv[1]
    except:
        print("Please provide the archive name as an argument")
        return

    try:
        output_name = sys.argv[2]
    except:
        output_name = 'new_archive'

    archive_files = extract_archive(archive_name)
    archive_files = sort_files(archive_files)

    create_zip(output_name, archive_files)


if __name__ == "__main__":
    main()
