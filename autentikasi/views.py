from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from .forms import LoginForm, RegisterForm

User = get_user_model()

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password_first")
        User.objects.create_user(username, email, password)
        user = authenticate(request, username=username, password=password)
        auth_login(request, user)
        return redirect('/')
    return render(request, 'register.html', context=context)

def login(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
    return render(request, 'login.html', context=context)

def logout(request):
    auth_logout(request)
    return render(request, 'logout.html')