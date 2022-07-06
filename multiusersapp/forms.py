from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm:
    username=forms.CharField(
        widget=forms.TextInput( attrs={"class":"form-control"} )
    )
    password=forms.PasswordInput(
        widget=forms.PasswordInput( attrs={"class":"form-control"} )
    )


class SignUpForm:
    username=forms.CharField(widget=forms.TextInput( attrs={"class":"form-control"} ))
    password1=forms.PasswordInput(widget=forms.PasswordInput( attrs={"class":"form-control"} ))
    password2=forms.PasswordInput(widget=forms.PasswordInput( attrs={"class":"form-control"} ))
    email=forms.EmailField(widget=forms.PasswordInput( attrs={"class":"form-control"} )) 

    class Meta:
        model=User
        fields=('username', 'email', 'password1', 'password2', 'is_admin', 'is_student')
        fields='__all__'   