from django import forms
from .models import Registration,Person,Bid1,Bid2,Contact
class DateInput(forms.DateInput):
    input_type = "date"

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"                 # it will display all the fields the forms except default fields like id and registrationtime
        widgets = {"password":forms.PasswordInput(),"dateofbirth":DateInput()}  # additional features of the fields
        labels = {"gender":"Select Gender","location":"Provide Location"}  #using this, we can change label name in the form
        #exclude = {"gender"}       #using this, we can hide the fields in the form

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields="__all__"
        widgets ={"peronspassword":forms.PasswordInput()}
        exclude={"personlocation"}

class Bid1Form(forms.ModelForm):
    class Meta:
        model=Bid1
        fields="__all__"

class Bid2Form(forms.ModelForm):
    class Meta:
        model=Bid1
        fields="__all__"

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields = "__all__"