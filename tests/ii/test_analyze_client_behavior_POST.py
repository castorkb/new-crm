import requests
import json

# URL API
url = "http://127.0.0.1:8000/api/ii/analyze_client_behavior/"

# Пример данных, которые могут быть отправлены в запросе
data = {
    "client_data": {
        "age": 30,
        "location": "Бишкек",
        "purchase_history": [
            {"item": "Product A", "price": 100, "date": "2024-10-01"},
            {"item": "Product B", "price": 50, "date": "2024-10-10"}
        ],
        "interaction_history": [
            {"type": "email", "date": "2024-10-15", "outcome": "positive"},
            {"type": "call", "date": "2024-10-16", "outcome": "negative"}
        ]
    }
}

# Заголовки, указывающие на тип контента JSON
headers = {
    "Content-Type": "application/json"
}

# Отправка POST-запроса с данными
response = requests.post(url, data=json.dumps(data), headers=headers)

# Обработка ответа от сервера
if response.status_code == 200:
    print("Ответ:", response.json())
else:
    print(f"Ошибка: {response.status_code}, {response.text}")
