from django import forms
from .models import TaskStatus
from django.utils.translation import gettext_lazy as _


class CreateStatusForm(forms.ModelForm):
    class Meta:
        model = TaskStatus
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': _('Name')
        }
