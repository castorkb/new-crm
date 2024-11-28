import openai


openai.api_key =''


def generate_gpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        return response['choices'][0]['message']['content']
    except openai.error.AuthenticationError:
        return "Ошибка аутентификации. Проверьте ваш API-ключ."
    except openai.error.OpenAIError as e:
        return f"Ошибка API: {str(e)}"

# Пример вызова функции
prompt = "What is the current status of the construction project?"
response = generate_gpt_response(prompt)
print(response)


def forecast_demand(data: dict) -> str:
    """
    Прогнозирование спроса на ресурсы (материалы, оборудование) на основе исторических данных.
    """
    prompt = f"Проанализируйте исторические данные по проектам: {data}. На основе этого, предложите прогноз по спросу на ресурсы и материалы для будущих проектов."
    return generate_gpt_response(prompt)



def analyze_client_behavior(client_data: dict) -> str:
    """
    Анализ клиентского поведения на основе данных о предыдущих заказах.
    """
    prompt = f"Проанализируйте поведение клиента на основе данных: {client_data}. На основе этого предложите, какие проекты или услуги могут его заинтересовать."
    return generate_gpt_response(prompt)



def handle_client_query(query: str, project_data: dict) -> str:
    """
    Обработка запросов клиентов и предоставление контекстуальных ответов.
    """
    prompt = f"Клиент спрашивает: '{query}'. Используя данные о проекте {project_data}, предоставьте точный и полезный ответ."
    return generate_gpt_response(prompt)



def predict_project_delays(project_data: dict) -> str:
    """
    Прогнозирование задержек в проекте и рекомендации по их предотвращению.
    """
    prompt = f"Проанализируйте данные по проекту {project_data} и предсказаниям задержек. Предложите рекомендации по их предотвращению."
    return generate_gpt_response(prompt)



def analyze_client_feedback(feedback: list) -> str:
    """
    Анализ отзывов клиентов для улучшения качества обслуживания.
    """
    prompt = f"Анализируйте отзывы клиентов: {feedback}. Выделите ключевые проблемы и предложите улучшения для сервиса."
    return generate_gpt_response(prompt)



def financial_analysis_and_optimization(project_finances: dict) -> str:
    """
    Анализ финансов проекта и рекомендации по оптимизации бюджета.
    """
    prompt = f"Проанализируйте финансы проекта: {project_finances}. Предложите способы оптимизации бюджета и сокращения затрат."
    return generate_gpt_response(prompt)


