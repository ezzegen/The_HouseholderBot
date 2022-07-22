import requests
from bs4 import BeautifulSoup

response = requests.get('https://my-calend.ru/day-and-number-today')
soup = BeautifulSoup(response.text, 'html.parser')
split_lst = soup.get_text().split('Праздники сегодня')[0].split('Какое сегодня число и день недели ')
today = split_lst[-1]
