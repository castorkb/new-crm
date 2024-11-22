import requests

# URL для эндпоинта регистрации
url = "http://127.0.0.1:8000/api/workers/register/"

# Данные для нового пользователя
data = {
    "username": "worker1",
    "first_name": "Иван",
    "last_name": "Иванов",
    "email": "ivan.ivanov@example.com",
    "password": "password123",
    "group": "manager"
}

# Отправка POST запроса
response = requests.post(url, json=data)

# Проверка ответа
if response.status_code == 201:
    print("Пользователь успешно зарегистрирован:", response.json())
else:
    print("Не удалось зарегистрировать пользователя. Код статуса:", response.status_code)
    print("Ответ:", response.text)

