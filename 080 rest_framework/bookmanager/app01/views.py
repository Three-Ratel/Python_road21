from rest_framework.response import Response
from rest_framework.views import APIView

from app01 import models


class BookListView(APIView):

	def get(self, request, *args, **kwargs):
		all_book = models.Book.objects.all().values('title', 'price', 'pub_date', 'authors', 'pub')
		return Response(all_book)
