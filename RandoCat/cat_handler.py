from PIL import Image
import aiohttp
import random
import io

async def fetch_cat(_id = random.random()):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://thiscatdoesnotexist.com/?{_id}') as res:
            return Image.open(io.BytesIO(await res.read())).save('cat.jpg')
