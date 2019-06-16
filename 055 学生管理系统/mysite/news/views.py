from django.shortcuts import HttpResponse

from news.models import Reporter, Article


def my_test(request):
    re = Reporter.objects.all()
    print(re, type(re))
    return HttpResponse(' ok')
