from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    displayname = forms.CharField(max_length=30)
    bio = forms.CharField(widget=forms.Textarea)
    birthdate =  forms.DateField(widget=forms.SelectDateWidget)
    

