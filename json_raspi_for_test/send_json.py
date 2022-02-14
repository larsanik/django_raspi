import requests
import json
from datetime import datetime

# целевой URL-адрес
url = 'http://127.0.0.1:8000/meteodata/post_q/'
# данные в виде словаря

idstation=1
timemes=str(datetime.today())
temperature=-3.35
humidity=87.65
press=760.34
geocoord='38.161594892513094, 20.43207143133511'

param = {
    'ID station': idstation,
    'Date&time measurement': timemes,
    'Temperature': temperature,
    'Humidity': humidity,
    'Pressure': press,
    'Geocoord': geocoord
}
print(f'Словарь = {param}')

# кодируем словарь в формат JSON
json_param = json.dumps(param)

# отправка POST-запроса с данными в формате JSON
resp = requests.post(url, data=json_param)
print(f'Результат = {resp}')
