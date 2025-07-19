from django.contrib import admin
from .models import TaskManager, MessageManager

admin.site.register(TaskManager)
admin.site.register(MessageManager)
# Register your models here.
