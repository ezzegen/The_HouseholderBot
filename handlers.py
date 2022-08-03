from main import bot as bot
import sqlite3
import random
from keyboards import main_kb
import phrase


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
    bot.send_message(message.chat.id, phrase.gr_dict['/start'], reply_markup=main_kb())


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
def menu(message):
    """talking with a bot"""
    r_mess = message.text.lower()
    if r_mess in phrase.gr_dict:
        b_answ = phrase.gr_dict[r_mess]
        bot.send_message(message.chat.id, b_answ, reply_markup=main_kb())
    elif r_mess in phrase.phrase_data:
        b_answ = phrase.phrase_data[r_mess]
        bot.send_message(message.chat.id, b_answ)
    elif phrase.exp_str.find(r_mess[:3]) != -1:
        b_answ = random.choice(phrase.exp_answ)
        bot.send_message(message.chat.id, b_answ)
    else:
        b_answ = 'Я тебя не понял. :( Просто напиши /start или /menu'
        bot.send_message(message.chat.id, b_answ)
