import requests
from bs4 import BeautifulSoup
import time


def date(url, retry=5):
    """
    Date and day of the week now
    :param: url(str), retry(int)
    :return: str
    """
    try:
        response = requests.get(url)
    except Exception:
        time.sleep(3)
        if retry:
            return date(url, retry=retry-1)
        else:
            return 'Сервис временно недоступен, но можно глянуть в календарь на телефоне)).'
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        split_lst = soup.get_text().split('Праздники сегодня')[0].split('Какое сегодня число и день недели ')
        return split_lst[-1]


today = date('https://my-calend.ru/day-and-number-today')

if __name__ == '__main__':
    date('https://my-calend.ru/day-and-number-today')
