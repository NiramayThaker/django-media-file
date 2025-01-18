from django import forms
from core.models import Dog


class DogForm(forms.ModelForm):
	class Meta:
		model = Dog
		fields = ('name', 'image')
		widgets = {
			'image': forms.FileInput(attrs={'accept': '.png, .jpg'})
		}
