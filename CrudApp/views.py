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

def delete(request,pk):
    data=Task.objects.get(pk=pk)
    data.delete()
    data = Task.objects.all() 
    return render(request, 'task.html',{'datas':data})

def edit(request,pk):
    edited_data=Task.objects.get(pk=pk)
    if request.method == 'POST':
       data=TaskForm(request.POST,instance=edited_data)
       if data.is_valid():
          data.save()
          return redirect('home')  

    else:
        data = TaskForm(instance=edited_data)


    return render(request, 'Home.html',{'frm':data})
  


def about(request):
    return render(request, 'about.html')
