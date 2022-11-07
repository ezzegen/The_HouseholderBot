from bot import bot as bot
import sqlite3
import schedule
import time
from keyboards import flowers_kb


def users_lst():
    """extracting id from table"""
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute('SELECT login_id FROM users;')
    new_data = cursor.fetchall()
    connect.commit()
    user_id = []
    for i in new_data:
        i = i[0]
        user_id.append(i)
    return user_id


users_id = users_lst()


def watering_1(lst):
    """reminder about watering"""
    for user in lst:
        bot.send_message(user, 'Не забудь полить Калатею, Хлорофиттумы и Кофе!))',
                         reply_markup=flowers_kb())


def watering_2(lst):
    for user in lst:
        bot.send_message(user, 'Не забудь полить Фикус, Кариссу, Гранат, Мирт!))',
                         reply_markup=flowers_kb())


def watering_3(lst):
    for user in lst:
        bot.send_message(user, 'Не забудь полить Эухарис, Антуриум!'
                               ' И проверь, нуждаются ли в поливе Крассула, Долларовое дерево!))',
                         reply_markup=flowers_kb())


def watering_4(lst):
    for user in lst:
        bot.send_message(user, 'Не забыла про Долларовое дерево и Крассулу? Полей,'
                               'если 4 дня назад не поливала!))))',
                         reply_markup=flowers_kb())


def notifications(lst):
    """automatic sending of notifications"""
    schedule.every(4).day.at('15:00').do(watering_1, lst)
    schedule.every(6).day.at('15:00').do(watering_2, lst)
    schedule.every(10).day.at('15:00').do(watering_3, lst)
    schedule.every(14).day.at('15:00').do(watering_4, lst)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    print(users_id)
