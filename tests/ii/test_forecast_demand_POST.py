import requests
import json

# URL вашего API
url = "http://127.0.0.1:8000/api/ii/forecast_demand/"

# Данные, которые вы хотите отправить в запросе (пример)
data = {
    "data": "Некоторые исторические данные проекта"
}

# Заголовки, указывающие на тип данных в формате JSON
headers = {
    "Content-Type": "application/json"
}

# Отправка POST запроса с данными
response = requests.post(url, data=json.dumps(data), headers=headers)

# Выводим ответ от сервера
if response.status_code == 200:
    print("Ответ:", response.json())
else:
    print(f"Ошибка: {response.status_code}, {response.text}")
