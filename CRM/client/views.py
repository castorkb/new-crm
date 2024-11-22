from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from .serializers import Interaction1Serializer
from .models import Interaction
from rest_framework.permissions import IsAuthenticated





class RegisterView(generics.CreateAPIView):  # Представление для регистрации
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class CustomTokenObtainPairView(TokenObtainPairView):  # Представление для получения JWT-токенов
    permission_classes = (AllowAny,)



class Interaction1ListCreateView(generics.ListCreateAPIView):
    queryset = Interaction.objects.all()
    serializer_class = Interaction1Serializer


class InteractionListCreateView(generics.ListCreateAPIView):
    queryset = Interaction.objects.all()
    serializer_class = Interaction1Serializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Interaction.objects.filter(manager=self.request.user)

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)

class Interaction1DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interaction.objects.all()
    serializer_class = Interaction1Serializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Interaction.objects.filter(client=self.request.user)

class InteractionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interaction.objects.all()
    serializer_class = Interaction1Serializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Interaction.objects.filter(client=self.request.user)
