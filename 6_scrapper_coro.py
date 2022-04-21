import sys
import asyncio
from bs4 import BeautifulSoup

def get_urls_from_root(root_url):
    soup = BeautifulSoup(reqs.text, 'html.parser')
    return soup.find_all('a'):

async def fetch(url):
    await r = get_non_block(url)
    await parse_response(r.content) #Content of the response, in bytes

async def parse_response(response):
    hace_su_magia(response)

async def main():
    root_url = sys.argv[1]
    urls = [link.get('href') for link in get_urls_from_root(root_url)]

    for url in urls:
        task = asyncio.create_task(fetch(url))
        await task

asyncio.run(main())