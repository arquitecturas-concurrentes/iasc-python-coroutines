import sys
import requests
import threading
from bs4 import BeautifulSoup

def get_urls_from_root(root_url):
    soup = BeautifulSoup(reqs.text, 'html.parser')
    return soup.find_all('a')

def fetch(url):
    r = requests.get(url)
    parse_response(r.content) #Content of the response, in bytes

def parse_response(response):
    hace_su_magia(response)

if __name__ == '__main__':
    root_url = sys.argv[1]
    urls = [link.get('href') for link in get_urls_from_root(root_url)]

    for url in urls:
        t = threading.Thread(target=fetch, args=(i,))
        t.start()