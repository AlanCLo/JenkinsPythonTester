from django import forms
from .models import Cat, Human

class CatForm(forms.ModelForm):
	class Meta:
		model = Cat
		fields = ('name', 'owner')

