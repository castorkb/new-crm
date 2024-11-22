import requests

url = "http://127.0.0.1:8000/api/workers/financial/"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMTk5ODg4LCJpYXQiOjE3MzIxNjk4ODgsImp0aSI6IjNjOTZhNjMyYWFmZDQ5ZmRiZmJhNTA2ZDQwNWZjNmU4IiwidXNlcl9pZCI6MX0.TMptxz7e2YM7DLp_9uFovpExFJingQXe5M6u-E1zhRg",  # Укажите ваш токен
    "Content-Type": "application/json",
}
data = {
    "budget": 50000,
    "expenses": 20000,
    "invoices": 5,
    "payments": 4,
    "taxes": 1000,
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("Успешно создано:", response.json())
else:
    print("Ошибка:", response.status_code, response.text)
