# seriesname.com-type Image Downloader

## Overview

So, I got tired of rewriting the same image scraper over and over for sites like `seriesname.com`—you know the type. Instead of rebuilding from scratch every time, I threw together this lightweight tool using bits and pieces from my other (more complex) scrapers.

It’s not fancy, but it gets the job done. Perfect if you're just messing around, learning, or need a quick base to start from.

I've baked in a couple of my usual preferences: automatic image format conversion, a consistent renaming scheme, and easy customization if you want to switch up the output format.

Basically, it's my go-to starter pack for scraping image-heavy sites. Feel free to make it yours.

## This Script Will

- Scrape images from seriesname.com-style websites
- Automatically convert images to your preferred format (currently converts them into pngs)
- Rename files using a consistent naming convention (single-digit numbers are padded with leading zeros—e.g., `1.png` becomes `01.png`)

## Prerequisites

- Python 3.x
- Requests library
- BeautifulSoup library
- Pillow

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4 pillow
```

Or install them using the [`requirements.txt`](requirements.txt) by typing the following command in a terminal window: `pip install -r requirements.txt`

## Usage

After cloning the repository, run the script with command-line arguments to specify the target URL, and optionally the output folder.

### Command-line Arguments

| Argument           | Description                                                                        |
| ------------------ | ---------------------------------------------------------------------------------- |
| `--url`            | The URL of the chapter or comic to scrape.                                         |
| `-o, --output_dir` | (Optional) The name of the folder to save images. Defaults to `downloaded_images`. |

Examples:

```bash
python scraper.py --url https://www.example-series.com/chapter-1
```
