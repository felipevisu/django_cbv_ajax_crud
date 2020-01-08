from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.BookListView.as_view(), name='list'),
    path('create/', views.BookCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='delete'),
]
