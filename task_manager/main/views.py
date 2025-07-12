from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from pyexpat.errors import messages

from .forms import TaskManagerForm, MessageManagerForm
from .models import TaskManager, MessageManager


def index(request):
    tasks = TaskManager.objects.all()
    return render(request, 'main/index.html', {'title': "главная страница", 'tasks': tasks})

def about(request):
    return render(request, 'main/about_us.html')

def create_task(request):
    error = ''
    if request.method == "POST":
        form = TaskManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'form invalid'
    form = TaskManagerForm
    context = {'form': form,
               'error': error}
    return render(request, 'main/create_task.html', context)

def chat(request):
    messages = MessageManager.objects.all()
    return render(request, 'main/chat.html', {'title': "Сообщения", 'messages': messages})

def write_message(request):
    error = ''
    if request.method == "POST":
        form = MessageManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat')
        else:
            error = "form is invlid"
    form = MessageManagerForm
    context = {'form': form,
               'error' :error}
    return render(request, 'main/write_message.html', context)
