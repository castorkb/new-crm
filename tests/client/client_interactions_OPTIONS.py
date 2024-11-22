import requests

# URL вашего API
url = "http://127.0.0.1:8000/api/client/interactions/"

# Пример авторизации (замените на реальные данные)
headers = {
    'Authorization': 'Bearer YOUR_JWT_TOKEN'
}

def test_options():
    response = requests.options(url, headers=headers)
    if response.status_code == 200:
        print("OPTIONS запрос успешно выполнен.")
        print("Поддерживаемые методы:", response.headers.get('allow'))  # Печатает методы, поддерживаемые сервером
    else:
        print(f"Ошибка OPTIONS запроса. Код статуса: {response.status_code}")
