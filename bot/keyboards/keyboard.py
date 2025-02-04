from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


auth_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Войти")],
        [KeyboardButton(text="👤 Регистрация")]
    ],
    resize_keyboard=True
)

main_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔎 Проверить IMEI")],
        [KeyboardButton(text="❌ Выйти")]
    ],
    resize_keyboard=True
)
