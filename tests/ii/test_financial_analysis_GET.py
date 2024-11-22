import requests

# URL API с параметрами (например, для анализа по ID проекта)
url = "http://127.0.0.1:8000/api/ii/financial_analysis/"

# Параметры запроса (например, передаем ID проекта для получения финансового анализа)
params = {
    "project_id": 123  # Пример параметра для фильтрации по проекту
}

# Отправка GET-запроса с параметрами
response = requests.get(url, params=params)

# Обработка ответа от сервера
if response.status_code == 200:
    print("Ответ:", response.json())
else:
    print(f"Ошибка: {response.status_code}, {response.text}")
