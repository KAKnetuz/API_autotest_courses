import requests

# Создание новой локации
base_url = "https://rahulshettyacademy.com"
endpoint = "/maps/api/place/add/json"
params = {
    "key": "qaclick123"
}

# создание файла и заполнение place_id
with open("place_ids.txt", "w") as f:
    for i in range(5):
        payload = {
            "location": {
                "lat": "-33.8669710",
                "lng": "151.1958750"
            },
            "accuracy": "50",
            "name": "Google Shoes",
            "phone_number": "(02) 9374 4000",
            "address": "48 Pirrama Road, Pyrmont, NSW 2009, Australia",
            "types": ["shoe_store"],
            "website": "http://www.google.com.au/",
            "language": "en-AU"
        }
        response = requests.post(base_url + endpoint, params=params, json=payload)
        place_id = response.json()["place_id"]
        f.write(place_id + "\n")
        print(f"Создана новая локация c place_id: {place_id}")
        assert response.status_code == 200
        print("Статус ответа верен")

# 1. Удаление 2-го и 4-го place_id
with open("place_ids.txt", "r") as f:
    lines = f.readlines()
    del lines[1::2]  # удаляем каждый второй элемент (2-й и 4-й)

with open("place_ids.txt", "w") as f:
    f.writelines(lines)
    print("2-й и 4-й place_id удалены!")

# 2. Отбор на существующие и несуществующие локации
existing_place_ids = []
non_existing_place_ids = []

with open("place_ids.txt", "r") as f:
    for line in f:
        place_id = line.strip()
        endpoint = "/maps/api/place/get/json"
        params = {
            "key": "qaclick123",
            "place_id": place_id
        }
        response = requests.get(base_url + endpoint, params=params)
        print(f"Проверка локации с place_id: {place_id}")
        if response.status_code == 200:
            existing_place_ids.append(place_id)
            print("Локация существует!")
        else:
            non_existing_place_ids.append(place_id)
            print("Локация не найдена!")
        print(response.json())

print("Список существующих локаций:", existing_place_ids)
print("Список несуществующих локаций:", non_existing_place_ids)

# 3. Создание нового файла с 3-мя существующими локациями
with open("new_place_ids.txt", "w") as f:
    for place_id in existing_place_ids[:3]:
        f.write(place_id + "\n")
        print(f"Добавлен place_id: {place_id} в новый файл")

# 4. Проверка файла с новыми place_id
with open("new_place_ids.txt", "r") as f:
    for line in f:
        place_id = line.strip()
        endpoint = "/maps/api/place/get/json"
        params = {
            "key": "qaclick123",
            "place_id": place_id
        }
        response = requests.get(base_url + endpoint, params=params)
        print(f"Проверка новой локации с place_id: {place_id}")
        print(response.json())
        assert response.status_code == 200
        if response.status_code == 200:
            print("Успешно!!! Статус код верный!")
        else:
            print("Провал! Запрос ошибочный!")