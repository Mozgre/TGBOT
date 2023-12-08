import asyncio
from aiogram import Bot, Dispatcher,executor
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery    

bot = Bot(token="6858592542:AAFawrZn-_hBsmn77n8eGdE5fChv9Y3P02o")
loop = asyncio.get_event_loop()
dp = Dispatcher(bot,loop=loop)

@dp.message_handler(commands=['start'])
async def command_start_handler(message: Message):
    await bot.send_message(
        chat_id= message.from_user.id,
        text='Привет, я Бот для просмотра расписания КПК,нажми на кнопку:',
        reply_markup= InlineKeyboardMarkup(
            inline_keyboard= [[InlineKeyboardButton(text='Вывести список групп', callback_data='11')]]
        )
    )
@dp.callback_query_handler(lambda callback_query: callback_query.data)
async def callback_query (callback_query : CallbackQuery):
    if callback_query.data == '11':
        await bot.send_message(
            chat_id = callback_query.from_user.id,
            text= "Список Групп:",
            reply_markup = InlineKeyboardMarkup(
                inline_keyboard=[
                [InlineKeyboardButton(text="2-1P11",callback_data='1'),
                InlineKeyboardButton(text="3-2P9",callback_data='2'),
                InlineKeyboardButton(text="Назад", callback_data='3')]            
                ])
        )
    if callback_query.data == '3':
        await bot.send_message(
        chat_id= callback_query.from_user.id,
        text='Привет, я Бот для просмотра расписания КПК,нажми на кнопку:',
        reply_markup= InlineKeyboardMarkup(
            inline_keyboard= [[InlineKeyboardButton(text='Вывести список групп', callback_data='11')]]
        )
    )
    # elif callback_query.data == '12':
    #     buttons=[]
    #     for list in list:
    #         buttons.append([InlineKeyboardButton(text=list)])
    #     await bot.send_message(
    #         chat_id = callback_query.from_user.id,
    #         text="gey",
    #         reply_markup= InlineKeyboardMarkup (inline_keyboard=[[InlineKeyboardButton(text="Net",callback_data="1")]])
    #     )
if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)