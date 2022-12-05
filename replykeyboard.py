from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging


start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔍Qidirish")
        ],
        [
            KeyboardButton(text="✍Fikr bildirish"),
            KeyboardButton(text="🔁Tilni o'zgartirish")
        ],
        [
            KeyboardButton(text="🎯Mening Joylashuvim: ")
        ],
        [
            KeyboardButton(text="Qanday qo'llash mumkin❔"),
        ]
    ]
)
