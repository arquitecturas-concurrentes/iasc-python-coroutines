import sys
import requests
import socket
import re
import logging
import ssl
import threading
from bs4 import BeautifulSoup
from urllib.parse import urlparse

http_header_delimiter = b'\r\n\r\n'
content_length_field = b'Content-Length:'
http_prefix = b'HTTP/1.1'


def get_urls_from_root(root_url):
    reqs = requests.get(root_url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    return soup.find_all('a')

def fetch(root_url, url):
    full_url = root_url+url
    hostname = strip_scheme(root_url)
    print(f"URL to get: {full_url}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((hostname, 443))
    sock.settimeout(4)
    context = ssl.create_default_context()
    ssock = context.wrap_socket(sock, server_hostname=hostname)
    request = 'GET {} HTTP/1.1\r\nHost:{}\r\n\r\n'.format(url, hostname)
    ssock.send(request.encode())
    parse_response(read_response(ssock, url), full_url)

def read_response(ssock, url):
    response = b''
    try:
        while True:
            data = ssock.recv(4096)
            logging.debug(f'receiving {len(data)} bytes data...')
            response += data
            if not data or all_data_received(response):
                print("closing connection")
                ssock.close()
                break
    except socket.timeout as e:
        logging.debug(f'Timeout out for {url}.')
    ssock.close()
    return response

def all_data_received(response):
    return attempt_full_lenght(response) == len(response)

def attempt_full_lenght(data):
    header, _body = separate_header_and_body(data)
    return get_content_length(header) + len(header)

def parse_response(response, url):
    print(f'Received response from {url}')
    header, data = separate_header_and_body(response)
    http_response_code = get_repsonse_code(header)
    content_length = get_content_length(header)

    print(f'Raw header: {header.decode()}')
    print(f'Code: {http_response_code}. Content lenght: {content_length}')

def get_content_length(header):
    for line in header.split(b'\r\n'):
        if content_length_field in line:
            return int(line[len(content_length_field):])
    return 0

def get_repsonse_code(header):
    for line in header.split(b'\r\n'):
        if http_prefix in line:
            return int("".join(re.findall(r"\d+", line[len(http_prefix):].decode())))
    return 0

def separate_header_and_body(data):
    '''
    Returns a the tuple (header, body) from the given array of bytes. If
    the given array doesn't contain the end of header signal then it is
    assumed to be all header.
    '''
    try:
        index = data.index(http_header_delimiter)
    except:
        return (data, bytes())
    else:
        index += len(http_header_delimiter)
        return (data[:index], data[index:])

def strip_scheme(url):
    parsed = urlparse(url)
    scheme = "%s://" % parsed.scheme
    return parsed.geturl().replace(scheme, '', 1)

if __name__ == '__main__':
    root_url = sys.argv[1]
    urls = [link.get('href') for link in get_urls_from_root(root_url)]

    for url in urls:
        if urlparse(url).hostname and root_url not in urlparse(url).hostname:
            continue
        t = threading.Thread(target=fetch, args=(root_url,url,))
        t.start()