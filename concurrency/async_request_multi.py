import aiohttp
import async_timeout
import asyncio
import time

async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start}')
            return response.status



#New solution without deprecation warning:
async def get_multiple_pages(*urls):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

urls = ['http://google.com' for _ in range(50)]
start = time.time()

asyncio.run(get_multiple_pages(*urls))
print(f'All took {time.time()-start}')

# Original - video - solution:
# async def get_multiple_pages(loop, *urls):
#     tasks = []
#     async with aiohttp.ClientSession(loop=loop) as session:
#         for url in urls:
#             tasks.append(fetch_page(session, url))
#         grouped_tasks = asyncio.gather(*tasks)
#         return await grouped_tasks

# loop = asyncio.get_event_loop()
# urls = ['http://google.com' for _ in range(50)]

# start = time.time()
# loop.run_until_complete(get_multiple_pages(loop, *urls))
# print(f'All took {time.time()-start}')