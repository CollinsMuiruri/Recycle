from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Neighbourhood,Business,Profile,Posts,Comments


class SignUpForm(UserCreationForm):
	'''
	Model form class to create a sign up form
	'''
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
        phone_number = forms.IntegerField(max_value=15, help_text='Required. Inform a valid phone number')
        drop_off_area = forms.URLField(help_text='Required. Inform a valid pin location')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
	def __init__(self,*args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] ='form-control'
		self.fields['email'].widget.attrs['class'] ='form-control'
		self.fields['first_name'].widget.attrs['class'] ='form-control'
		self.fields['last_name'].widget.attrs['class'] ='form-control'
		self.fields['password1'].widget.attrs['class'] ='form-control'
		self.fields['password2'].widget.attrs['class'] ='form-control'