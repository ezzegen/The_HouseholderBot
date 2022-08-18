from bot import bot as bot
import telebot
from content import phrase, date, weather
from content.flowers import flower, images
from content.recipes import recipe
from keyboards import main_kb, line_kb, flowers_kb, recipes_kb, second_kb


@bot.callback_query_handler(func=lambda call: call.data == 'menu')
def menu(call):
    try:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Жми на кнопку! :)', reply_markup=line_kb())
    except telebot.apihelper.ApiTelegramException:
        pass


@bot.callback_query_handler(func=lambda call: call.data == 'help')
def helping(call):
    try:
        bot.edit_message_text(
                    chat_id=call.message.chat.id, message_id=call.message.message_id,
                    text=phrase.b_help, reply_markup=line_kb())
    except telebot.apihelper.ApiTelegramException:
        pass


@bot.callback_query_handler(func=lambda call: call.data == 'date')
def today(call):
    try:
        bot.edit_message_text(
                    chat_id=call.message.chat.id, message_id=call.message.message_id,
                    text=f'Сегодня {date.today}', reply_markup=main_kb())
    except telebot.apihelper.ApiTelegramException:
        pass


@bot.callback_query_handler(func=lambda call: call.data == 'weather')
def weather_td(call):
    try:
        bot.edit_message_text(
                    chat_id=call.message.chat.id, message_id=call.message.message_id,
                    text=weather.weather_smr, reply_markup=main_kb())
    except telebot.apihelper.ApiTelegramException:
        pass


@bot.callback_query_handler(func=lambda call: call.data == 'recipes')
def recipe_menu(call):
    try:
        bot.edit_message_text(
            chat_id=call.message.chat.id, message_id=call.message.message_id,
            text='Любимые рецепты', reply_markup=recipes_kb()
                            )
    except telebot.apihelper.ApiTelegramException:
        pass


@bot.callback_query_handler(func=lambda call: call.data == 'second')
def recipes(call):
    try:
        bot.edit_message_text(
            chat_id=call.message.chat.id, message_id=call.message.message_id,
            text='Чего хочется?', reply_markup=second_kb()
        )
    except telebot.apihelper.ApiTelegramException:
        pass


@bot.callback_query_handler(func=lambda call: call.data in recipe)
def recipes(call):
    try:
        for i in recipe:
            if call.data == i:
                bot.edit_message_text(
                    chat_id=call.message.chat.id, message_id=call.message.message_id,
                    text=recipe[i], parse_mode='HTML', reply_markup=recipes_kb()
                )
    except telebot.apihelper.ApiTelegramException:
        pass


@bot.callback_query_handler(func=lambda call: call.data == 'flowers')
def flowers_menu(call):
    try:
        bot.edit_message_text(
                    chat_id=call.message.chat.id, message_id=call.message.message_id,
                    text='Краткая информация по растениям', reply_markup=flowers_kb()
                )
    except telebot.apihelper.ApiTelegramException:
        pass


flower_callb = [
        'anturium', 'chlor', 'coffee',
        'dollar', 'eucharis', 'ficus',
        'carissa', 'krassula', 'calatea'
        'myrtle', 'pomegranate', 'spatifillum'
                    ]


@bot.callback_query_handler(func=lambda call: call.data in flower_callb)
def flowers_content(call):
    for i in flower_callb:
        if call.data == i:
            index = flower_callb.index(i)
            img = open(images[index], 'rb')
            bot.send_message(
                chat_id=call.message.chat.id,
                text=flower[index], parse_mode='HTML'
                                )
            bot.send_photo(chat_id=call.message.chat.id, photo=img)
    bot.send_message(
        chat_id=call.message.chat.id,
        text='Для возврата к главному меню.',
        reply_markup=main_kb()
                )
