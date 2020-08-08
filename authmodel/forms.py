from django import forms
from django.contrib.auth.forms import UserCreationForm, User, UserChangeForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth import login, logout, authenticate


class SignupForm(UserCreationForm):

    username = forms.CharField(
        label='username', label_suffix='-->', widget=forms.TextInput(attrs={'class': 'form-control'}))

    first_name = forms.CharField(
        label='Firstname', label_suffix='-->', widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = forms.CharField(
        label='Lastname', label_suffix='-->', widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.CharField(label='Email', label_suffix='-->', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    password1 = forms.CharField(
        label='Password', label_suffix='-->', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label='ConformPassword', label_suffix='-->', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='username', label_suffix='-->', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Password', label_suffix='-->', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = '__all__'


class SetPassword(SetPasswordForm):
    new_password1 = forms.CharField(
        label='Enter New Password', label_suffix='-->', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    new_password2 = forms.CharField(
        label='Confirm Password', label_suffix='-->', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = '__all__'


class UserForm(UserChangeForm):

    username = forms.CharField(
        label='username', label_suffix='-->', widget=forms.TextInput(attrs={'class': 'form-control'}))

    first_name = forms.CharField(
        label='Firstname', label_suffix='-->', widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = forms.CharField(
        label='Lastname', label_suffix='-->', widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.CharField(label='Email', label_suffix='-->', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]
        # fields = '__all__'
        
class AdminForm(UserChangeForm):
    password = None    
    class Meta:
        model = User
        exclude = ['password']
