import requests

url = 'http://127.0.0.1:8000/api/ii/client/query/'

# Пример запроса
query = "Каков текущий статус строительного проекта?"

# Данные для отправки (например, строка запроса в теле запроса)
data = {
    'query': query
}

# Отправляем POST-запрос
response = requests.post(url, data=data)

if response.status_code == 200:
    print("Response from GPT:", response.json()['response'])
else:
    print(f"Request failed with status code {response.status_code}")
    print("Error details:", response.text)
