import requests

url = "http://127.0.0.1:8000/api/workers/tasks/"
headers = {
    "Authorization": "Bearer   Epo",
}

response = requests.options(url, headers=headers)

print("HTTP статус:", response.status_code)
print("Методы, поддерживаемые этим ресурсом:", response.headers.get('Allow'))
