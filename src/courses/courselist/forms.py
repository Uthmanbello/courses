from django import forms
from .models import Courselist, Topic

class CourseForm(forms.ModelForm):
    class Meta:
        model = Courselist
        fields = ['name', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'text-field secondary'}),
            'icon': forms.Select(attrs={'class': 'select-field secondary'}),
        }

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'text-field secondary'}),
            'description': forms.TextInput(attrs={'class': 'text-field secondary'}),
        }
