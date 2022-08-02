import telebot
import sqlite3
from config import token
import random
import time
import datetime
import phrase
import date
import weather
from flowers import flower
from keyboards import main_kb, line_kb, flowers_kb

bot = telebot.TeleBot(token)

"""Keyboard's functions"""
main_kb()
line_kb()
flowers_kb()
""""""


@bot.message_handler(commands=['start'])
def greeting(message):
    """connect DB and create the table"""
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS login_id( 
                             id INT
                            )''')
    connect.commit()

    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM login_id WHERE id = {people_id};")
    data = cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", user_id)
        connect.commit()
    """answers after greeting phrase"""
    bot.send_message(message.chat.id, phrase.greeting_answ, reply_markup=main_kb())


def send_all():
    """sending mess to users """
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    users_id = []
    cursor.execute('SELECT * FROM login_id;')
    new_data = cursor.fetchall()
    connect.commit()
    for i in new_data:
        i = i[0]
        users_id.append(i)
    """number of users"""
    bot.send_message(users_id[0], f'Количество зарегистрированных пользователей - {len(users_id)}')
    """automatic sending of notifications"""
    while True:
        for user in users_id:
            bot.send_message(user, 'тест')
        time.sleep(10)


@bot.message_handler(commands=['delete'])
def delete(message):
    """delete id from table"""
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    people_id = message.chat.id
    cursor.execute(f"DELETE FROM login_id WHERE id = {people_id}")
    connect.commit()
    bot.send_message(message.chat.id, 'Данные успешно удалены.')


@bot.message_handler(content_types=['text'])
def talk(message):
    """talking with a bot"""
    r_mess = message.text.lower()
    if r_mess in phrase.phrase_data:
        b_ans = phrase.phrase_data[r_mess]
        bot.send_message(message.chat.id, b_ans)
    elif r_mess in phrase.menu_ph:
        b_ans = 'Вот и меню.)) Выбирай.'
        bot.send_message(message.chat.id, b_ans, reply_markup=main_kb())
    elif phrase.exp_str.find(r_mess[:3]) != -1:
        b_ans = random.choice(phrase.exp_answ)
        bot.send_message(message.chat.id, b_ans)
    else:
        b_ans = 'Я тебя не понял. :( Просто напиши /start или /menu'
        bot.send_message(message.chat.id, b_ans)


@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    if call.message:
        if call.data == 'menu':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Жми на кнопку! :)', reply_markup=line_kb())
        elif call.data == 'help':
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=phrase.b_help, reply_markup=line_kb())
        elif call.data == 'date':
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=f'Сегодня {date.today}')
        elif call.data == 'weather':
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=weather.weather_smr)
        elif call.data == 'flowers':
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text='Краткая информация по растениям', reply_markup=flowers_kb()
            )
        elif call.data == 'calatea':
            img = open('images\\medalion.jpg', 'rb')
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=flower[0], parse_mode='HTML'
                                )
            bot.send_photo(chat_id=call.message.chat.id, photo=img)
        elif call.data == 'carissa':
            img = open('images\\karissa.jpg', 'rb')
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=flower[1], parse_mode='HTML'
                                  )
            bot.send_photo(chat_id=call.message.chat.id, photo=img)
        elif call.data == 'eucharis':
            img = open('images\\eucharis.jpg', 'rb')
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=flower[2], parse_mode='HTML'
            )
            bot.send_photo(chat_id=call.message.chat.id, photo=img)
        elif call.data == 'chlor':
            img = open('images\\chlorofittum.jpg', 'rb')
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=flower[3], parse_mode='HTML'
            )
            bot.send_photo(chat_id=call.message.chat.id, photo=img)
        elif call.data == 'ficus':
            img = open('images\\ficus.jpg', 'rb')
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=flower[4], parse_mode='HTML'
            )
            bot.send_photo(chat_id=call.message.chat.id, photo=img)
        elif call.data == 'coffee':
            img = open('images\\coffee.jpg', 'rb')
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=flower[5], parse_mode='HTML'
            )
            bot.send_photo(chat_id=call.message.chat.id, photo=img)
        elif call.data == 'anturium':
            img = open('images\\anturium.jpg', 'rb')
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=flower[6], parse_mode='HTML'
            )
            bot.send_photo(chat_id=call.message.chat.id, photo=img)
        elif call.data == 'pomegranate':
            img = open('images\\pomegranate.jpeg', 'rb')
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text=flower[7], parse_mode='HTML'
            )
            bot.send_photo(chat_id=call.message.chat.id, photo=img)


if __name__ == '__main__':
    bot.infinity_polling()
