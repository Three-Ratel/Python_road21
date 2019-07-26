from rest_framework.views import APIView

from app01 import models

from rest_framework.response import Response
from app01.serializer import BookSerializer


class BookListView(APIView):
	book_obj = {}

	def get(self, request, pk=None, *args, **kwargs):
		if not pk:
			all_book = models.Book.objects.all()
		else:
			all_book = models.Book.objects.filter(pk=pk)
			self.book_obj['obj'] = all_book.first()

		ser_obj = BookSerializer(all_book, many=True)
		# print(ser_obj.data, type(ser_obj.data))
		return Response(ser_obj.data)

	def post(self, request, *args, **kwargs):
		# print(request.data)
		ser_obj = BookSerializer(data=request.data)
		if ser_obj.is_valid():
			ser_obj.save()
			return Response(ser_obj.data)
		return Response(ser_obj.errors)

	def put(self, request, pk, *args, **kwargs):
		obj = self.book_obj.get('obj')
		if not obj:
			return Response('更新数据不存在')

		ser_obj = BookSerializer(instance=obj, data=request.data, partial=True)
		if ser_obj.is_valid():
			ser_obj.save()
			return Response(ser_obj.data)
		return Response(ser_obj.errors)

	def delete(self, requset, pk, *args, **kwargs):
		obj = models.Book.objects.filter(pk=pk)
		if obj:
			obj.delete()
			return Response('删除成功')
		return Response('删除的数据不存在')


"""JsonResponse"""
# from django.http.response import JsonResponse
# class BookListView(APIView):
#
# 	def get(self, request, *args, **kwargs):
# 		all_book = models.Book.objects.all().values('id', 'title', 'pub__name', 'authors')
# 		# ser_obj = serializers.serialize('json', all_book)
# 		# return HttpResponse(ser_obj)
# 		return JsonResponse(data=list(all_book), json_dumps_params={'ensure_ascii': False}, safe=False)


"""django的序列化器"""
# from django.http.response import HttpResponse
# from django.core import serializers
#
#
# class BookListView(APIView):
# 	def get(self, request, *args, **kwargs):
# 		all_book = models.Book.objects.all()
# 		ser_obj = serializers.serialize('json', all_book, ensure_ascii=False)
# 		return HttpResponse(ser_obj)
