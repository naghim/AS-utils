import requests
from bs4 import BeautifulSoup
import json


with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

    KEY_MAPPING = config.get("KEY_MAPPING", {})
    BASE_URL = config.get("BASE_URL")
    MODULES = config.get("MODULES")


def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None


def get_page_data(url):
    html = get_html(url)

    if html:
        soup = BeautifulSoup(html, 'html.parser')
        divs = soup.find_all('div', id=lambda x: x and x.startswith('post_'))

        data = []
        if not divs:
            print(f"No more pages at {url}")
            return data, False

        # Note:
        # The following code is highly custimized based on the structure of the HTML content I'm scraping
        # It needs to be adjusted based on the structure of the website being scraped
        for div in divs:
            # Title
            title = div.find('a').text.strip()
            flat_details = {'title': title}
            
            # Contents: Table
            details = {}
            for row in div.find_all('tr'):
                tds = row.find_all('td')
                if len(tds) == 2:
                    key = tds[0].text.strip().strip(':')
                    value = tds[1].text.strip()
                    details[key] = value
            for key, value in details.items():
                new_key = KEY_MAPPING.get(key, key.lower())  # Use original key if no mapping found
                flat_details[new_key] = value

            # Contents: Buttons of the links
            for button in div.find_all('button'):
                button_text = button.text.strip()
                button_link = button.get('onclick').split("'")[1]
                if button_link:
                    new_key = KEY_MAPPING.get(button_text, button_text)
                    flat_details[new_key] = button_link

            # Contents: Link after table, if any
            p_projekt = [p for p in div.find_all('p', style="text-align: center;") if 'projekt' in p.text]
            if p_projekt:
                p_projekt = p_projekt[0]
                link = p_projekt.find('a')

                if link:
                    flat_details['joint_project'] = {
                        'team': link.text.strip(),
                        'link': link.get('href') if not None else ""
                    }
                else:
                    flat_details['joint_project'] = {
                        'team': p_projekt.text.strip()
                    }

            data.append(flat_details)

        return data, True


def run_scraper():
    data = []
    for module in MODULES:
        pageno = 1
        while True:  
            url = f"{BASE_URL}gindex.php?pg={module}&pageno={pageno}"
            pageno += 1

            page_data, has_more_pages = get_page_data(url)
            if not has_more_pages:
                break

            data.append(page_data)

    with open('output.json', 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    run_scraper()
