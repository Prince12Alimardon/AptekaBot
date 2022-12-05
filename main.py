from aiogram import executor
from aiogram.types import Message, CallbackQuery
from config import dp, bot
from replykeyboard import start_button
import logging

@dp.message_handler(commands='start')
async def start(message: Message):
    await message.answer(f"📲👇 Kerakli bo'limni tanlang yoki 💊 dori nomini kiriting.", reply_markup=start_button)



if __name__ == '__main__':
    executor.start_polling(dp)