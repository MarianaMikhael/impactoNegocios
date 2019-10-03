from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

from .forms import UserLogin
from django.contrib.auth import logout


def login_request(request):
    context = {}
    form = UserLogin(request.POST or None)
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index_sistemas')
    context['form'] = form
    return render(request, 'account/login.html', context)


def logout_request(request):
    logout(request)
    return redirect('login')
