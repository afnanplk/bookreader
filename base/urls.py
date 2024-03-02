from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage, name='home'),
    path('books', views.Bookview.as_view(), name='books'),
    path('books/<slug:slug>', views.Bookview.as_view(), name='books'),
    path('books/<str:add>', views.Bookview.as_view(), name='addbook'),
]