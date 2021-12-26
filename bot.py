from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = '12371263817623812638716238716'
chat_id = "chat id"

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    # ебануть текста сюды
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(content_types=types.ContentType.ANY)
async def echo(message: types.Message):
    print(message.from_user.id)
    await bot.copy_message(chat_id = chat_id, from_chat_id = message.from_user.id, message_id = message.message_id	)

if __name__ == '__main__':
    executor.start_polling(dp)
