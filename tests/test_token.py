import requests


# URL для получения токена
url = "http://127.0.0.1:8000/api/workers/api/token/"
data = {
    "username": "admin",
    "password": "admin"
    }

# Выполнение POST-запроса для получения токена
response = requests.post(url, json=data)

if response.status_code == 200:
    # Извлекаем токен доступа
    access = response.json().get('access')
    refresh = response.json().get('refresh')  # Если нужен refresh-токен

    if access:
        print('Логин успешен.')
        print(f"Access Token: {access}")
        print(f"Refresh Token: {refresh}")
    else:
        print("Ошибка: токен не найден в ответе.")
else:
    print('Ошибка при отправке запроса:', response.status_code, response.text)

url = "http://127.0.0.1:8000/api/workers/api/token/"
data = {
    "username": "admin",    
    "password": "admin"
}
response = requests.post(url, json=data)

if response.status_code == 200:    
    access = response.json().get('access')
    headers = {
        "Authorization": f"Bearer {access}"
    }    
    print('Логин успешен.')
else:
    print('Ошибка при отправке запроса:', response.status_code, response.text)

