from aiogram import Bot, Dispatcher, executor, types
from cat_handler import CatFetcher
from emoji import emojize
import asyncio
import random
import json


def parse_config(file: str):
    with open(file) as cfg:
        data = json.load(cfg)

    return data


bot = Bot(token=parse_config('config.json')['API_TOKEN'])
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    message_welcome = parse_config('config.json')['WELCOME_MESSAGE']
    await message.reply(message_welcome)


@dp.message_handler(commands=['cat', 'random'])
async def random_cat(message: types.Message):
    captions = ["Hold the cat!", "What lovely eyes! :eyes:", "Here's the cat!"]
    caption = random.choice(captions)
    cat = CatFetcher()
    asyncio.create_task(cat.fetch_cat())
    photo = open(('cat.jpg').encode('utf-8'), 'rb')
    # _id = random.random()
    await bot.send_photo(chat_id=message.chat.id,
                         # photo = f'https://thiscatdoesnotexist.com/?{_id}',
                         photo=photo,
                         caption=emojize(
                             caption) if caption == captions[1] else caption,
                         reply_to_message_id=message.message_id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
