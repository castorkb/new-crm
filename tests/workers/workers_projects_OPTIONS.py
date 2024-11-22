import requests

url = "http://127.0.0.1:8000/api/workers/projects/"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMTcwMzE2LCJpYXQiOjE3MzIxNDAzMTYsImp0aSI6IjdhYzM3MGY5MzhiMTQ3YWZiZjkzZjBiNjI1ODgwZWYxIiwidXNlcl9pZCI6MX0.TQWfH0ndMLghnRmUtKt6LfO5AFxBd4yo12nRX1_YbZQ"  
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.options(url, headers=headers)

if response.status_code == 200:
    print("Поддерживаемые методы:", response.headers.get("Allow"))
else:
    print("Ошибка:", response.status_code, response.text)
