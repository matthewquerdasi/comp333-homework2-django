from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from musicdb.forms import UserForm, RetrieveRatingsForm
from musicdb.models import Users, Ratings

def index(request):
    return HttpResponse("Hello, world. You're at the musicdb index.")

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'user_create.html', {'form': form})

def login(request):
    return HttpResponse("LOGIN PAGE")


def retrieve_ratings(request):
    form = RetrieveRatingsForm(request.GET or None)
    ratings = None 
    if request.method == 'GET':
        if form.is_valid():
            # return HttpResponse("POST SUCCESSFUL")
            ratings = Ratings.objects.filter(username=form.cleaned_data.get('username'))
            
    return render(request, 'retrieve_ratings.html', {'form': form, 'ratings': ratings})


