from django.contrib import admin
from .models import Interaction,Client,Type
admin.site.register(Interaction)
admin.site.register(Client)
admin.site.register(Type)