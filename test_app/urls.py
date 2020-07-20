from django.urls import path
from .views import BookListView, OneBookView, BookCreateView


urlpatterns = [
    path('all/', BookListView.as_view()),
    path('<int:book_id>/', OneBookView.as_view()),
    path('new_book/', BookCreateView.as_view())
]