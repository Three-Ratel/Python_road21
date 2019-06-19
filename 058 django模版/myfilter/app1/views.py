from django.shortcuts import render

# Create your views here.

hobby = ['movies', 'music', 'reading']


def filter_test(request):
    return render(request, 'filter_test.html',
                  {'a': 10,
                   'b': 2,
                   'string': 'Django',
                   'dic': [hobby, hobby, hobby],
                   })
