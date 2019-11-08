from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RecyclerProfile,Product

class SignUpForm(UserCreationForm):
    """
    Model Form to create a sign up form for businesses
    """
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username',)

class CreateProductForm(forms.ModelForm):
    """
    Form to facilitate creation of a Product
    """
    class Meta:
        model = Product
        fields = ['name']