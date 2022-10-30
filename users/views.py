from operator import imod
from django.shortcuts import render, redirect
from .forms import UserSignup, UserLogin, UpdateProfileForm, UpdateUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages


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

            return redirect('user-home')
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
                return redirect('user-home', user_id=auth_user.id)
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


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('user-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'user_profile.html', {'user_form': user_form, 'profile_form': profile_form})
