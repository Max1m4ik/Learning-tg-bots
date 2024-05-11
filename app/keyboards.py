from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
 
main = ReplyKeyboardMarkup(keyboard= # Клавиатура main под вводом текста (Reply клавиатура)
    [[KeyboardButton(text="Каталог")],   #Три ряда кнопок под клавиатурой Два ряда с одной кнопкой и один с двумя, 
    [KeyboardButton(text="Корзина")],   #при нажатии на кнопку сообшение из переменной text пишется в чат
    [KeyboardButton(text="Контакты"),KeyboardButton(text="О нас")]], 
    resize_keyboard=True,                                  #Делаем кнопки меньше
    input_field_placeholder="Выберите пункт меню...") #То что будет написанно в поле ввода текста у пользователя 

catalog = InlineKeyboardMarkup(inline_keyboard=  # Клавиатура catalog под сообшением (Inline клавиатура) 
    [[InlineKeyboardButton(text="Футболки", callback_data="t-shirts")], #Возврашяет через data с помошью функции callback
    [InlineKeyboardButton(text="Кроссовки", callback_data="sneakers")], #функции callback_data текст
    [InlineKeyboardButton(text="Бейсболки", callback_data="caps")]])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="отправить номер", # Reply клавиатура get_number
                                    request_contact=True,resize_keyboard=True)]]) #запрашивает котакт пользователя
                                                                    # С помошью функции request_contact=True
