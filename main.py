import asyncio
import datetime
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, BufferedInputFile
from aiogram.utils.markdown import hbold

import config
import subtitles

from dotenv import dotenv_values

secrets = dotenv_values(".env")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(config.START_TEXT)


@dp.message()
async def echo_handler(message: types.Message) -> None:
    answer_text = subtitles.main_subtitles(message.text)
    if len(answer_text) < 4095:
        await message.reply(answer_text)
    else:
        await message.reply_document(BufferedInputFile(
            answer_text.encode(),
            filename=f'subtitles-{int(datetime.datetime.now().timestamp())}.txt'
        ))


async def main() -> None:

    bot = Bot(secrets['TOKEN'], parse_mode=ParseMode.HTML)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())