import random
import json

"""SOS"""
b_help = 'Спешу на помощь!\nРассказываю подробно. ' \
         'Если ты хочешь вернуться в меню, то просто поприветсвуй меня :) ' \
         'Вот так /start или через /menu\nНиже ты увидишь кнопки. ' \
         'Просто тыкай и все!\nЕсли я глючу, то попробуй нажать на мою иконку в правом верхнем углу, ' \
         'там будет кнопка "остановить", нажми на неё, а потом ниже на "Перезапустить бота".' \
         ' А еще я очень не люблю, когда матерятся, поэтому давай НЕНАДА.'


"""Say 'Hello' to the bot"""
gr_dict = {
    '/start': 'Привет, дорогой друг! Меня зовут Кузька и я помощник по дому.'
    ' Для работы со мной нажми "Меню" ;)', 'привет': 'Привет, дорогой друг!'
    ' Меня зовут Кузька и я помощник по дому. Для работы со мной нажми "Меню")',
    'старт': 'Привет, дорогой друг! Меня зовут Кузька и я помощник по дому. Для работы со мной нажми "Меню" ;)',
    'hi': 'HI!!! ;)',
    'хай': 'Хай! Ай донт спик инглиш вери вел! Пуш "Меню" плиз. ))',
    'hello': 'Hello ;)', 'здарова': 'Даров!', 'добрый день': 'Добрый день, мой вежливый друг!'
    'Нажимай "Меню". ;)', 'здравствуй': 'Здравствуй, товарищ!', 'куку': 'Ку! Кин-дза-дза! Жми "Меню"!',
    'ghbdtn': 'Привет, привет. Поменяй раскладку! :D или нажми "Меню"',
    'я тебя люблю': 'Ой-ёй-ёёёй 😍\nА я тебя ЛЮБЛЮЮЮЮ!!\n💓', 'меню': 'Вот тебе меню!',
    'menu': 'На!))', '/menu': 'Жми кнопку! ;)'}

"""How is the bot doing today?"""
how_r_u = [
    'Да норм...', 'Бывало и получше...', 'Всегда хорошо!:) Спасибо, что интересуешься.',
    'Все клёво!', 'Хорошо, потому что ты пишешь!', 'Ну конечно хорошо!', 'Все супер!'
           ]
questions_hru = [
    'как дела?', 'как дела', 'как ты', 'как ты?'
            ]
hru_dict = {k: v for k, v in zip(questions_hru, random.sample(how_r_u, 4))}


"""What is the bot doing now?"""
questions_d = [
    'что делаешь', 'что делаешь?', 'чем занимаешься', 'чем занимаешься?'
            ]
wat_ru_d = [
    'Тебе стараюсь помочь!', 'Медитирую \U0001F60C', 'Радуюсь, что ты пишешь! \U0001F917',
    'Думаю, как бы повысить свой функционал...', 'Мечтаю о мире во всем мире \U0001F607'
]
wrd_dict = {k: v for k, v in zip(questions_d, random.sample(wat_ru_d, 5))}


"""Menu"""
menu_ph = ['меню', 'menu', '/menu']


"""control over swearing"""
exp_answ = [
    'Фу! Как некультурно! Я вообще-то воспитанный бот! :( Хватит учить меня плохому))\nЛучше тыкни на кнопочку /start.',
    'Может хватит? Жми /start!', 'Мама говорит, что ругаться плохо.', 'Фуфуфу!', 'Откуда ты знаешь такие слова??',
    'Да понял я, понял! У тебя богатый словарный запас!', 'Сделаю вид, что я этого не слышал.', '*Кузя закрыл глаза',
    'Ну почему ты ругаешься??', 'Выдохни и просто напиши /menu', 'Ляляля! А я ничего не слышуууу!', '\U0001F922'
    ]*4
cens_lst = json.load(open('censor.json'))
exp_str = ','.join(cens_lst)
exp_dict = {k: v for k, v in zip(cens_lst, random.sample(exp_answ, 42))}


def create_dict(*args):
    """creating a large dict of phrases from small dicts"""
    dict_phrases = {}
    for d in args:
        dict_phrases.update(d)
    return dict_phrases


grand_dictphr = create_dict(wrd_dict, hru_dict, gr_dict)

if __name__ == '__main__':

    create_dict(wrd_dict, hru_dict, gr_dict)
