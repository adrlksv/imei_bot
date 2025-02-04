# IMEI Checker Bot

Этот проект представляет собой Telegram-бота для проверки IMEI номеров с использованием API FastAPI.

📌 Возможности

- Регистрация и аутентификация пользователей

- Проверка IMEI через API

- Удобный интерфейс на базе aiogram3

🚀 Запуск проекта

1. Клонирование репозитория
```
git clone https://github.com/adrlksv/imei_bot.git
cd imei_bot
```
2. Установка зависимостей

Создайте виртуальное окружение и установите зависимости:
```
python -m venv .venv
source .venv/bin/activate  # Для Linux/MacOS
.venv\Scripts\activate    # Для Windows
python -m pip install -r requirements.txt
```
3. Настройка переменных окружения

Создайте файл .env и добавь нужные параметры:

API_URL=http://127.0.0.1:8000  # Адрес FastAPI сервера
BOT_TOKEN=your_telegram_bot_token  # Токен Telegram-бота
TOKEN_SANDBOX=your_api_key  # API-ключ для проверки IMEI
...

4. Запуск сервера FastAPI
```
uvicorn src.backend.main:app --reload
```

5. Запуск Telegram-бота

Откройте новый терминал, запустите бота:
```
python bot/run.py
```
📖 Использование

1. Запусти бота в Telegram, отправив команду /start.

2. Выбери "✅ Войти" или "👤 Регистрация".

3. После входа используй кнопку "🔎 Проверить IMEI".

4. Введи IMEI-номер, и бот отправит результат проверки.

🛠 Технологии

- FastAPI – серверная часть

- PostgreSQL – база данных

- aiogram3 – Telegram-бот

- aiohttp – HTTP-запросы к API
