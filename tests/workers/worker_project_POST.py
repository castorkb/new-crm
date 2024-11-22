import requests

# URL для эндпоинта проектов
url = "http://127.0.0.1:8000/api/workers/projects/"

# Данные для создания нового проекта с обязательными полями
data = {
    "title": "Новый проект",
    "description": "Описание нового проекта",
    "deadline": "2024-12-31",  # Дата в формате YYYY-MM-DD
    "status": "В процессе",
    "manager": 21,
    "client": 2,
}


headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMjk1NDgwLCJpYXQiOjE3MzIyODgyODAsImp0aSI6IjZkM2UzNjE0NDUwYjQ4ZmZhN2MzYWZjYzhiNGU2OTE3IiwidXNlcl9pZCI6MX0.hGyiQRDS2eRG01g_gXPfY_M0eBhxm1vBp2SagbUwmf4"
}

# Отправка POST запроса
response = requests.post(url, json=data, headers=headers)

# Проверка ответа
if response.status_code == 201:
    print("Проект успешно создан:", response.json())
else:
    print("Не удалось создать проект. Код статуса:", response.status_code)
    print("Ответ:", response.text)

