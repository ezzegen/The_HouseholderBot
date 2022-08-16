from main import bot as bot
import phrase
import date
import weather
from flowers import flower, images
from recipes import recipe
from keyboards import line_kb, flowers_kb, recipes_kb, second_kb


@bot.callback_query_handler(func=lambda call: call.data == 'menu')
def menu(call):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text='Жми на кнопку! :)', reply_markup=line_kb())


@bot.callback_query_handler(func=lambda call: call.data == 'help')
def helping(call):
    bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=phrase.b_help, reply_markup=line_kb())


@bot.callback_query_handler(func=lambda call: call.data == 'date')
def today(call):
    bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=f'Сегодня {date.today}')


@bot.callback_query_handler(func=lambda call: call.data == 'weather')
def weather_td(call):
    bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=weather.weather_smr)


@bot.callback_query_handler(func=lambda call: call.data == 'recipes')
def recipe_menu(call):
    bot.edit_message_text(
        chat_id=call.message.chat.id, message_id=call.message.message_id,
        text='Любимые рецепты', reply_markup=recipes_kb()
                        )


recipe_callb = ['first', 'dessert', 'drink', 'snacks']


@bot.callback_query_handler(func=lambda call: call.data in recipe_callb)
def recipes(call):
    bot.edit_message_text(
        chat_id=call.message.chat.id, message_id=call.message.message_id,
        text=recipe, parse_mode='HTML'
    )


@bot.callback_query_handler(func=lambda call: call.data == 'second')
def recipes(call):
    bot.edit_message_text(
        chat_id=call.message.chat.id, message_id=call.message.message_id,
        text='Чего хочется?', reply_markup=second_kb()
    )


@bot.callback_query_handler(func=lambda call: call.data in recipe)
def recipes(call):
    for i in recipe:
        if call.data == i:
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=recipe[i], parse_mode='HTML'
            )


@bot.callback_query_handler(func=lambda call: call.data == 'flowers')
def flowers_menu(call):
    bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text='Краткая информация по растениям', reply_markup=flowers_kb()
            )


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
        text='Для возврата к главному меню кликни /menu.'
                )
