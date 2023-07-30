from django import forms
from .models import Courselist

class CourseForm(forms.ModelForm):
    class Meta:
        model = Courselist
        fields = ['name', 'icon']
