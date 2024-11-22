import requests

# URL API для предсказания задержек по проекту
url = "http://127.0.0.1:8000/api/ii/predict_project_delays/"

# Пример параметров для предсказания задержек (например, ID проекта)
params = {
    "project_id": 123,  # Пример параметра для предсказания задержек по ID проекта
    "deadline": "2024-12-31"  # Пример дополнительного параметра - дата завершения проекта
}

# Отправка GET-запроса с параметрами
response = requests.get(url, params=params)

# Обработка ответа от сервера
if response.status_code == 200:
    print("Ответ:", response.json())
else:
    print(f"Ошибка: {response.status_code}, {response.text}")
