from django.forms import ModelForm, CharField
from django import forms
from .models import Users, Ratings


class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'password']


class RetrieveRatingsForm(forms.Form):
    username = forms.CharField()


