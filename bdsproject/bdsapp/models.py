from django.db import models
class Registration(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100,blank=False)
    gender_choices =  ( ("M","Male") , ("F","Female") , ("Others","Prefer not to say")  )
    gender=models.CharField(blank=False,choices=gender_choices,max_length=10)
    dateofbirth=models.CharField(max_length=20,blank=False)
    email=models.EmailField(max_length=50,blank=False,unique=True)
    username=models.CharField(max_length=50,blank=False,unique=True)
    password = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50, blank=False)
    contact = models.BigIntegerField(blank=False,unique=True)
    registrationtime = models.DateTimeField(blank=False,auto_now=True)

    class Meta:
        db_table = "registration_table"

class Person(models.Model):
    personName=models.CharField(max_length=20,blank=False)
    gender_choices = (("M", "Male"), ("F", "Female"), ("Others", "Prefer not to say"))
    persongender = models.CharField(blank=False, choices=gender_choices, max_length=10)
    persondob = models.DateField(max_length=20, blank=False)
    personemail = models.EmailField(max_length=50, blank=False, unique=True)
    peronsusername = models.CharField(max_length=50, blank=False, unique=True)
    peronspassword = models.CharField(max_length=50, blank=False)
    personlocation = models.CharField(max_length=50, blank=False)
    personcontact = models.BigIntegerField(blank=False, unique=True)
    class Meta:
        db_table="person_table"

class Bid1(models.Model):
    bidamount=models.PositiveIntegerField(blank=False,primary_key=True)
    usermail=models.CharField(max_length=50, blank=False, unique=True)
    class Meta:
        db_table="bid1_table"

class Bid2(models.Model):
    bidamount=models.PositiveIntegerField(blank=False,primary_key=True)
    usermail=models.CharField(max_length=50, blank=False, unique=True)
    class Meta:
        db_table="bid2_table"

class Contact(models.Model):
    usermail=models.CharField(max_length=50, blank=False, unique=True)
    userfeedback=models.CharField(max_length=200,blank=False)

    class Meta:
        db_table="contact_table"





























