from django import forms

class RegisterPrincipal(forms.Form):
    email=forms.EmailField()
    password1=forms.CharField(widget=forms.PasswordInput,required=False)
    password2=forms.CharField(widget=forms.PasswordInput,required=False)

class LoginPrincipal(forms.Form):
    email = forms.EmailField(required=False)
    password1 = forms.CharField(widget=forms.PasswordInput)


class Register(forms.Form):
    firstname=forms.CharField(max_length=100,required=False)
    lastname=forms.CharField(max_length=100,required=False)
    studing=forms.CharField(max_length=10,required=False)
    bloodgroup=forms.CharField(max_length=100,required=False)