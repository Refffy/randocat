from PIL import Image
import aiohttp
import random
import io


class CatFetcher:
    def __init__(self):
        self._id = random.random()
        self._link = f'https://thiscatdoesnotexist.com/?{self._id}'

    async def fetch_cat(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self._link) as res:
                return Image.open(io.BytesIO(await res.read())).save('cat.jpg')
