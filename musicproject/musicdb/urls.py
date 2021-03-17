from django.urls import path
from . import views
from musicdb.views import index, user_create, retrieve_ratings

urlpatterns = [
    path('', index, name='index'),
    path('register/', user_create, name='user_create'),
    path('retrieve/', retrieve_ratings, name='retrieve_ratings')
]