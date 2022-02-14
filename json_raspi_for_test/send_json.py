# -*- coding: utf-8 -*-
import requests
import json
from datetime import datetime
from input import sensorPolling

# целевой URL-адрес
url = 'http://larsanik.sknt.ru/meteodata/post_q/'
# данные в виде словаря
temperature_in, humidity_in, press_in = sensorPolling()
idstation=1
timemes = str(datetime.today())
temperature = temperature_in
humidity = humidity_in
press = press_in
geocoord='60.0277651653459, 30.213837357491467'

param = {
    'ID station': idstation,
    'Date&time measurement': timemes,
    'Temperature': temperature,
    'Humidity': humidity,
    'Pressure': press,
    'Geocoord': geocoord
}
# print(f'Словарь = {param}')

# кодируем словарь в формат JSON
json_param = json.dumps(param)

# отправка POST-запроса с данными в формате JSON
resp = requests.post(url, data=json_param)
# print(f'Результат = {resp}')
