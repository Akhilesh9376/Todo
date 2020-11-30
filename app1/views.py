from django.shortcuts import render,redirect
from .models import Task
from .forms import *
# Create your views here.
def Home(request):
    tasks =Task.objects.all()
    form=TaskForm()
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Home')
    context={'tasks':tasks,'form':form ,}
    return render(request,'app1/Home.html',context)


def UpdateTask(request ,pk):
    task=Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'app1/Update.html',context)

def delete(request,pk):
    item =Task.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('/')
    context ={'item':item}
    return render(request,'app1/delete.html',context)