from django.urls import path
from .views import BookView


urlpatterns = [
    path('', BookView.as_view({'get': 'list', 'post': 'create'})),
    path('<int:book_id>/', BookView.as_view({'get': 'retrieve'}))
]