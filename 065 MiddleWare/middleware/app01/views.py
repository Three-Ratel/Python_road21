from django.shortcuts import render
from django.template.response import TemplateResponse


# Create your views here.

def index(request):
    print('here is index')
    # return render(request, 'index.html')
    return TemplateResponse(request, 'index.html', {'name': 'herny', 'age': 19})
