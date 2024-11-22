import requests

# URL вашего API
url = "http://127.0.0.1:8000/api/client/interactions/"

# Пример авторизации (замените на реальные данные)
headers = {
    'Authorization': 'Bearer YOUR_JWT_TOKEN'
}

def test_get():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("GET запрос успешно выполнен. Ответ:")
        print(response.json())  # Печатает JSON-ответ от сервера
    else:
        print(f"Ошибка GET запроса. Код статуса: {response.status_code}")
