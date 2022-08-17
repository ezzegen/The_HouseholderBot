import telebot
from config import token
import threading
import time
import logging

bot = telebot.TeleBot(token)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
import handlers
import callbacks
from notifications import notifications, users_id

while True:
    try:
        t1 = threading.Thread(target=bot.polling(non_stop=True))
        t2 = threading.Thread(target=notifications, args=(users_id,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    except Exception as e:
        logger.error(e)
        time.sleep(15)
