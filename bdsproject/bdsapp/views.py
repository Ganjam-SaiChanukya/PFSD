from django.db.models import Q

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm,PersonForm
from .models import Registration,Person,Bid1,Bid2,Contact


def homepage(request):
    return render(request,"home.html")

def indexpage(request):
    return render(request,"index.html")

def registrationpage(request):
    return render(request,"registration.html")

def savetheperson(request):

    name=request.POST['name']
    gender=request.POST['gender']
    dateofbirth=request.POST['dateofbirth']
    emailid=request.POST['emailid']
    username=request.POST['username']
    password=request.POST['password']
    contactno=request.POST['contactno']
    Personobj=Person(personName=name,persongender=gender,persondob=dateofbirth,personemail=emailid,peronsusername=username,peronspassword=password,personcontact=contactno)
    Person.save(Personobj)
    return HttpResponse("DATA ADDED SUCCESSFULLY")


def loginpage(request):
    return render(request,"login.html")

def checkuserlogin(request):
    emailid=request.POST["emailid"]
    pwd=request.POST["password"]

    flag=Person.objects.filter( Q(personemail=emailid) & Q(peronspassword=pwd) )
    print(flag)

    if flag:
        user=Person.objects.get(personemail=emailid)
        print(user)
        print(user.personName,user.persondob,user.personemail)  #other fields
        request.session["uname"]=user.peronsusername
        return render(request,"services.html",{"uname":user.peronsusername})
    else:
        msg="Login Failed"
        return render(request, "login.html",{"msg":msg})

def servicepage(request):
    return render(request,"services.html")
def buyaproduct1(request):
    bidamount = request.POST["bidamount"]
    usermail = request.POST["usermail"]
    Bid1obj=Bid1(bidamount=bidamount,usermail=usermail)
    Bid1.save(Bid1obj)
    return HttpResponse("DATA ADDED SUCCESSFULLY")

def buyaproduct2(request):
    bidamount = request.POST["bidamount"]
    usermail = request.POST["usermail"]
    Bid2obj=Bid2(bidamount=bidamount,usermail=usermail)
    Bid2.save(Bid2obj)
    return HttpResponse("DATA ADDED SUCCESSFULLY")

def contactpage(request):
    return render(request,"contact.html")

def savethedatacontact(request):
    usermail=request.POST["usermail"]
    userfeedback=request.POST["userfeedback"]
    Contactobj=Contact(usermail=usermail,userfeedback=userfeedback)
    Contact.save(Contactobj)
    msg="successfully submitted"
    return render(request,"contact.html",{"msg":msg})