import sys
import requests
import threading
from bs4 import BeautifulSoup

def get_urls_from_root(root_url):
    reqs = requests.get(root_url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    return soup.find_all('a')

def fetch(root_url, url):
    full_url = root_url+url
    r = requests.get(root_url+url)
    parse_response(r.status_code, full_url) #Content of the response, in bytes

def parse_response(status_code, url):
    if status_code == 200:
      print(url) 

if __name__ == '__main__':
    root_url = sys.argv[1]
    urls = [link.get('href') for link in get_urls_from_root(root_url)]
    local_urls = [url for url in urls if url.startswith('/')]

    for url in local_urls:
        t = threading.Thread(target=fetch, args=(root_url, url))
        t.start()
# python3 intro.py http://xkcd.com