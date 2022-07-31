import telebot


def main_kb():
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text='Меню', callback_data='menu')
    keyboard.add(button)
    return keyboard


def line_kb():
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_help = telebot.types.InlineKeyboardButton(text='Помощь', callback_data='help')
    button_date = telebot.types.InlineKeyboardButton(text='Дата', callback_data='date')
    button_weather = telebot.types.InlineKeyboardButton(text='Погода', callback_data='weather')
    button_flowers = telebot.types.InlineKeyboardButton(text='Растения', callback_data='flowers')
    keyboard.add(button_help, button_date, button_weather, button_flowers)
    return keyboard


def flowers_kb():
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_kal = telebot.types.InlineKeyboardButton(text='Калатея', callback_data='calatea')
    button_kar = telebot.types.InlineKeyboardButton(text='Карисса', callback_data='carissa')
    button_eu = telebot.types.InlineKeyboardButton(text='Эухарис', callback_data='eucharis')
    keyboard.add(button_kar, button_kal, button_eu)
    return keyboard


if __name__ == '__main__':
    main_kb()
    line_kb()
    flowers_kb()
