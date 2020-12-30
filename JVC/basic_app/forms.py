from django import forms
from django.contrib.auth.models import User
from basic_app.models import WorkersProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):

    class meta():
        model = WorkersProfileInfo
        exclude = ('Protfolio_site','Profile_pic')