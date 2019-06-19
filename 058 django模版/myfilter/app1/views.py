from django.shortcuts import render


# Create your views here.

def filter_test(request):
    return render(request, 'filter_test.html',
                  {'a': 10,
                   'b': 2,
                   'string': 'Django',
                   'dic': [1, 2, 3],
                   })
