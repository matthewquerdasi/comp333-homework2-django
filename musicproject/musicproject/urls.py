from django.contrib import admin
from django.urls import include, path
from musicdb.views import user_create

urlpatterns = [
    path('musicdb/', include('musicdb.urls')),
    path('admin/', admin.site.urls),
]
