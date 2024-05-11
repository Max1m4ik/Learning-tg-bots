from aiogram import F, Router
from aiogram.types import Message , CallbackQuery
from aiogram.filters import CommandStart,Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb 

router = Router()

class Register(StatesGroup):  # Делаем состояния для регестрации
    name = State()
    age = State()
    number = State()


@router.message(CommandStart())    #Функция при команде /start
async def cmd_start(message: Message):
    await message.answer("Привет!", reply_markup=kb.main) #Вызываем клавиатуру main из файла keyboards
    await message.reply("Как дела?")

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Вы нажали на кнопку помощи")

@router.message(F.text == "Каталог") #Если в клавиатуре main выбрали католог вызываем клавиатуру catalog                                                                               
async def cmd_help(message: Message):#проверяем на текст тк как это Reply клавиатура (отправляет текст)
    await message.answer("Выберите категорию товара", reply_markup=kb.catalog) 

@router.callback_query(F.data == "t-shirts") #Если в клавиатуре catalog выбрали футболки(возврашяется t-shorts)
async def t_shirt(callback: CallbackQuery):#Отправляем уведомление с подтверждением и пишем текст
    await callback.answer("Вы выбрали категорию", show_alert = True)#Мы проверяли на data потомучто это inline клавиатура
    await callback.message.answer("Вы выбрали категорию футболок.")#Которая возврашяет data (callback_data)

@router.message(Command("register"))# При команде register делаем состояние Register.name и спрашиваем текстом имя
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer("Введите ваше имя")

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext): #Когда на послали сообщение в ответ записываем его
    await state.update_data(name = message.text)#в переменную name и меняем состояние на Register.age и спрашиваем возраст
    await state.set_state(Register.age)
    await message.answer("Введите ваш возвраст")

@router.message(Register.age)#После ответа записываем его в переменную age и меняем состояние на Register.number
async def register_age(message: Message, state: FSMContext):#Но на этот раз вызываем клавиатуру get_number из keyboards.py    await state.update_data(age = message.text)
    await state.set_state(Register.number)
    await message.answer("Отправте ваш номер телефона", reply_markup=kb.get_number)

@router.message(Register.number, F.contact)#Когда нам отправляют именно контакт 
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number = message.contact.phone_number)#Берём от туда толко номер и записываем в переменную number
    data = await state.get_data()# Записываем все ответы в data у и с помошью f строки выводим все данные пользователю
    await message.answer(f"Ваше имя: {data['name']}\nВаш возвраст: {data['age']}\nНомер: {data['number']}")
    await state.clear() # И очишаем состояния