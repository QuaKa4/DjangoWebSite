from .models import TaskManager, MessageManager
from django.forms import ModelForm, TextInput, Textarea, DateInput, TimeInput


class TaskManagerForm(ModelForm):
    class Meta:
        model = TaskManager
        fields = ["title", 'task']
        widgets = {'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'введите название'}),
            'task': Textarea(attrs={'class': 'form-control', 'placeholder': 'введите табутаск'})}

class MessageManagerForm(ModelForm):
    class Meta:
        model = MessageManager
        fields = ['user', 'message', 'date', 'time']
        widgets = {'user': TextInput(attrs={'class': 'form-control', 'placeholder': 'пользователь'}),
                   'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'сообщение'}),
                   'date': DateInput(attrs={'class': 'form-control', 'placeholder': 'дата'}),
                   'time': TimeInput(attrs={'class': 'form-control', 'placeholder': 'время'})}