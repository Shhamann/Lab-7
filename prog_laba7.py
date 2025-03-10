import requests
import json
from holidayapi import holidayapi

def task1():
    city_name = "Tokio"
    key = "3c8f16824a7d5ddcfe1165eece60ca76"
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}")
    result = json.loads(response.text)
    temperature = f"{float(result['main']['temp'])- 273.15} °C"
    humidity = f"{result['main']['humidity']} %"
    pressure = f"{result['main']['pressure']} гПа"
    print(f'Погода в Токио:\nТемпература: {temperature}\nВлажность: {humidity}\nДавление: {pressure}\n')

def task2(): 
    while True:
        country = input('Введите страну в формате ISO 3166-1 alpha-2 или ISO 3166-1 alpha-3\nДля выхода введите "стоп"\n')
        if country == 'стоп': break
        try:
            key = 'f71fb38c-5901-4c97-b710-01884129b472'
            hapi = holidayapi.v1(key)
            holidays = hapi.holidays({
                'country': country,
                'year': '2024',
                'language': 'RU'
            })
            for holi in holidays['holidays']:
                date = holi['date'].split('-')
                months = ['января','февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
                print(f'Название: {holi['name']}\nДата: {date[2]} {months[int(date[1]) - 1]}\n')
        except:
            print('Неверный ввод')

if __name__ == '__main__':
    task1()
    task2()
