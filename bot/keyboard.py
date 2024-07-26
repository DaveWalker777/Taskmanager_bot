from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Выбрать данные")],
            [KeyboardButton(text="Выбрать тему по ID")],
            [KeyboardButton(text="Добавить тему")],

        ],
        resize_keyboard=True
    )
    return keyboard
