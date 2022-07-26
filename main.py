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


@bot.message_handler(commands=['sendall'])
def send_all(message):
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
    for user in users_id:
        bot.send_message(user, 'тест')
    """number of users"""
    bot.send_message(message.chat.id, f'Количество пользователей бота: {len(users_id)}.')


@bot.message_handler(commands=['delete'])
def delete(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    people_id = message.chat.id
    """delete id from table"""
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
        b_answ = 'Вот и меню.)) Выбирай.'
        bot.send_message(message.chat.id, b_answ, reply_markup=main_kb())
    elif phrase.exp_str.find(r_mess[:3]) != -1:
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
