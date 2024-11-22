import requests

url = "http://127.0.0.1:8000/api/workers/resources/"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMjA5ODcxLCJpYXQiOjE3MzIxNzk4NzEsImp0aSI6ImYwNTcxMzk1OGEzNDQ0OTRhNWZhYjc4OTA0MWQyYWE3IiwidXNlcl9pZCI6MX0.lwRW6p7AWsBwSDOKUZO4YoQuLV8ROQMaYCIFwy0IEpo",
    "Content-Type": "application/json",
}
data = {
    "name": "Кран",                  # Название ресурса
    "type": "Оборудование",         # Тип ресурса
    "quantity": "5 штук",           # Количество в виде строки
    "availability": "В наличии",    # Доступность как строка
    "usage_history": "Использован на проекте X",  # История использования
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("Ресурс успешно создан:", response.json())
else:
    print("Ошибка:", response.status_code, response.text)

