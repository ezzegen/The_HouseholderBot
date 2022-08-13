import telebot


def main_kb():
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text='Меню', callback_data='menu')
    keyboard.add(button)
    return keyboard


def line_kb():
    name_but = ['Помощь', 'Дата', 'Погода', 'Растения','Рецепты']
    call_b = ['help', 'date', 'weather', 'flowers', 'recipes']
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(*[telebot.types.InlineKeyboardButton(text=i, callback_data=j)
                 for i, j in zip(name_but, call_b)])
    return keyboard


def flowers_kb():
    flower_callb = [
        'anturium', 'chlor', 'coffee',
        'dollar', 'eucharis', 'ficus',
        'carissa', 'krassula', 'calatea'
        'myrtle', 'pomegranate', 'spatifillum'
                    ]
    flowers_but = [
        'Антуриум', 'Хлорофиттум', 'Кофе',
        'Долл.дерево', 'Эухарис', 'Фикус',
        'Карисса', 'Крассула', 'Калатея',
        'Мирт', 'Гранат', 'Спатифиллум'
                    ]
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(*[telebot.types.InlineKeyboardButton(text=i, callback_data=j)
                   for i, j in zip(flowers_but, flower_callb)])
    return keyboard


def recipes_kb():
    recipe_callb = ['first', 'second', 'dessert', 'drink', 'snacks']
    recipe_menu = ['Первое', 'Второе', 'Десерты', 'Напитки', 'Закуски']
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(*[telebot.types.InlineKeyboardButton(text=i, callback_data=j)
                   for i, j in zip(recipe_menu, recipe_callb)])
    return keyboard


def second_kb():
    second_callb = ['chicken', 'fish', 'meat', 'vegetables']
    second_mn = ['Курица', 'Рыба', 'Мясо', 'Овощи']
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(*[telebot.types.InlineKeyboardButton(text=i, callback_data=j)
                   for i, j in zip(second_mn, second_callb)])
    return keyboard


if __name__ == '__main__':
    main_kb()
    line_kb()
    flowers_kb()
    recipes_kb()
