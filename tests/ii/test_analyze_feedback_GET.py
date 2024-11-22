import requests

# URL API для анализа отзывов
url = "http://127.0.0.1:8000/api/ii/analyze_feedback/"

# Пример параметров для фильтрации (например, ID проекта или конкретный отзыв)
params = {
    "project_id": 123,  # Пример параметра для фильтрации по ID проекта
    "feedback_type": "positive"  # Пример фильтрации по типу отзыва (положительные/отрицательные)
}

# Отправка GET-запроса с параметрами
response = requests.get(url, params=params)

# Обработка ответа от сервера
if response.status_code == 200:
    print("Ответ:", response.json())
else:
    print(f"Ошибка: {response.status_code}, {response.text}")
