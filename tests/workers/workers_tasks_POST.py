import requests

url = "http://127.0.0.1:8000/api/workers/tasks/"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMjk1MjM0LCJpYXQiOjE3MzIyODgwMzQsImp0aSI6ImI2YjhjNTY3MjBiNzQ1MGQ4M2U3ZDc3MGMyZTA1YzY3IiwidXNlcl9pZCI6MX0.1ITKhGsBdcqqY-oVFMMmOm56R8dpS8qvh9QpISwpm5c",
    "Content-Type": "application/json",
}

data = {
    "task_name": "Установить оборудование",
    "title": "Установка строительного крана",
    "description": "Установить строительный кран на строительной площадке.",
    "status": "в процессе",
    "assigned_to": 21,  # ID работника или группы, к которой назначена задача
    "project": 1  # ID проекта, к которому привязана задача (например, проект с ID = 1)
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("Задача успешно создана:", response.json())
else:
    print("Ошибка:", response.status_code, response.text)

