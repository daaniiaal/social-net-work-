from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile

class UserRegistrationForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'enter your email address'}))
    password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'enter your password'}))
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'enter your password again'}))
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email already exists')
        return email
    


    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('this username alread exists')
        return username
    
    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')
        
        if p1 and p2 and p1 != p2 :
            raise ValidationError('passwords must match')
        


class UserLoginForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'enter your password'}))



class EditUserForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = Profile
        fields = ('age' , 'bio')
