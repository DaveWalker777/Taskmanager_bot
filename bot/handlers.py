import logging
from aiogram import Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove
from keyboard import get_reply_keyboard
from api import fetch_tasks, fetch_theme_by_id, create_theme

async def send_welcome(message: types.Message):
    keyboard = get_reply_keyboard()
    await message.answer("Выберите одну из кнопок:", reply_markup=keyboard)

async def ask_number_of_themes(message: types.Message):
    await message.answer("Сколько тем вы хотите получить? Пожалуйста, введите количество.", reply_markup=ReplyKeyboardRemove())

async def handle_number_of_input(message: types.Message):
    number_of_themes = int(message.text)
    data = await fetch_tasks(limit=number_of_themes)
    result = ""

    for theme in data["results"]:
        theme_id = theme["id"]
        theme_title = theme["title"]
        result += f"ID темы: {theme_id}\nНазвание темы: {theme_title}\n\n"

        for task in theme["tasks"]:
            task_id = task["id"]
            task_title = task["title"]
            task_description = task["task"]
            task_date = task["date"]
            task_time = task["time"]
            result += (f"ID задачи: {task_id}\n"
                       f"Title: {task_title}\n"
                       f"Task: {task_description}\n"
                       f"Date: {task_date}\n"
                       f"Time: {task_time}\n\n")

    if result:
        await message.answer(result)
    else:
        await message.answer("Нет доступных задач.")

    # Show keyboard again if needed
    keyboard = get_reply_keyboard()
    await message.answer("Вы можете выбрать данные снова:", reply_markup=keyboard)

async def ask_theme_id(message: types.Message):
    await message.answer("TEST", reply_markup=ReplyKeyboardRemove())

async def handle_theme_id(message: types.Message):
    theme_id_str = message.text
    if not theme_id_str.isdigit():
        await message.answer("Пожалуйста, введите корректный ID темы.")
        return

    theme_id = int(theme_id_str)
    data = await fetch_theme_by_id(theme_id)

    if data:
        result = f"ID темы: {data['id']}\nНазвание темы: {data['title']}\n\n"

        for task in data["tasks"]:
            task_id = task["id"]
            task_title = task["title"]
            task_description = task["task"]
            task_date = task["date"]
            task_time = task["time"]
            result += (f"ID задачи: {task_id}\n"
                       f"Title: {task_title}\n"
                       f"Task: {task_description}\n"
                       f"Date: {task_date}\n"
                       f"Time: {task_time}\n\n")

        await message.answer(result)
    else:
        await message.answer("Тема с таким ID не найдена.")

    # Show keyboard again if needed
    keyboard = get_reply_keyboard()
    await message.answer("Вы можете выбрать данные снова:", reply_markup=keyboard)

async def ask_theme_title(message: types.Message):
    await message.answer("Укажите название темы.", reply_markup=ReplyKeyboardRemove())

async def handle_theme_title(message: types.Message):
    theme_title = message.text
    success = await create_theme(theme_title)

    if success:
        await message.answer("Тема успешно добавлена!")
    else:
        await message.answer("Не удалось добавить тему.")

    # Show keyboard again if needed
    keyboard = get_reply_keyboard()
    await message.answer("Вы можете выбрать данные снова:", reply_markup=keyboard)

def register_handlers(dp: Dispatcher):
    dp.message.register(send_welcome, Command("start"))
    dp.message.register(ask_number_of_themes, lambda message: message.text == "Выбрать данные")
    dp.message.register(handle_number_of_input, lambda message: message.text.isdigit())
    dp.message.register(ask_theme_id, lambda message: message.text == "Выбрать тему по ID")
    dp.message.register(handle_theme_id, lambda message: message.text.isdigit())
    dp.message.register(ask_theme_title, lambda message: message.text == "Добавить тему")
    dp.message.register(handle_theme_title, lambda message: not message.text.isdigit())
