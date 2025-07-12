from dbm import error

from django.shortcuts import render, redirect
from django.template.defaultfilters import title

from .forms import TaskManagerForm
from .models import TaskManager
from django.http import HttpResponse


def index(request):
    tasks = TaskManager.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': "главная стр", 'tasks': tasks})

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

def settings(request):
    return render(request, 'main/settings.html', {'title': 'настройки'})
