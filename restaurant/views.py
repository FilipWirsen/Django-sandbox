from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from .models import SiteUser
from django.contrib.auth import authenticate, login
# Create your views here.


def signup_view(request):
    return render(request, 'signup.html')


def login_view(request):
    return render(request, 'login.html')
