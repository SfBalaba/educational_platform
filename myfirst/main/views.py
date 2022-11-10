from django.shortcuts import render, redirect
from .models import Task
from .forms import FormTask


def index(request):
    articles = Task.objects.order_by('-id')
    return render(request, 'main/index.html',
                  {'title': "Образовательная платфома", "articles": articles})


def about(request):
    return render(request, 'main/about.html')

def lib(request):
    return render(request, 'main/lib.html')

def blog(request):
    return render(request, 'main/blog.html')

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