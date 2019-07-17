from django.db.models import Q
from django.shortcuts import HttpResponse
from django.views import View


class BaseView(View):
    def post(self, request, *args, **kwargs):
        action = request.POST.get('action', '')
        if not hasattr(self, action):
            return HttpResponse('非法操作')
        ret = getattr(self, action)()
        if ret: return ret
        return self.get(request, *args, **kwargs)

    def search(self, field_list):
        """根据关键词，进行模糊查询"""
        query = self.request.GET.get('query', '')
        q = Q()
        q.connector = 'OR'
        for i in field_list:
            q.children.append(Q(('{}__contains'.format(i), query)))
        # (OR: (AND: ('qq__contains', '')), (AND: ('name__contains', '')), (AND: ('phone__contains', '')))
        return q
