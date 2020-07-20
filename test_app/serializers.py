from rest_framework.serializers import ModelSerializer
from .models import Book


class BookListSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name']


class OneBookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookCreateSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
