from django.shortcuts import render, redirect
from .forms import UserSignup, UserLogin
from django.contrib.auth import login, logout, authenticate
from django.http import Http404


# Create your views here.


def user_signup(request):
    form = UserSignup()
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)

            return redirect("user-home")
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)


def user_login(request):
    form = UserLogin()
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('user-home')
    context = {
        'form': form,
    }
    return render(request, 'signin.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def some_view(request):
    if request.user.is_anonymous:
        return redirect('login')
    if not request.user.is_staff:
        raise Http404
