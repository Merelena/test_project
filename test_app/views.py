from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer, OneBookSerializer, BookCreateSerializer
from rest_framework import viewsets
from rest_framework import mixins


class BookView(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer

    def list(self, request):
        BookView.queryset = Book.objects.all()
        serializer = BookSerializer(BookView.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, book_id=None):
        instance = BookView.queryset.filter(id=book_id)
        serializer = OneBookSerializer(instance=instance, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = BookCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
