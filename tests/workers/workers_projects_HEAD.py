import requests

url = "http://127.0.0.1:8000/api/workers/projects/"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMTcwNTAwLCJpYXQiOjE3MzIxNDA1MDAsImp0aSI6IjMxMDEzZTU5ZDQyMzRlM2RiYWNmNGMxZTk0M2QyZWM5IiwidXNlcl9pZCI6MX0.dzb3T2ZKjd0c7tbU5ilSaBnboZS6cCO_0whXfHfyjJA"
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.head(url, headers=headers)

if response.status_code == 200:
    print("Заголовки ответа:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")
else:
    print("Ошибка:", response.status_code, response.text)
