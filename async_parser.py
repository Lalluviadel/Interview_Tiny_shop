from bs4 import BeautifulSoup

import asyncio
import aiohttp


async def make_request(main_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=main_url) as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')

            # получаем список ссылок на страницы категорий, убираем последнюю ссылку (на авторизацию)
            pages = [f'{main_url[:-1]}{a["href"]}' for a in soup.find('div', class_='nav').find_all('a', href=True)]
            pages.pop()

        tasks = [parsing_page(session, url) for url in pages]
        await asyncio.gather(*tasks)


async def parsing_page(session, url):
    async with session.get(url=url) as response:
        response_text = await response.text()
        with open(f'{url[-2]}.html', 'w') as f:
            f.write(response_text)


loop = asyncio.get_event_loop()
loop.run_until_complete(make_request('http://127.0.0.1:8002/'))
