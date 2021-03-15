from django.urls import path
from . import views
from musicdb.views import user_create

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', user_create, name='user_create')
]