import requests

url = "http://127.0.0.1:8000/api/workers/financial/"
token = "your_jwt_access_token_here"
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Список финансовых записей:", response.json())
else:
    print("Ошибка:", response.status_code, response.text)
