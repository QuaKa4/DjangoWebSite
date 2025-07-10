from .models import TaskManager
from django.forms import ModelForm, TextInput, Textarea

class TaskManagerForm(ModelForm):
    class Meta:
        model = TaskManager
        fields = ["title", 'task']
        widgets = {'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'введите название'}),
            'task': Textarea(attrs={'class': 'form-control', 'placeholder': 'введите табутаск'})}
