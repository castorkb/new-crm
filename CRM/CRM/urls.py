"""
URL configuration for CRM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.urls import path
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Документация к API вашего проекта",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
        ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    )


def home(request):
    return HttpResponse("Добро пожаловать на главную страницу CRM!")


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),  # Админка
    path('api/client/', include('client.urls')),  # Подключаем маршруты приложения client
    path('api/workers/', include('workers.urls')),  # Подключаем маршруты приложения workers
    path('api/ii/', include('ii.urls')),  # Подключаем маршруты приложения ii
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger- ui'),
    # Альтернативный интерфейс документации Redoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Для дополнительной поддержки DRF
    ]
