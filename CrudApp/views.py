from django.shortcuts import render, redirect
from . models import Task
from .forms import TaskForm
# Create your views here.
def Todo(request):
    frm=TaskForm()
    if request.method == 'POST':
        tsk=TaskForm(request.POST)
       
        tsk.is_valid()
        tsk.save()
    return render(request, 'Home.html',{'frm':frm})

def task(request):
    data=Task.objects.all()
    return render(request, 'task.html',{'datas':data})
  





def about(request):
    return render(request, 'about.html')
