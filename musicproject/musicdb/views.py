from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from musicdb.forms import UserForm
from musicdb.models import Users

def index(request):
    return HttpResponse("Hello, world. You're at the musicdb index.")

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_create')
    else:
        form = UserForm()
    return render(request, 'user_create.html', {'form': form})