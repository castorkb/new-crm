import requests

# URL API для прогноза спроса
url = "http://127.0.0.1:8000/api/ii/forecast_demand/"

# Пример параметров для прогноза спроса (например, категория товара и период)
params = {
    "category": "construction_materials",  # Пример категории для прогноза
    "start_date": "2024-01-01",  # Пример начала периода для прогноза
    "end_date": "2024-12-31"  # Пример окончания периода для прогноза
}

# Отправка GET-запроса с параметрами
response = requests.get(url, params=params)

# Обработка ответа от сервера
if response.status_code == 200:
    print("Ответ:", response.json())
else:
    print(f"Ошибка: {response.status_code}, {response.text}")
