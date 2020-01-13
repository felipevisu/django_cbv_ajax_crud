from django.urls import path

from . import views

app_name = 'locations'
urlpatterns = [
    path('', views.CityListView.as_view(), name='list'),
    path('create/', views.CityCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.CityUpdateView.as_view(), name='update'),
]
