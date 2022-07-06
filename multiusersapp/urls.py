from django import views
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('/admin', views.admin, name="adminpage"),
    path('/register', views.register, name="register"),
    path('/login', views.login_view, name="login"),

]