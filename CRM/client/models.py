from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=250)  # Имя клиента
    client_email = models.EmailField(max_length=250)  # Электронная почта клиента
    client_phonenamber = models.CharField(max_length=20)  # Номер телефона клиента

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    additional_field = models.CharField(max_length=100)






class Interaction(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager_interactions')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_interactions')
    type = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return f"{self.type} with {self.client.username} by {self.manager.username} on {self.date}"


