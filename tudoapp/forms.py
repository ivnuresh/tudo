from django import forms
from .models import Task

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task Name'}),
            'priority': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Priority'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'name': 'Task Name',
            'priority': 'Priority',
            'date': 'Date',
        }
