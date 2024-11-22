
from rest_framework import serializers
from .models import GPTService

class GPTServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPTService
        fields = ['id', 'query', 'response', 'created_at']


# serializers.py
from rest_framework import serializers
from .models import Prompt

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['id', 'text', 'category']


