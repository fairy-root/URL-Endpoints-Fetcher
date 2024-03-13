import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse

def fetch_and_parse_url(url: str) -> list:
    """Fetches the given URL's content and parses it for all links, returning a list of absolute URLs."""
    try:
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        wiki_urls = [requests.compat.urljoin(url, link.get('href')) for link in soup.find_all('a') if link.get('href')]
        return wiki_urls
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def save_urls_to_json(urls: list, base_url: str) -> None:
    """Saves the list of URLs to a JSON file named after the base URL's hostname."""
    parsed_url = urlparse(base_url)
    hostname = parsed_url.hostname
    if hostname:
        # Use only the hostname for the filename, without the scheme
        filename = f"{hostname}.json"
        all_links = {'urls': urls}
        with open(filename, 'w') as f:
            json.dump(all_links, f)
    else:
        print("Invalid URL, cannot extract hostname.")

if __name__ == "__main__":
    url = input("Input a link to get endpoins: ")
    
    wiki_urls = fetch_and_parse_url(url)
    
    # Print each URL on a new line
    [print(url) for url in wiki_urls]
    
    save_urls_to_json(wiki_urls, url)