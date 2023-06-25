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

# Отправка метода get к созданным локациям
with open("place_ids.txt", "r") as f:
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
