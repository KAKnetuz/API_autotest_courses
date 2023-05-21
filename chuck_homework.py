import requests

"""базовый URL для запроса шутки по категории"""
base_url = "https://api.chucknorris.io/jokes/random?category="
# получаем список доступных категорий
categories = requests.get("https://api.chucknorris.io/jokes/categories").json()

"""Цикл для получения по одной шутке из каждой категории"""
for category in categories:
    url = base_url + category  # формируем URL для запроса шутки для текущей категории
    response = requests.get(url)  # получаем ответ на запрос

    if response.status_code == 200:  # проверяем статус код ответа
        joke = response.json()["value"]  # если статус код 200 - получаем значение шутки из ответа
        print(f"{category.capitalize()}: {joke}. Статус код: {response.status_code}")  # выводим шутку и статус код
    else:
        # если статус код не 200, выводим сообщение об ошибке
        print(f"Ошибка получения шутки для {category}. Статус код: {response.status_code}")
