from django.shortcuts import render, redirect
from .models import Mobile  # Correct model import
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def products(request):
    mobiles = Mobile.objects.all()  # Fetch all Mobile objects from the database
    return render(request, 'products.html', {'mobiles': mobiles})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def search(request):
    query = request.GET.get('q', '')
    results = Mobile.objects.filter(Q(brand__icontains=query) | Q(model__icontains=query))
    return render(request, 'search_results.html', {'mobiles': results})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

# This function now uses the Mobile model and expects a 'product_list.html' template
def product_list(request):
    mobiles = Mobile.objects.all()
    return render(request, 'product_list.html', {'mobiles': mobiles})

def product_detail(request, id):
    mobile = Mobile.objects.get(id=id)
    return render(request, 'product_detail.html', {'mobile': mobile})
