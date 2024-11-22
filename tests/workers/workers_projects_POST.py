import requests

# URL для регистрации
url = "http://127.0.0.1:8000/api/workers/register/"

# Данные для отправки
data = {
    "username": "worker",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "password": "qwerty123",
    "group": "Строительные рабочие",  # Укажите правильное имя группы
}

# Выполняем POST-запрос
response = requests.post(url, json=data)

# Обработка ответа
if response.status_code == 201:
    print("Пользователь успешно зарегистрирован.")
    print("Ответ сервера:", response.json())
else:
    print(f"Ошибка регистрации: {response.status_code}")
    print("Детали ошибки:", response.json())
