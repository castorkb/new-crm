
# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ai_integration import (
    handle_client_query,
    forecast_demand,
    analyze_client_behavior,
    predict_project_delays,
    analyze_client_feedback,
    financial_analysis_and_optimization
)

@csrf_exempt
def client_query_view(request):
    """
    Взаимодействие с клиентом через чат-бота. Обрабатываем запрос клиента и возвращаем ответ.
    """
    client_query = request.GET.get('query', '')
    project_data = {"project_id": 123, "status": "in_progress"}  # Пример данных проекта
    response = handle_client_query(client_query, project_data)
    return JsonResponse({'response': response})

@csrf_exempt
def forecast_demand_view(request):
    """
    Прогнозирование спроса на ресурсы.
    """
    historical_data = request.POST.get('data', {})  # Данные о прошлых проектах
    response = forecast_demand(historical_data)
    return JsonResponse({'forecast': response})

@csrf_exempt
def analyze_client_behavior_view(request):
    """
    Анализ клиентского поведения.
    """
    client_data = request.POST.get('client_data', {})  # Данные о клиенте
    response = analyze_client_behavior(client_data)
    return JsonResponse({'analysis': response})

@csrf_exempt
def predict_project_delays_view(request):
    """
    Прогнозирование задержек по проекту.
    """
    project_data = request.POST.get('project_data', {})  # Данные о проекте
    response = predict_project_delays(project_data)
    return JsonResponse({'prediction': response})

@csrf_exempt
def analyze_feedback_view(request):
    """
    Анализ отзывов клиентов.
    """
    feedback_data = request.POST.get('feedback', [])  # Отзывы клиентов
    response = analyze_client_feedback(feedback_data)
    return JsonResponse({'analysis': response})

@csrf_exempt
def financial_analysis_view(request):
    """
    Финансовый анализ и рекомендации по оптимизации бюджета.
    """
    project_finances = request.POST.get('project_finances', {})  # Финансовые данные проекта
    response = financial_analysis_and_optimization(project_finances)
    return JsonResponse({'financial_analysis': response})





