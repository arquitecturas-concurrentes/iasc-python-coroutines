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
    async with aiohttp.ClientSession() as session:
        full_url = root_url+url
        async with session.get(full_url) as resp:
            if resp.status == 200:
                print(full_url)

async def main():
    root_url = sys.argv[1]
    urls = [link.get('href') for link in get_urls_from_root(root_url)]
    local_urls = [url for url in urls if url.startswith('/')]
    tasks = []

    for url in local_urls:
        tasks.append(asyncio.create_task(fetch(root_url, url)))
    await asyncio.gather(*tasks)

asyncio.run(main())
# python3 6_scrapper_coro.py http://xkcd.com