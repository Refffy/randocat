from PIL import Image
import aiohttp
import random
import io


class CatFetcher:
    def __init__(self):
        self.__id = random.random()
        self.__link = f'https://thiscatdoesnotexist.com/?{self.__id}'

    async def fetch_cat(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.__link) as res:
                return Image.open(io.BytesIO(await res.read())).save('cat.jpg')
