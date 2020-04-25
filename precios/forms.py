from django import forms
from .models import ModulesPrice


class MyForm(forms.ModelForm):
    class Meta:
        model = ModulesPrice
        fields = ('price',)

