import asyncio
import logging
import openpyxl

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

from scheldue import ScheldueInit

Token = '6594051922:AAHK06ngrvDanukwIWGam3RS7zqRxnPF4x4'

bot = Bot(token=Token)
dp = Dispatcher()


scheldueInit = ScheldueInit('16.11.2023.xlsx', openpyxl)


@dp.message(Command("get"))
async def handle_get(message: types.Message):
    
    await message.answer(text="""
    1. Кто оккупировал кабинет?
    2. Какие у папы суриката пары?
    3. Кто из папы сурикатов свободен?
    4. Какие пары у группы сурикатов?
    5. С кем поменяться ключами?
    6. Какой кабинет свободен?
    Действие:
    """)


@dp.message()
async def handle_get(message: types.Message):
    
    result = "Я тебя не понял"

    if message.text == "1":

        result = "Введите номер кабинета:"
        await message.answer(text=result)
    
    


# @dp.message()
# async def handle_get(message: types.Message):
#     result = "Я тебя не понял"
#     if message.text == "1":
#         result = scheldueInit.find_by_cabinet(cabinet)
#     await message.answer(text=str(result))


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
