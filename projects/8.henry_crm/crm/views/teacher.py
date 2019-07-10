from django.shortcuts import render, redirect
from django.views import View

from crm import models
from crm.forms import ClasslistForm
from utils.pagenation import Pagenation


class ClassList(View):

    def get(self, request):
        all_item = models.ClassList.objects.filter(teachers=request.user_obj)
        obj = Pagenation(request, all_item.count(), per_page=3)
        return render(request, 'teacher/list_class.html',
                      {'all_item': all_item[obj.start:obj.end], 'all_page': obj.show})


def modify_class(request, pk=None):
    user_obj = models.ClassList.objects.filter(pk=pk).first()
    obj = ClasslistForm(instance=user_obj)
    if request.method == 'POST':
        obj = ClasslistForm(request.POST, instance=user_obj)
        if obj.is_valid():
            obj.save()
            url = request.GET.get('next', '')
            url = url if url else 'list_class'
            return redirect(url)
    title = '修改班级' if pk else '添加班级'
    return render(request, 'form.html', {'obj': obj, 'title': title})
