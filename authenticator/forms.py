from django.forms import ModelForm
from . import models
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        # fields = ('email', 'password1', 'password2')
        fields = "__all__" 