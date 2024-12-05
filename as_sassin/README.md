# as_sassin

~~Yes, bad puns will never end.~~

## Overview

**as_sassin** is a web scraping tool designed to extract data from G-Portál websites based on a user-defined configuration (`config.json`). It retrieves HTML content, parses it with BeautifulSoup, and organizes the extracted data into a structured format.
The final output is saved in a file named `output.json`.

## This Script Will

- Fetch the HTML content of the specified URL(s).
- Parse the HTML content to extract relevant data.
- Scrape data from multiple modules ("blogs") as defined in the configuration.
  - Iterates through pages and collects data until no more pages are available.
- Saves the collected data into `output.json`.

## Configuration (`config.json`):

The script relies on `config.json` to define scraping behavior:

- `KEY_MAPPING` (dict): Maps scraped data keys to their English equivalents. If left empty or a key is missing, the original lowercase keys will be used.
- `BASE_URL` (str): The base URL of the website to scrape.
- `MODULES` (list): A list of "blog" modules to scrape data from.

For example:

```json
{
  "KEY_MAPPING": {
    "Hungarian_key": "english_key", // Maps "Hungarian_key" to "english_key" in the output
    "Hungarian_key_2": "english_key_2"
  },
  "BASE_URL": "https://example-website.gportal.hu/", // Base URL of the website to scrape
  "MODULES": [
    "module_id_1", // Replace with actual module IDs (e.g., blog categories such as 36877639)
    "module_id_2"
  ]
}
```

## Prerequisites

1. **Python 3.x**: Ensure you have Python 3 installed.
2. **Dependencies**:

- `requests`: Install via `pip install requests`
- `beautifulsoup4`: Install via `pip install beautifulsoup4`

You can also install them via the [`requirements.txt`](requirements.txt).

## Usage

### Command-line Execution

Run the script:

```bash
./as_sassin.py
```

## Notes

**This scraper is designed with a flexible structure but may require customization.** While optimized for scraping blog modules on G-Portál websites, adjustments may be necessary to handle variations in the structure of individual posts. The script is modular, allowing you to easily expand its functionality or adapt it to new modules by modifying `config.json` and the parsing logic. Sections of the code requiring customization have been clearly marked with comments.
