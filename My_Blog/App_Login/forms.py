from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from App_Login.models import UserProfile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='First name', max_length=50)
    last_name = forms.CharField(label='Last name', max_length=50)
    email = forms.EmailField(label='Email')
    class Meta:

        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class ProfilePicForm(forms.ModelForm):
    class Meta:

        model =  UserProfile
        fields = ('profile_pic',)

 
class UserProfileChange(UserChangeForm):
    first_name = forms.CharField(label='First name', max_length=50)
    last_name = forms.CharField(label='Last name', max_length=50)
    email = forms.EmailField(label='Email')
    class Meta:

        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')