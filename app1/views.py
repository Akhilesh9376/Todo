from django.shortcuts import render,redirect
from .models import Task
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import NewUserForm
from django.contrib.auth import login
# from .models import Contact
from django.contrib.auth import authenticate



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

def Register(request):
    if request.method =='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Created For {username}!')
            return redirect('Home')
    else:
        form=NewUserForm()

    return render(request,'app1/Register.html',{'form':form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request,'app1/login.html',{'form':form})

def Contact(request):
    
    return render(request,'app1/Contact.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")
    return render(request,'App1/logout.html')
