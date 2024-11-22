import requests

# URL для регистрации
url = "http://127.0.0.1:8000/api/client/register/"

# Данные для регистрации пользователя
data = {
    "username": "client312",         # Имя пользователя
    "first_name": "First",         # Имя
    "last_name": "Last",           # Фамилия
    "email": "newuser616@example.com", # Электронная почта
    "password": "Qwerty123",  # Пароль
    "confirm_password": "Qwerty123" # Подтверждение пароля
}

# Выполнение POST запроса
response = requests.post(url, data=data)

# Проверка статуса ответа
if response.status_code == 201:
    print("Пользователь успешно зарегистрирован!")
else:
    print(f"Ошибка регистрации: {response.status_code}")
    print(response.json())  # Вывод ошибки в формате JSON
