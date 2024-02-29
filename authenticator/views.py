from django.shortcuts import render
from . import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model as User

# Create your views here.
def renderSignup(req):
    if req.method=="POST":
        form = forms.CustomUserForm(req.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.error_messages)
            print("form is not valid")

    print(User().objects.all())

    context = {
        'form': forms.CustomUserForm
    }
    return render(req,"authenticator/SignUp.html",context=context)