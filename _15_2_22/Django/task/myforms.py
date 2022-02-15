from django import forms

class Register(forms.Form):
    firstname=forms.CharField()
    lastname=forms.CharField()
    email=forms.EmailField(widget=forms.EmailInput())
    mobile=forms.IntegerField()
    password1=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())

class Login(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput())
    password=forms.CharField(widget=forms.PasswordInput())