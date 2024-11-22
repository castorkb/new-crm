# ai_integration.py
import openai
from django.conf import settings



def generate_gpt_response(prompt: str) -> str:
    """
    Функция для взаимодействия с GPT API и получения ответа.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # или другой подходящий движок
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Ошибка при запросе к GPT: {e}"
