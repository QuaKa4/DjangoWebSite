from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about-us'),
    path('create-task', views.create_task, name='create-task'),
    path('settings', views.settings, name='settings'),
]
