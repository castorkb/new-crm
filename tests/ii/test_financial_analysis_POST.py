import requests
import json

# URL API
url = "http://127.0.0.1:8000/api/ii/financial_analysis/"

# Пример финансовых данных для анализа
data = {
    "project_id": 123,
    "project_name": "Строительство жилого комплекса",
    "budget": 5000000,  # Бюджет проекта
    "expenses": 3500000,  # Расходы по проекту
    "revenues": 4500000,  # Доходы от проекта
    "taxes": 500000  # Налоги по проекту
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
