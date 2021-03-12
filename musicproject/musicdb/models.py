from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)

class Artists(models.Model):
    song = models.CharField(max_length=50, primary_key=True)
    artist = models.CharField(max_length=200)

class Ratings(models.Model):
    username = models.ForeignKey(Users, primary_key=True, unique=True, on_delete=models.CASCADE)
    song = models.ForeignKey(Artists, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)