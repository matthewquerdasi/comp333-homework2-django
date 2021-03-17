from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from musicdb.forms import UserForm, RetrieveRatingsForm, RetrieveByYearForm
from musicdb.models import Users, Ratings, Years

def index(request):
    return render(request, 'index.html')

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_create')
    else:
        form = UserForm()
    return render(request, 'user_create.html', {'form': form})


def retrieve_ratings(request):
    form = RetrieveRatingsForm(request.GET or None)
    ratings = None 
    if request.method == 'GET':
        if form.is_valid():
            # return HttpResponse("POST SUCCESSFUL")
            ratings = Ratings.objects.filter(username=form.cleaned_data.get('username'))
            
    return render(request, 'retrieve_ratings.html', {'form': form, 'ratings': ratings})

def retrieve_years(request):
    form = RetrieveByYearForm(request.GET or None)
    year = None
    if request.method == 'GET':
        if form.is_valid():
            year = Years.objects.filter(year=form.cleaned_data.get('year'))

    return render(request, 'retrieve_years.html', {'form': form, 'year': year})


