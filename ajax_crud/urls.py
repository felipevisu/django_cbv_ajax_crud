from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.books.urls')),
    path('admin/', admin.site.urls),
    path('locations/', include('apps.locations.urls')),
]
