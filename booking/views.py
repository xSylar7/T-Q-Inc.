from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def get_home(request):
    return render(request, 'index.html')


@login_required
def user_home(request):
    return render(request, 'user.html')
