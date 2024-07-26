import aiohttp
from config import API_URL, API_URL_CREATE_THEME

async def fetch_tasks(offset=0, limit=10):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}&offset={offset}&limit={limit}") as response:
            data = await response.json()
            return data


async def fetch_theme_by_id(theme_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}/{theme_id}") as response:
            if response.status == 200:
                data = await response.json()
                return data
            return None


async def create_theme(title):
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL_CREATE_THEME, json={'title': title}) as response:
            if response.status == 201:
                return True
            return False
