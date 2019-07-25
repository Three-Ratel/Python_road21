from rest_framework import serializers
from app01 import models

class PublisherSerializer(serializers.Serializer):
	name = serializers.CharField()


class AuthorSerializer(serializers.Serializer):
	name = serializers.CharField()


class BookSerializer(serializers.Serializer):
	id = serializers.IntegerField(required=False)
	title = serializers.CharField()
	price = serializers.DecimalField(max_digits=6, decimal_places=2)
	pub_date = serializers.DateTimeField()
	# 外键，多对多关系处理，get请求
	pub = PublisherSerializer(read_only=True)
	authors = serializers.SerializerMethodField()
	# post请求
	post_pub = serializers.IntegerField(write_only=True)
	post_authors = serializers.ListField(write_only=True)

	def get_authors(self, obj):
		obj = AuthorSerializer(obj.authors.all(), many=True)
		return obj.data

	def create(self, validated_data):
		book = models.Book.objects.create(
			title=validated_data.get('title'),
			price=validated_data.get('price'),
			pub_date=validated_data.get('pub_date'),
			pub_id=validated_data.get('post_pub'),
		)
		book.authors.set(validated_data.get('post_authors'))
		return book

	def update(self, instance, validated_data):

		instance.title = validated_data.get('title', instance.title)
		instance.price = validated_data.get('price', instance.price)
		instance.pub_date = validated_data.get('pub_date', instance.pub_date)
		instance.pub_id = validated_data.get('put_pub', instance.pub_id)
		instance.save()
		instance.authors.set(validated_data.get('put_authors', instance.authors.all()))
		return instance





