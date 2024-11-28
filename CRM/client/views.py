from functools import reduce

from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, InteractionSerializer, TypeSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets

from .models import Interaction, Type
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q






class RegisterView(generics.CreateAPIView):  # Представление для регистрации
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class CustomTokenObtainPairView(TokenObtainPairView):  # Представление для получения JWT-токенов
    permission_classes = (AllowAny,)





class InteractionListCreateView(generics.ListCreateAPIView):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer

    # Optional: Filter queryset based on query params (e.g., by manager, client, type)
    def get_queryset(self):
        queryset = Interaction.objects.all()
        manager = self.request.query_params.get('manager')
        client = self.request.query_params.get('client')
        type = self.request.query_params.get('type')

        if manager:
            queryset = queryset.filter(manager__username__icontains=manager)
        if client:
            queryset = queryset.filter(client__username__icontains=client)
        if type:
            queryset = queryset.filter(type__type_name__icontains=type)

        return queryset

# View for interaction detail (update, delete, or view specific interaction)
class InteractionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer

class TypeDetailView(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer





