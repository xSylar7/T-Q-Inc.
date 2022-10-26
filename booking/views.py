from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def get_home(request):
    return render(request, 'index.html')


@login_required
def user_home(request):
    return render(request, 'user_home.html')


@login_required
def user_profile(request):
    return render(request, 'user_profile.html')
