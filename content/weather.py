import requests
from bs4 import BeautifulSoup
import time


def weather(url, retry=5):
    """
    Find out the weather in Samara
    :param: url(str), retry(int)
    :return: str
    """
    try:
        response = requests.get(url)
    except Exception:
        time.sleep(3)
        if retry:
            return weather(url, retry=retry-1)
        else:
            return 'Сервис временно недоступен'
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        find_weather = soup.find_all('span', class_="dw-into")
        clear_weather = [c.text for c in find_weather][0].split('погода')[1].split('Подробнее')[0]
        if 'Облачно' or 'Ясно' in clear_weather:
            return f'{clear_weather}\n\nОтличная погода для пробежки или,' \
                      f' может, для прогулки... Хотя лучше на дачу!\U0001F493'
        else:
            return f'{clear_weather}\n\nХммм... А я думаю,' \
                      f' почему меня в сон клонит...'


weather_smr = weather('https://world-weather.ru/pogoda/russia/samara/')

if __name__ == 'main':
    print(weather_smr)
