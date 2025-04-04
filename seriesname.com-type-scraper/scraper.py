import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse
from io import BytesIO
from PIL import Image
import random

# A list of User-Agent strings to rotate
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
]

HEADERS = {
        "User-Agent": random.choice(USER_AGENTS) 
    }



def download_images(chapter_url, output_dir):
    """"
    Download all images from a given URL and save them to the specified directory:
        - all images will be saved as PNG files; if the image is not in PNG format, it will be converted to PNG.
        - the images will be named as 01.png, 02.png, etc.

    Args:
        chapter_url (str): The URL of the chapter containing images.
        output_dir (str): The directory where images will be saved.
    """

    response = requests.get(chapter_url, headers=HEADERS)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img')

    for img_tag in image_tags:
        img_url = img_tag.get('src')
        if not img_url:
            print("❌ No image URL found in the tag.")
            continue

        img_url = urljoin(chapter_url, img_url)
        img_name = os.path.basename(img_url)

        img_response = requests.get(img_url, headers=HEADERS)
        img_response.raise_for_status()

        img_name = f"{image_tags.index(img_tag) + 1:02}.png"
        original_img_extension = os.path.basename(img_url).split('.')[-1]

        with open(os.path.join(output_dir, img_name), 'wb') as img_file:

            # Convert image to PNG if it's not already in PNG format
            if original_img_extension.lower() != 'png':
                img = Image.open(BytesIO(img_response.content))
                img = img.convert('RGB')
                img.save(os.path.join(output_dir, img_name), 'PNG')
            else:
                img_file.write(img_response.content)

        print(f'✅ Downloaded {img_name}')



def main():
    """"
    Main function to handle command line arguments and initiate the download process:
        - handles arguments for the URL of the chapter and the output directory.
        - if no output directory is provided, it defaults to 'downloaded_images'
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', type=str, help='URL of the chapter')
    parser.add_argument('-o', '--output_dir', type=str, required=False, help='Directory to save the images')

    args = parser.parse_args()

    chapter_url = args.url
    output_dir = args.output_dir
    if output_dir is None:
        output_dir = 'downloaded_images'


    os.makedirs(output_dir, exist_ok=True)

    download_images(chapter_url, output_dir)
    print(f"\t 🎉 All images downloaded to {output_dir}")



if __name__ == "__main__":
    main()