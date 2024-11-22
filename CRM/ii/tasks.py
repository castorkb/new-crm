# tasks.py
from .ai_integration import predict_project_delays

def automate_task_assignment(project_data):
    """
    Автоматическое назначение задач и прогнозирование задержек с использованием ИИ.
    """
    delay_predictions = predict_project_delays(project_data)
    # Логика для автоматической настройки задач и ресурсов с учетом прогнозов.
