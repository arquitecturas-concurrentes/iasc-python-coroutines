import sys
import requests
import aiohttp
import asyncio
from bs4 import BeautifulSoup

def get_urls_from_root(root_url):
    reqs = requests.get(root_url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    return soup.find_all('a')

async def fetch(root_url, url):
    full_url = root_url+url
    r = await aiohttp.request('GET', full_url)
    await parse_response(r.status_code, full_url) #Content of the response, in bytes

async def parse_response(status_code, url):
    if status_code == 200:
      print(url)

async def main():
    root_url = sys.argv[1]
    urls = [link.get('href') for link in get_urls_from_root(root_url)]
    local_urls = [url for url in urls if url.startswith('/')]

    for url in local_urls:
        task = asyncio.create_task(fetch(root_url, url))
        await task

asyncio.run(main())
# python3 6_scrapper_coro.py http://xcd.com