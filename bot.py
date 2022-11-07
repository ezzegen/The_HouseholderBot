import telebot
import threading
import time
import logging
import sqlite3

bot = telebot.TeleBot('5448428966:AAENRJbG09ug3GZOJJRM3dtvtcv_BhaAAV0')

import handlers
import callbacks
from notifications import notifications, users_id

while True:
    try:
        logging.basicConfig(level=logging.INFO)
        t1 = threading.Thread(target=bot.polling(non_stop=True))
        t2 = threading.Thread(target=notifications, args=(users_id,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    except Exception:
        time.sleep(15)
