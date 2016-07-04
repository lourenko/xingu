

from django import forms
from django.contrib.auth.models import User
from mysite.models import Category, Page, Student

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('groups', 'firstname', 'lastname', 'user_permissions', 'last_login')

