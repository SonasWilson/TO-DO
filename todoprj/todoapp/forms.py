from .models import Task
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'priority', 'date']
        labels = {
            'task_name': 'To Do',
            'priority': 'Priority',
            'date': 'Due Date'}