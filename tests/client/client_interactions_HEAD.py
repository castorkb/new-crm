import requests

# URL вашего API
url = "http://127.0.0.1:8000/api/client/interactions/"

# Пример авторизации (замените на реальные данные)
headers = {
    'Authorization': 'Bearer YOUR_JWT_TOKEN'
}

def test_head():
    response = requests.head(url, headers=headers)
    if response.status_code == 200:
        print("HEAD запрос успешно выполнен.")
        print("Заголовки ответа:", response.headers)  # Печатает заголовки ответа
    else:
        print(f"Ошибка HEAD запроса. Код статуса: {response.status_code}")
