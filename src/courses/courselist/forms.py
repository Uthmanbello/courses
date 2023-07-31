from django import forms
from .models import Courselist

class CourseForm(forms.ModelForm):
    class Meta:
        model = Courselist
        fields = ['name', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'text-field secondary'}),
            'icon': forms.Select(attrs={'class': 'select-field secondary'}),
        }
