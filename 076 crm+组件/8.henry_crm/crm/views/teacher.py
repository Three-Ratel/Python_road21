from django.forms import modelformset_factory
from django.shortcuts import render, redirect, reverse, HttpResponse

from crm import models
from crm.forms import ClasslistForm, CourseRecordForm, StudyRecordForm
from utils.pagenation import Pagenation
from .base import BaseView


class ClassList(BaseView):

	def get(self, request):
		# all_item = models.ClassList.objects.filter(teachers=request.user_obj)
		all_item = models.ClassList.objects.all()
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


class CourseRecord(BaseView):

	def get(self, request, class_id):
		all_item = models.CourseRecord.objects.filter(re_class_id=class_id)
		page = Pagenation(request, all_item.count(), request.GET.copy(), per_page=3)
		return render(request, 'teacher/list_course_record.html',
					  {'all_item': all_item[page.start:page.end], 'all_page': page.show, 'class_id': class_id})

	def multi_init(self):
		course_record_id = self.request.POST.get('edit_name')
		course_record_objs = models.CourseRecord.objects.filter(pk__in=course_record_id)
		for course_record in course_record_objs:
			stu_list = []
			for stu in course_record.re_class.customer_set.filter(status='studying'):
				# models.StudyRecord.objects.create(course_record_id=course_record_id, student=stu)
				# 批量插入
				stu_list.append(models.StudyRecord(course_record=course_record, student=stu))
			models.StudyRecord.objects.bulk_create(stu_list)


# return HttpResponse('添加成功')


def modify_course_record(request, pk=None, class_id=None):
	cr_obj = models.CourseRecord(re_class_id=class_id, recorder=request.user_obj) if class_id \
		else models.CourseRecord.objects.filter(pk=pk).first()
	obj = CourseRecordForm(instance=cr_obj)
	if request.method == 'POST':
		obj = CourseRecordForm(request.POST, instance=cr_obj)
		if obj.is_valid():
			obj.save()
			next = request.GET.get('next')
			if next:
				return redirect(next)
			else:
				return redirect(reverse('list_course_record', args=(class_id,)))
	title = '编辑课程记录' if pk else '新增课程记录'
	return render(request, 'form.html', {'obj': obj, 'title': title})


class StudyRecord(BaseView):
	ModelFormSet = modelformset_factory(models.StudyRecord, StudyRecordForm, extra=0)

	def get(self, request, pk=None):
		# ModelFormSet = modelformset_factory(models.StudyRecord, fields='__all__', extra=0)
		queryset = models.StudyRecord.objects.filter(course_record_id=pk)
		all_item = self.ModelFormSet(queryset=queryset)
		return render(request, 'teacher/list_study_record.html', {'all_item': all_item})

	def post(self, request, pk=None, *args, **kwargs):
		queryset = models.StudyRecord.objects.filter(course_record_id=pk)
		all_item = self.ModelFormSet(queryset=queryset, data=request.POST)
		if all_item.is_valid():
			all_item.save()
			return HttpResponse('保存成功')
		return render(request, 'teacher/list_study_record.html', {'all_item': all_item})


# def study_record_list(request, pk):
# 	ModelFormSet = modelformset_factory(models.StudyRecord, StudyRecordForm, extra=0)
# 	queryset = models.StudyRecord.objects.filter(course_record_id=pk)
# 	form_set_obj = ModelFormSet(queryset=queryset)
# 	if request.method == 'POST':
# 		form_set_obj = ModelFormSet(queryset=queryset, data=request.POST)
# 		if form_set_obj.is_valid():
# 			form_set_obj.save()
# 			return HttpResponse('保存成功')
#
# 	return render(request, 'teacher/list_study_record.html', {'all_item': form_set_obj})
