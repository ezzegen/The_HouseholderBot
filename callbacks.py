from main import bot as bot
import phrase
import date
import weather
from flowers import flower, images
from keyboards import line_kb, flowers_kb, recipes_kb


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


recipe_callb = ['first', 'second', 'dessert', 'drink', 'snacks']


@bot.callback_query_handler(func=lambda call: call.data in recipe_callb)
def recipes(call):
    bot.edit_message_text(
        chat_id=call.message.chat.id, message_id=call.message.message_id,
        text='рецепт'
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
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=flower[index], parse_mode='HTML'
                                )
            bot.send_photo(chat_id=call.message.chat.id, photo=img)
    bot.send_message(
        chat_id=call.message.chat.id,
        text='Смотрим далее. Для возврата к главному меню кликни /menu.', reply_markup=flowers_kb()
                )
