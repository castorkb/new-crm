
import requests

# URL вашего API
url = "http://127.0.0.1:8000/api/client/interactions/"

# Пример авторизации (замените на реальные данные)
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMzEzOTQ2LCJpYXQiOjE3MzIyODM5NDYsImp0aSI6IjNkODgxOTIxY2RlYTQyMTlhZGJkNDhiZDEwZGI1NWU0IiwidXNlcl9pZCI6MX0.4noZ3orrcTfWlJB5aDRLB1TpHKx8CyvombO6KrwDz08'
}

def test_post():
    data = {
        'manager': 1,  # ID менеджера, например, 1
        'client': 2,  # ID клиента
        'type': 'call',  # Тип взаимодействия
        'details': 'Обсуждение деталей проекта',  # Описание взаимодействия
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Status code: {response.status_code}")
        if response.status_code == 201:
            print("POST запрос успешно выполнен. Ответ:")
            print(response.json())  # Печатает JSON-ответ от сервера
        else:
            print(f"Ошибка POST запроса. Ответ: {response.text}")
    except Exception as e:
        print(f"Ошибка запроса: {str(e)}")

if __name__ == "__main__":
    test_post()
