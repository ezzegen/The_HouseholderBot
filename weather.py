import requests

response = requests.get('https://world-weather.ru/pogoda/russia/samara/')
content = response.text
pars = content.split('<span class="dw-into">')[1].split('<span id="open-desc-weather">')[0]
weather_pars = pars.split()
join_lst = ' '.join(weather_pars)
if 'Облачно' or 'Ясно' in weather_pars:
    weather_smr = f'{join_lst}\n\nОтличная погода для пробежки или, может, для прогулки... Хотя лучше на дачу!\U0001F493'
else:
    weather_smr = f'{join_lst}\n\nХммм... А я думаю, почему меня в сон клонит...'
