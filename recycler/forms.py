from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CompanyProfile,Product

from django.contrib.auth import get_user_model
User = get_user_model()

class CompanySignUpForm(UserCreationForm):
    """
    Model Form to create a sign up form for businesses
    """
    class Meta:
        model = User
        fields = ('username',)

class CreateProductForm(forms.ModelForm):
    """
    Form to facilitate creation of a Product
    """
    class Meta:
        model = Product
        fields = ['name','description','mode_of_recycling']
        exclude = ['User']