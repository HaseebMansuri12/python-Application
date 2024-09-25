from django import forms
from .models import *

class taskForm(forms.ModelForm):
	class Meta:
		model=taskModel
		fields="__all__"

class userForm(forms.ModelForm):
	class Meta:
		model=userModel
		fields="__all__"