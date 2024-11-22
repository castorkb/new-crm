from django.db import models

class GPTService(models.Model):
    query = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query: {self.query[:50]}... | Response: {self.response[:50]}..."






class Prompt(models.Model):
    text = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)  # Категория (например, Строительство, Клиенты)

    def __str__(self):
        return self.text[:50]  # Для отображения первых 50 символов текста





