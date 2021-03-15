from django.contrib import admin

from .models import Users, Songs, Ratings

admin.site.register(Users)
admin.site.register(Songs)
admin.site.register(Ratings)