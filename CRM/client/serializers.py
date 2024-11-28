from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Interaction
import re


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)  # Поле подтверждения пароля

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        ref_name = 'WorkerRegisterSerializer'

    def validate(self, attrs):
        # Получаем пароли
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        # Проверка на совпадение паролей
        if password != confirm_password:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})

        # Проверка на минимальную длину пароля
        if len(password) < 8:
            raise serializers.ValidationError({"password": "Пароль должен быть не менее 8 символов."})

        # Проверка на наличие хотя бы одной буквы и одной цифры
        if not re.search(r'[A-Za-z]', password):
            raise serializers.ValidationError({"password": "Пароль должен содержать хотя бы одну букву."})
        if not re.search(r'\d', password):
            raise serializers.ValidationError({"password": "Пароль должен содержать хотя бы одну цифру."})

        return attrs

    def create(self, validated_data):
        # Удаляем confirm_password, так как это поле не сохраняется
        validated_data.pop('confirm_password', None)

        # Проверяем, существует ли пользователь с таким же email или username
        if User.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError({"username": "Пользователь с таким именем уже существует."})
        if User.objects.filter(email=validated_data.get('email', '')).exists():
            raise serializers.ValidationError({"email": "Пользователь с таким email уже существует."})

        # Создаем пользователя
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
        )

        # Создаем профиль, если его нет
        Profile.objects.get_or_create(user=user)

        # Добавляем пользователя в группу "Клиенты"
        group, _ = Group.objects.get_or_create(name="Клиенты")
        user.groups.add(group)

        return user


from rest_framework import serializers
from .models import Interaction,Type

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class InteractionSerializer(serializers.ModelSerializer):
    type = TypeSerializer(read_only=True)

    class Meta:
        model = Interaction
        fields = ['id', 'manager', 'client', 'type', 'date', 'details']