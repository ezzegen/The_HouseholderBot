import telebot
from config import token
import threading

bot = telebot.TeleBot(token)

import handlers
import callbacks
from notifications import notifications, users_id

t1 = threading.Thread(target=bot.polling)
t2 = threading.Thread(target=notifications, args=(users_id,))
t1.start()
t2.start()
t1.join()
t2.join()
