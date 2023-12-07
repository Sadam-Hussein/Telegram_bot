import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

Token = '6594051922:AAHK06ngrvDanukwIWGam3RS7zqRxnPF4x4'

bot = Bot(token=Token)
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.full_name}!")


@dp.message(Command("help"))
async def handle_help(message: types.Message):
    text = "При моей помощи Вы можете узнать расписание в центре ИКТ, для этого пропишите команду \"get\""
    await message.answer(text=text)


# @dp.message()
# async def echo(message: types.Message):
#     await bot.send_message(
#        chat_id=message.chat.id,
#        text='Wait...'
#     )
#     if message.text:
#         await message.answer(text=message.text)
#     else:
#         await message.reply(text='Wrong command')


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
