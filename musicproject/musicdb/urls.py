from django.urls import path
from . import views
from musicdb.views import user_create, retrieve_ratings

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', user_create, name='user_create'),
    path('login/', views.login, name='login'),
    path('retrieve/', retrieve_ratings, name='retrieve_ratings')
]