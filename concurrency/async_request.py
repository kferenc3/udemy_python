import aiohttp
import asyncio
import time

async def fetch_page(url):
    page_start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start}')
            return response.status

#New solution without deprecation warning:
async def main():
    tasks = [fetch_page('http://google.com') for i in range(50)]
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
print(f'All took {time.time()-start}')

#Original - video - solution:
#loop = asyncio.get_event_loop()
#start = time.time()
#loop.run_until_complete(asyncio.gather(*tasks))
#print(f'All took {time.time()-start}')