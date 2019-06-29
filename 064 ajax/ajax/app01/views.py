from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


def upload(request):
    if request.method == 'POST':
        data = request.FILES.get('file')
        print(data, type(data), '*' * 8, data.name, type(data.name))
        with open(data.name, mode='wb') as f:
            for i in data.chunks():
                f.write(i)
        return HttpResponse('ok')

    return render(request, 'upload.html')


def sum(request):
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = int(a) + int(b)
        print(request.POST)
        return HttpResponse(c)
    return render(request, 'sum.html')


import json


def test(request):
    ret = request.POST.get('hobby')
    ret = json.loads(ret)
    print(request.POST)
    print(ret)
    # return HttpResponse('ok')
    return redirect('/test_ajax_href/')


def test_ajax_href(request):
    return render(request, 'test_ajax_href.html')
