import telebot
from config import token
import schedule
import threading
import sqlite3
import time

bot = telebot.TeleBot(token)

import handlers
import callbacks


"""sending mess to users """
connect = sqlite3.connect('users.db')
cursor = connect.cursor()
cursor.execute('SELECT * FROM login_id;')
new_data = cursor.fetchall()
connect.commit()
users_id = []
for i in new_data:
    i = i[0]
    users_id.append(i)


def watering(lst):
    """reminder about watering"""
    for user in lst:
        bot.send_message(user, 'Не забудь полить Калатею!))')


def notifications(lst):
    """automatic sending of notifications"""
    schedule.every(4).day.do(watering, lst)
    while True:
        schedule.run_pending()
        time.sleep(1)


t1 = threading.Thread(target=bot.polling)
t2 = threading.Thread(target=notifications, args=(users_id,))
t1.start()
t2.start()
t1.join()
t2.join()
