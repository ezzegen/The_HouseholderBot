import requests
from bs4 import BeautifulSoup


def date(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    split_lst = soup.get_text().split('Праздники сегодня')[0].split('Какое сегодня число и день недели ')
    return split_lst[-1]


today = date('https://my-calend.ru/day-and-number-today')

if __name__ == '__main__':
    date('https://my-calend.ru/day-and-number-today')
