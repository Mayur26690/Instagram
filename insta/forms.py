from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import Profile 
from imgs.models import Image

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

class SignUpForm(UserCreationForm):
	fullname = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class Meta:
		model = User
		fields = ('email','fullname','username', 'password1', 'password2', )

class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
