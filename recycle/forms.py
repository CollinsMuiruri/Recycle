from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction

from django.contrib.auth import get_user_model
User = get_user_model()

from .models import User

class ConsumerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_consumer = True
        if commit:
            user.save()
        return user