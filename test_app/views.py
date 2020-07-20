from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Book
from .serializers import BookListSerializer, OneBookSerializer, BookCreateSerializer


class BookListView(ListAPIView):
    serializer_class = BookListSerializer
    queryset = Book.objects.all()


class OneBookView(APIView):
    def get(self, request, book_id):
        book = Book.objects.filter(id=book_id)
        serializer = OneBookSerializer(book, many=True)
        return Response({"books": serializer.data})


class BookCreateView(CreateAPIView):
    serializer_class = BookCreateSerializer