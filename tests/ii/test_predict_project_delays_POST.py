import requests
import json

# URL API
url = "http://127.0.0.1:8000/api/ii/predict_project_delays/"

# Пример данных, которые могут быть отправлены в запросе
data = {
    "project_data": {
        "project_id": 123,
        "project_name": "Строительство жилого комплекса",
        "expected_completion_date": "2025-12-31",
        "current_status": "в процессе",
        "progress_percentage": 45,
        "delays": [
            {"cause": "недавние погодные условия", "duration_days": 5},
            {"cause": "поставка материалов", "duration_days": 10}
        ],
        "resources": {
            "available_workers": 50,
            "needed_workers": 60,
            "equipment_availability": "ограничено"
        }
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
