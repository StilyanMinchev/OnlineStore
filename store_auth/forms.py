from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from store_auth.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('Email is required')
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        widgets={
            'profile_image': forms.FileInput(attrs={'class': 'custom-file-input'})
        }
        # fields = ('profile_image',)
        exclude = ('user',)
        # fields= '__all__'
