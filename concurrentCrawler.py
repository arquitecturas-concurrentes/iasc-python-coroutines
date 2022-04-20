import sys
import requests
import threading
from bs4 import BeautifulSoup

def get_urls_from_root(root_url):
    soup = BeautifulSoup(reqs.text, 'html.parser')
    return soup.find_all('a')

def fetch(url):
    sock = socket.socket()
    sock.connect(('bla.com', 80))
    request = 'GET {} HTTP/1.0\r\nHost: bla.com\r\n\r\n'.format(url)
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    parse_response(response)

if __name__ == '__main__':
    root_url = sys.argv[1]
    urls = [link.get('href') for link in get_urls_from_root(root_url)]

    for url in urls:
        t = threading.Thread(target=fetch, args=(i,))
        t.start()