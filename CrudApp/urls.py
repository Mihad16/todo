from django.urls import path
from . import views


urlpatterns = [
    path('',views.Todo, name='home'),
    path('about/',views.about, name='about'),
    path('task/',views.task, name='task'),
    path('delete/ <int:pk>',views.delete, name='delete'),
    
     
    
]