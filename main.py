import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.models import async_main

bot = Bot(token="7163339025:AAH3WCXsQvpM2kQSQmNlqVoOtj5f1D_jn6M") #токен бота сохроняется в переменную bot
dp = Dispatcher() #сокрашение для Despatcher а

#Функции ниже для запуска бота
async def main():
    await async_main() #Вызываем функцию создания таблий при запуске файла
    dp.include_router(router) # Добовляем роутер в дп чтобы корректно работали друшгие файлы
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:# Чтобы вместо ошибки при завершении работы программы (ctrl+c) выводилось "Бот выключен"
        print("Бот выключен")



