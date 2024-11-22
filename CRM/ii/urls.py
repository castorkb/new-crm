from django.urls import path
from . import views

urlpatterns = [
    path('client/query/', views.client_query_view, name='client_query'),  # Обработка запросов от клиентов
    path('forecast_demand/', views.forecast_demand_view, name='forecast_demand'),  # Прогнозирование спроса
    path('analyze_client_behavior/', views.analyze_client_behavior_view, name='analyze_client_behavior'),  # Анализ клиентского поведения
    path('predict_project_delays/', views.predict_project_delays_view, name='predict_project_delays'),  # Прогнозирование задержек
    path('analyze_feedback/', views.analyze_feedback_view, name='analyze_feedback'),  # Анализ отзывов
    path('financial_analysis/', views.financial_analysis_view, name='financial_analysis'),  # Финансовый анализ
]







