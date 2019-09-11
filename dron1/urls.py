from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('telefon/',include('telefon.urls')),
    path('admin/', admin.site.urls),
]
