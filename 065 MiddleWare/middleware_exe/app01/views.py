from django.shortcuts import render


# Create your views here.

def test(request):
    print('welcome to our site!')
    return render(request, 'test.html')
