from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True, label='Email address')
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2'
            )
        

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']