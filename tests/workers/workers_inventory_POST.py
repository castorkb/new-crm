import requests

url = "http://127.0.0.1:8000/api/workers/inventory/"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMjA5ODcxLCJpYXQiOjE3MzIxNzk4NzEsImp0aSI6ImYwNTcxMzk1OGEzNDQ0OTRhNWZhYjc4OTA0MWQyYWE3IiwidXNlcl9pZCI6MX0.lwRW6p7AWsBwSDOKUZO4YoQuLV8ROQMaYCIFwy0IEpo",
    "Content-Type": "application/json",
}

data = {
    "item_name": "Бетон",
    "stock_level": 50,
    "purchase_order": 12345
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("Запись успешно создана:", response.json())
else:
    print("Ошибка создания записи:", response.status_code, response.text)
