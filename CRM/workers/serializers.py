from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task, Project, Inventory, Resource, Financial

import re

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Поле для пароля пользователя
    group = serializers.CharField(write_only=True)  # Поле для группы

    class Meta:
        model = User  # Модель User, с которой работает сериализатор
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'group']  # Используемые поля
        ref_name = 'ClientRegisterSerializer'

    def validate_username(self, value):
        """Проверка уникальности имени пользователя."""
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Пользователь с таким именем уже существует.")
        return value

    def validate_group(self, value):
        """Проверка существования группы."""
        if not Group.objects.filter(name=value).exists():
            raise serializers.ValidationError("Этой группы не существует.")
        return value

    def validate_email(self, value):
        """Проверка уникальности email, если он указан."""
        if value and User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует.")
        return value

    def validate_password(self, value):
        """Валидация пароля."""
        # Проверка минимальной длины пароля
        if len(value) < 8:
            raise serializers.ValidationError("Пароль должен содержать минимум 8 символов.")

        # Проверка на наличие хотя бы одной цифры и одной буквы
        if not re.search(r'[A-Za-z]', value):
            raise serializers.ValidationError("Пароль должен содержать хотя бы одну букву.")
        if not re.search(r'\d', value):
            raise serializers.ValidationError("Пароль должен содержать хотя бы одну цифру.")

        return value

    def create(self, validated_data):
        # Создание нового пользователя
        group_name = validated_data.pop('group')  # Извлекаем и удаляем группу из данных
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
        )

        # Добавляем пользователя в группу
        group = Group.objects.get(name=group_name)






# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True) # Поле для пароля пользователя
#     group = serializers.CharField(write_only=True) # Поле для группы
#
#     class Meta:
#         model = User # Модель User, с которой работает сериализатор
#         fields = ['username', 'first_name', 'last_name', 'email', 'password', 'group'] # Перечисление полей, которые будут использоваться в сериализаторе
#
#     def create(self, validated_data):
#         # Создание нового пользователя с привязкой к группе
#
#         user = (User.objects.create_user(
#             username=validated_data['username'], # Добавляем поле
#             first_name=validated_data['first_name'], # Добавляем поле
#             last_name=validated_data['last_name'], # Добавляем поле
#             password=validated_data['password'], # Добавляем поле
#             email=validated_data.get('email', ''), # Добавляем поле
#             ))
#         group_name = validated_data['group'] # Получение группы по имени
#         try:
#             group = Group.objects.get(name=group_name) # Проверка наличия группы. Если группы нет, выкидывает ошибку.
#
#         except Group.DoesNotExist:
#             raise serializers.ValidationError({"group": "Этой группы не существует."})
#
#         user.groups.add(group)
#         user.save()
#
#         return user



class ProjectSerializer(serializers.ModelSerializer):
    status = serializers.CharField(default='Ожидает начала') # Поле для статуса проекта. Значение по умолчанию - 'Ожидает начала'
    manager = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True) # Поле для связи с менеджером проекта. Оно является обязательным
    team = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, required=False) # Поле для связи с командой проекта, позволяющее выбрать несколько пользователей
    client = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True) # Поле для связи с клиентом проекта

    class Meta:
        model = Project  # Указывает, что сериализатор связан с моделью Project
        fields = ['id', 'title', 'description', 'deadline', 'status', 'manager', 'team', 'client'] # Перечисление полей, которые будут использоваться в сериализаторе


    def update(self, instance, validated_data):
        team_data = validated_data.pop('team', None)
        if team_data:
            instance.team.set(team_data)  # Обновление команды
        return super().update(instance, validated_data)


class TaskSerializer(serializers.ModelSerializer):
    # Отображаем имя пользователя, к которому присвоена задача
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ['task_name', 'title', 'description', 'status', 'assigned_to', 'project']








class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['item_name', 'stock_level', 'purchase_order']

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'item_name', 'stock_Level', 'purchase_order']






class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name', 'type', 'quantity', 'availability', 'usage_history']





class FinancialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financial
        fields = ['id', 'budget', 'expenses', 'invoices', 'payments', 'taxes']








