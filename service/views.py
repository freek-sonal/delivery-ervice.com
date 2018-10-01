from django.shortcuts import render
from django.http import HttpResponse
from . import templates
from .models import category,restaurant
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def firstPage(request):
    category_list=category.objects.order_by('add_date')
    context={
        'category_list':category_list,
    }
    return render(request,'homepage.html',context)

def restaurantPage(request):
    rest_list=restaurant.objects.order_by('cons_date')
    context={
        'rest_list':rest_list,
    }
    return render(request,'restaurant.html',context)

# signup and login page view

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/homepage')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
