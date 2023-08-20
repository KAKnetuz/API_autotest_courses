import requests

# Отправляем GET запрос к API
response = requests.get("https://swapi.dev/api/people/4/")
data = response.json()

# Извлекаем имена персонажей, которые снимались в фильмах с Дарт Вейдером
darth_vader_films = data.get("films", [])
characters = set()

for film_url in darth_vader_films:
    film_data = requests.get(film_url).json()
    for character_url in film_data.get("characters", []):
        character_data = requests.get(character_url).json()
        character_name = character_data.get("name")
        if character_name:
            characters.add(character_name)

# Сохраняем имена в текстовый файл без повторов
with open("characters.txt", "w", encoding="utf-8") as file:
    for character in characters:
        file.write(character + "\n")

# Выводим сообщение о завершении
print("Имена персонажей сохранены в файл 'characters.txt'")
