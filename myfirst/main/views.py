from django.shortcuts import render, redirect
from .models import Task
from .forms import FormTask


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def lib(request):
    articles = Task.objects.order_by('-id')
    return render(request, 'main/lib.html',
                  {'title': "Образовательная платфома", "articles": articles})


def blog(request):
    return render(request, 'main/blog.html')

def register(request):
    return render(request, 'main/register.html')

def home(request):
    return render(request, 'main/home.html')

def password_reset_form(request):
    return render(request, 'main/password_reset_form.html')

def login(request):
    return render(request, 'main/login.html')

def help(request):
    return render(request, 'main/help.html')

def training(request):
    return render(request, 'main/training.html')

def create(request):
    error = ""
    if(request.method == "POST"):
        form = FormTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Данные некорректны"
    form = FormTask()
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'main/create.html', context)