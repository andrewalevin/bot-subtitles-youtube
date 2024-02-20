import asyncio
import datetime
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.client import bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BufferedInputFile, BotCommand
from aiogram.utils.markdown import hbold

import config
import subtitles

from dotenv import dotenv_values

secrets = dotenv_values(".env")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(config.START_TEXT)


@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    await message.answer(config.START_TEXT)


async def demo_command(message: Message, demo_request: str) -> None:
    answer_text = subtitles.main_subtitles(demo_request)
    await message.reply(demo_request)

    if len(answer_text) < config.MAX_TELEGRAM_BOT_TEXT_SIZE:
        await message.reply(answer_text)
    else:
        await message.reply_document(BufferedInputFile(answer_text.encode(), filename=get_filename_txt()))


@dp.message(Command("demo1"))
async def command_help_handler(message: Message) -> None:
    await demo_command(message, config.DEMO_1_REQUEST)


@dp.message(Command("demo2"))
async def command_help_handler(message: Message) -> None:
    await demo_command(message, config.DEMO_2_REQUEST)


def get_filename_txt():
    return f'subtitles-{int(datetime.datetime.now().timestamp())}.txt'


@dp.message()
async def echo_handler(message: types.Message) -> None:
    answer_text = subtitles.main_subtitles(message.text)
    if len(answer_text) < config.MAX_TELEGRAM_BOT_TEXT_SIZE:
        await message.reply(answer_text)
    else:
        await message.reply_document(BufferedInputFile(answer_text.encode(), filename=get_filename_txt()))




LEXICON_COMMANDS_RU: dict[str, str] = {
    '/start': 'Start',
    '/help': 'Help',
    '/demo1': 'Demo 1',
    '/demo2': 'Demo 2'
}


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in LEXICON_COMMANDS_RU.items()
    ]
    await bot.set_my_commands(main_menu_commands)


async def main() -> None:

    bot = Bot(secrets['TOKEN'], parse_mode=ParseMode.HTML)

    await set_main_menu(bot)

    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())