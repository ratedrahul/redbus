from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_bus, name='book_bus'),
]
