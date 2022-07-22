import telebot
import sqlite3
from config import token
import phrase
import random
import date
import weather

bot = telebot.TeleBot(token)


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
    keyboard.add(button_help, button_date, button_weather)
    return keyboard


@bot.message_handler(content_types=['text'])
def greeting(message):
    r_mess = message.text.lower()

    if r_mess in phrase.greeting_phrase:
        b_answ = phrase.greeting_answ
        bot.send_message(message.chat.id, b_answ, reply_markup=main_kb())
    elif r_mess == 'ghbdtn':
        b_ans = 'Привет, привет. Поменяй раскладку! :D или нажми /start'
        bot.send_message(message.chat.id, b_ans)
    elif r_mess in phrase.menu_ph:
        b_answ = 'Вот и меню.)) Выбирай.'
        bot.send_message(message.chat.id, b_answ, reply_markup=main_kb())
    elif r_mess in phrase.questions_hru:
        b_ans = random.choice(phrase.how_r_u)
        bot.send_message(message.chat.id, b_ans)
    elif r_mess in phrase.questions_d:
        b_ans = random.choice(phrase.wat_ru_d)
        bot.send_message(message.chat.id, b_ans)
    elif r_mess in phrase.expletives or phrase.expletives_str.find(r_mess[:3]) != -1:
        b_ans = random.choice(phrase.exp_answ)
        bot.send_message(message.chat.id, b_ans)
    else:
        b_ans = 'Я тебя не понял. :( Просто напиши /start или /menu'
        bot.send_message(message.chat.id, b_ans)


@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    ans = ''
    if call.message:
        if call.data == 'menu':
            ans = 'Жми на кнопку! :)'
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=ans, reply_markup=line_kb())
        elif call.data == 'help':
            ans = phrase.b_help
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=ans, reply_markup=line_kb())
        elif call.data == 'date':
            ans = f'Сегодня {date.today}'
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=ans)
        elif call.data == 'weather':
            ans = weather.weather_smr
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=ans)


if __name__ == '__main__':
    bot.infinity_polling()
