import requests

url = "http://127.0.0.1:8000/api/workers/resources/"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMjA5ODcxLCJpYXQiOjE3MzIxNzk4NzEsImp0aSI6ImYwNTcxMzk1OGEzNDQ0OTRhNWZhYjc4OTA0MWQyYWE3IiwidXNlcl9pZCI6MX0.lwRW6p7AWsBwSDOKUZO4YoQuLV8ROQMaYCIFwy0IEpo",  # Укажите ваш токен
}

response = requests.head(url, headers=headers)

if response.status_code == 200:
    print("Заголовки ответа:", response.headers)
else:
    print("Ошибка:", response.status_code)