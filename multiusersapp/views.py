from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, SignUpForm

# Create your views here.
def index(request):
    render(request,'index.html')

def register(request):
    msg=None
    if request.method=='POST':
        registerform=SignUpForm(request.POST)
        if registerform.is_valid():
            user=registerform.save()
            msg='User registered successfully'
            return redirect("login")
        else:
            msg='Register form is not valid'           
    else:        
        registerform=SignUpForm()
    return render(request, 'register.html', {"regform":registerform, "msg":msg}) 

def login(request):
    msg=None
    if request.method=='POST':
        form=LoginForm(request.POST) 
        if form.is_valid():
            username=form.cleaned_date.get("username")
            password=form.cleaned_date.get("password")
            user=authenticate(username=username, password=password)
            msg='Logged in successfully'
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('index')
            else:
                msg='Invalid credentials!'       
        else:
            msg='Error in validating the form'
    else:        
        form=LoginForm
    return render(request, 'login.html', {"form":form, "msg":msg})

def admin(request):
    return render(request, 'adminpage.html')    

def logout_view(request):
    logout(request)
    return redirect('index')




    