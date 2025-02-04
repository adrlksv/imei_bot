import json

from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import StatesGroup, State

import aiohttp

from bot.config import settings
from bot.keyboards.keyboard import auth_buttons, main_buttons


router = Router()


class AuthStates(StatesGroup):
    waiting_email = State()
    waiting_password = State()
    waiting_register_email = State()
    waiting_register_login = State()
    waiting_register_password = State()
    waiting_imei = State()
    authenticated = State() 


@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Привет! Войдите или зарегистрируйтесь.", reply_markup=auth_buttons)


@router.message(lambda message: message.text == "✅ Войти")
async def login(message: types.Message, state: FSMContext):
    await message.answer("Введите email:")
    await state.set_state(AuthStates.waiting_email)


@router.message(lambda message: message.text == "👤 Регистрация")
async def register(message: types.Message, state: FSMContext):
    await message.answer("Введите email для регистрации:")
    await state.set_state(AuthStates.waiting_register_email)


@router.message(StateFilter(AuthStates.waiting_register_email))
async def process_register_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Придумайте логин:")
    await state.set_state(AuthStates.waiting_register_login)


@router.message(StateFilter(AuthStates.waiting_register_login))
async def process_register_login(message: types.Message, state: FSMContext):
    await state.update_data(login=message.text)
    await message.answer("Придумайте пароль:")
    await state.set_state(AuthStates.waiting_register_password)


@router.message(StateFilter(AuthStates.waiting_register_password))
async def process_register_password(message: types.Message, state: FSMContext):
    data = await state.get_data()
    
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{settings.API_URL}/auth/register", json={
            "email": data["email"],
            "login": data["login"],
            "password": message.text
        }) as resp:
            response_json = await resp.json()
            
            if resp.status == 200:
                await message.answer("Вы успешно зарегистрированы! Теперь войдите в аккаунт.", reply_markup=auth_buttons)
            else:
                await message.answer(f"Ошибка регистрации: {response_json.get('detail', 'Неизвестная ошибка')}")
    
    await state.clear()


@router.message(lambda message: message.text == "✅ Войти")
async def login(message: types.Message, state: FSMContext):
    await message.answer("Введите email:")
    await state.set_state(AuthStates.waiting_email)


@router.message(StateFilter(AuthStates.waiting_email))
async def process_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Введите пароль:")
    await state.set_state(AuthStates.waiting_password)


@router.message(StateFilter(AuthStates.waiting_password))
async def process_password(message: types.Message, state: FSMContext):
    data = await state.get_data()
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{settings.API_URL}/auth/login", json={
            "email": data["email"],
            "password": message.text
        }) as resp:
            if resp.status == 200:
                cookies = resp.cookies
                print(f"Cookies received: {cookies}")
                token = cookies.get('imei_access_token')
                if token:
                    token_value = token.value
                    print(f"Token from cookies: {token_value}")
                    await state.update_data(token=token_value)
                    await state.set_state(AuthStates.authenticated)
                    await message.answer("Вы успешно вошли!", reply_markup=main_buttons)
                else:
                    await message.answer("Токен не найден в куках.")
            else:
                response_json = await resp.json()
                await message.answer(f"Ошибка авторизации: {response_json.get('detail', 'Неизвестная ошибка')}")


@router.message(lambda message: message.text == "🔎 Проверить IMEI")
async def ask_imei(message: types.Message, state: FSMContext):
    await message.answer("Введите IMEI для проверки:")
    await state.set_state(AuthStates.waiting_imei)

@router.message(StateFilter(AuthStates.waiting_imei))
async def check_imei(message: types.Message, state: FSMContext):
    imei = message.text
    
    async with aiohttp.ClientSession() as session:
        headers = {
            'Authorization': f'Bearer {settings.TOKEN_SANDBOX}',
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        async with session.post(f"{settings.API_URL}/check-imei/", json={"imei": imei}, headers=headers) as resp:
            if resp.status == 200:
                result = await resp.json()
                await message.answer(f"Результат: {result}", reply_markup=main_buttons)
            else:
                try:
                    response_json = await resp.json()
                    await message.answer(f"Ошибка: {response_json.get('detail', 'Неизвестная ошибка')}")
                except json.JSONDecodeError:
                    response_text = await resp.text()
                    await message.answer(f"Ошибка: {response_text}")

    await state.clear()
