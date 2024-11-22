import requests
import json

# URL API
url = "http://127.0.0.1:8000/api/ii/analyze_feedback/"

# Пример данных обратной связи
data = {
    "feedback": {
        "client_id": 101,
        "client_name": "Иван Иванов",
        "project_id": 123,
        "feedback_text": "Проект задерживается, поставки материалов не успевают по срокам.",
        "rating": 3,
        "suggestions": "Увеличить количество поставок и ускорить процессы."
    }
}

# Заголовки, указывающие на тип контента JSON
headers = {
    "Content-Type": "application/json"
}

# Отправка POST-запроса с данными
response = requests.post(url, data=json.dumps(data), headers=headers)

# Обработка ответа от сервера
if response.status_code == 200:
    print("Ответ:", response.json())
else:
    print(f"Ошибка: {response.status_code}, {response.text}")
