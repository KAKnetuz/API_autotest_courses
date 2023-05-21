import requests

category = input("Введите категорию: ")  # запрашиваем у пользователя категорию

"""Отправляем запрос для получения всех категорий"""

# отправляем запрос для получения списка категорий
response = requests.get("https://api.chucknorris.io/jokes/categories")

categories = response.json()  # получаем список категорий из ответа

"""Проверяем, что данная категория есть в списке категорий"""

if category not in categories:
    print(f"Категория {category} не найдена. Доступные категории: {', '.join(categories)}")
else:
    # формируем URL для получения шутки по заданной категории
    url = f"https://api.chucknorris.io/jokes/random?category={category}"
    response = requests.get(url)  # отправляем запрос для получения шутки

    if response.status_code == 200:
        joke = response.json()["value"]
        print(f"{category.capitalize()}: {joke}. Статус код: {response.status_code}")
    else:
        # выводим полученную шутку и статус код ответа
        print(f"Ошибка получения шутки для {category}. Статус код: {response.status_code}")
