from django.urls import path
from . import views
from musicdb.views import index, user_create, retrieve_ratings, retrieve_years
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'users', views.UserView, 'users')

urlpatterns = [
    path('', index, name='index'),
    path('register/', user_create, name='user_create'),
    path('retrieve/', retrieve_ratings, name='retrieve_ratings'),
    path('retrieve-by-year/', retrieve_years, name='retrieve_years'),
    path('api/', include(router.urls))
]