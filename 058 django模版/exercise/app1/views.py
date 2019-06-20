from django.shortcuts import render
from django.views import View


# Create your views here.
def index(request):
    li = [1, 2, 3, 4, 5]
    li2 = [1, 2, 3, 4, 5]
    # if request.method == 'POST':
    #     data = request.FILES.get('file')
    #     print(data)
    #     with open(data.name, 'wb') as f:
    #         for i in data.chunks():
    #             f.write(i)
    #             print(data.chunks)
    # print(request.get_host())
    # print(request.get_full_path())
    # print(request.is_ajax())
    # print(request.is_secure())
    # print(request.get_raw_uri())
    return render(request, 'index.html', {'li': li, 'li2': li2, 'li3': []})




