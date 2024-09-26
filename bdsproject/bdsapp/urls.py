"""demoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.homepage,name="home"),
    path('',views.indexpage,name="index"),

    path('registration',views.registrationpage,name="registration"),
    path('savepersondata',views.savetheperson,name="savepersondata"),


    path('login',views.loginpage,name="login"),
    path("checkuserlogin", views.checkuserlogin, name="checkuserlogin"),

    path('services',views.servicepage,name="services"),
    path('buyaproduct1',views.buyaproduct1,name="buyaproduct1"),
    path('buyaproduct2', views.buyaproduct2, name="buyaproduct2"),

    path('contact',views.contactpage,name="contact"),
    path('savethedatacontact',views.savethedatacontact,name="savethedatacontact")


]