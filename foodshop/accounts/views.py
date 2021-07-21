from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import NewUSerForm
from customers.models import Profile
def signup_view(request):
    if request.method == 'POST':
        form = NewUSerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            profile,_ = Profile.objects.get_or_create(user=request.user)
            if profile is None:
                return redirect('customers:profile')

            return redirect('main:home')
    else:
        form = NewUSerForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            profile,_ = Profile.objects.get_or_create(user=request.user)
            if profile is None:
                return redirect('customers:profile')
            return redirect('main:home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return redirect('/')