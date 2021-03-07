from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('musicdb/', include('musicdb.urls')),
    path('admin/', admin.site.urls),
]
