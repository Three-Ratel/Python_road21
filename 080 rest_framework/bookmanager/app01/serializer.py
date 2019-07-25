from rest_framework import serializers


class BookSerializer(serializers.Serializer):
	title = serializers.CharField()
	price = serializers.DecimalField(max_digits=6, decimal_places=2)
	pub_date = serializers.DateTimeField()
