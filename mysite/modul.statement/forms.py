from django.forms import fields
from .models import Statement
from django import forms


class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = '__all__'

