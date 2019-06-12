from django.shortcuts import render, redirect
from app1 import models


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        ret = models.User.objects.filter(username=username, password=pwd)
        if ret: return redirect('/index/')

    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')
