import asyncio
import requests
import tkpk.management.command.navigation as nav
from aiogram import Bot, Dispatcher,executor
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery    

bot = Bot(token="6858592542:AAFawrZn-_hBsmn77n8eGdE5fChv9Y3P02o")
loop = asyncio.get_event_loop()
dp = Dispatcher(bot,loop=loop)
headers = {
    
}

@dp.message_handler(commands=['start'])
async def command_start_handler(message: Message):
    text, reply_markup = nav.get_reply_message({"new_state":1})
    await bot.send_message(
        chat_id= message.from_user.id,
        text=text,
        reply_markup= reply_markup
        )
    # if callback_query.data == '2':
    #     await bot.send_message(
    #         chat_id=message.from_user.id,
    #         text="Monstr",
    #         reply_markup= InlineKeyboardMarkup(
    #             inline_keyboard= [[InlineKeyboardButton(text='Назад', callback_data='1')]]
    #         )
    #     )
@dp.callback_query_handler(lambda callback_query: callback_query.data)
async def callback_query (callback_query : CallbackQuery):
    context = eval(callback_query.data)
    text, reply_markup = nav.get_reply_message(context)
    await bot.send_message(
        chat_id= callback_query.from_user.id,
        text=text,
        reply_markup= reply_markup
        )
def get_page(url):
    pass
def main():
    get_page(url="")
    # if context['new_state'] == 11:
    #     await bot.send_message(
    #     chat_id= callback_query.from_user.id,
    #     text=text,
    #     reply_markup= reply_markup
    # )
    # if context['new_state'] == 1:
    #     await bot.send_message(
    #     chat_id= callback_query.from_user.id,
    #     text=text,
    #     reply_markup= reply_markup
    # )
    # if context['new_state'] == 2:
    #     await bot.send_message(
    #     chat_id= callback_query.from_user.id,
    #     text=text,
    #     reply_markup= reply_markup
    # )
    # if context['new_state'] == 3:
    #     await bot.send_message(
    #     chat_id= callback_query.from_user.id,
    #     text=text,
    #     reply_markup= reply_markup
    # )
    # elif callback_query.data == '12':
    #     buttons=[]
    #    for list in list:
    #         buttons.append([InlineKeyboardButton(text=list)])
    #     await bot.send_message(
    #         chat_id = callback_query.from_user.id,
    #         text="gey",
    #         reply_markup= InlineKeyboardMarkup (inline_keyboard=[[InlineKeyboardButton(text="Net",callback_data="1")]])
    #     )
if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)
    main()