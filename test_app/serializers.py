from rest_framework.serializers import ModelSerializer
from .models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author_name',)


class BookCreateSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class OneBookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
