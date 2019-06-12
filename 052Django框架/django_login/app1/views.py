from django.shortcuts import render, redirect

from app1 import models


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        res = models.Info.objects.filter(username=username, pwd=pwd)
        if res:
            # return redirect('https://www.baidu.com')
            return redirect('/index/')

    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')
