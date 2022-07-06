from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, SignUpForm

# Create your views here.
def index(request):
    render(request,'index.html')
