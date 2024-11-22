from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, CustomTokenObtainPairView
from .views import Interaction1ListCreateView, Interaction1DetailView
from .views import InteractionListCreateView, InteractionDetailView



urlpatterns = [
    path('register/', RegisterView.as_view(), name='client_register'),  # Регистрация
    path('login/', CustomTokenObtainPairView.as_view(), name='client_login'),  # Логин (получение JWT)
    path('token/refresh/', TokenRefreshView.as_view(), name='client_token_refresh'),  # Обновление JWT
    path('interactions/', Interaction1ListCreateView.as_view(), name='interaction-list-create'),
    path('interactions/<int:pk>/', Interaction1DetailView.as_view(), name='interaction-detail'),
    path('interactions/', InteractionListCreateView.as_view(), name='interaction-list-create'),
    path('interactions/<int:pk>/', InteractionDetailView.as_view(), name='interaction-detail'),

]



