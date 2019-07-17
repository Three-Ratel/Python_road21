from django.conf import settings
from django.db import transaction
from django.shortcuts import render, redirect, reverse, HttpResponse

from crm import models
from crm.forms import CustomerForm, ConsultRecordForm, EnrollmentForm
from utils.pagenation import Pagenation
from .base import BaseView


class CustomerList(BaseView):

    def get(self, request):
        q = self.search(['qq', 'name', 'phone'])
        if request.path == reverse('customer'):
            all_item = models.Customer.objects.filter(q, consultant__isnull=True)
        else:
            all_item = models.Customer.objects.filter(q, consultant=request.user_obj)
        obj = Pagenation(request, all_item.count(), request.GET.copy(), 3)
        return render(request, 'consultant/list_customer.html',
                      {'all_item': all_item[obj.start:obj.end], 'all_page': obj.show})

    def ctp(self):
        """common to public: 公户转私户"""
        li = self.request.POST.getlist('edit_name')
        num = models.Customer.objects.filter(consultant=self.request.user_obj).count()

        if num + len(li) > settings.MAX_CUSTOMER_NUM:
            return HttpResponse('做人不要太贪哦。。。')
        try:
            with transaction.atomic():
                queryset = models.Customer.objects.filter(pk__in=li, consultant=None).select_for_update()
                if len(li) == queryset.count():
                    queryset.update(consultant=self.request.user_obj)
                else:
                    return HttpResponse('客户以被占用。。。')
        except Exception as e:
            print(e)

    def ptc(self):
        """public to common: 私户转公户"""
        li = self.request.POST.getlist('edit_name')
        models.Customer.objects.filter(pk__in=li).update(consultant='')


def modify_customer(request, pk=None):
    user_obj = models.Customer.objects.filter(pk=pk).first()
    obj = CustomerForm(instance=user_obj)
    if request.method == 'POST':
        obj = CustomerForm(data=request.POST, instance=user_obj)
        if obj.is_valid():
            obj.save()
            url = request.GET.get('next', '')
            url = url if url else 'list_customer'
            return redirect(url)
    title = '修改客户' if pk else '新增客户'
    return render(request, 'form.html', {'obj': obj, 'title': title})


# 跟进记录
class ConsultRecordList(BaseView):

    def get(self, request, pk=0):
        all_item = models.ConsultRecord.objects.filter(consultant=request.user_obj)
        if pk:
            all_item = models.ConsultRecord.objects.filter(consultant=request.user_obj, customer_id=pk)
        obj = Pagenation(request, all_item.count(), per_page=3)
        return render(request, 'consultant/list_consult.html',
                      {'all_item': all_item[obj.start:obj.end], 'all_page': obj.show, 'customer_id': pk})


# 通过实例化，进行参数的间接传递
def modify_consult(request, pk=None, customer_id=None):
    user_obj = models.ConsultRecord(consultant=request.user_obj, customer_id=customer_id) if customer_id \
        else models.ConsultRecord.objects.filter(pk=pk).first()
    obj = ConsultRecordForm(instance=user_obj)
    if request.method == 'POST':
        obj = ConsultRecordForm(data=request.POST, instance=user_obj)
        if obj.is_valid():
            obj.save()
            url = request.GET.get('next', '')
            return redirect(url if url else 'consult_record')
    title = '修改记录' if pk else '新增记录'
    return render(request, 'form.html', {'obj': obj, 'title': title, })


class EnrollmentList(BaseView):

    def get(self, request, customer_id=None):
        if not customer_id:
            all_item = models.Enrollment.objects.filter(customer__in=request.user_obj.customers.all())
        else:
            all_item = models.Enrollment.objects.filter(customer_id=customer_id)
        obj = Pagenation(request, all_item.count(), per_page=2)
        return render(request, 'consultant/list_enrollment.html',
                      {'all_item': all_item[obj.start:obj.end], 'all_page': obj.show, 'customer_id': customer_id})


def modify_enrollment(request, pk=None, customer_id=None):
    user_obj = models.Enrollment(customer_id=customer_id) if customer_id \
        else models.Enrollment.objects.filter(customer_id=pk).first()
    obj = EnrollmentForm(instance=user_obj)
    if request.method == 'POST':
        obj = EnrollmentForm(data=request.POST, instance=user_obj)
        if obj.is_valid():
            obj.save()
            url = request.GET.get('next', '')
            return redirect(url if url else 'list_enrollment')
    title = '修改报名表' if pk else '添加报名表'
    return render(request, 'form.html', {'obj': obj, 'title': title, })
