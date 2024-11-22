import requests

# URL для эндпоинта регистрации
url = "http://127.0.0.1:8000/api/workers/register/"

# Отправка OPTIONS запроса
response = requests.options(url)

# Проверка ответа
if response.status_code == 200:
    print("Разрешенные методы:", response.headers.get('allow'))
else:
    print("Не удалось получить разрешенные методы. Код статуса:", response.status_code)
