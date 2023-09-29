from django import forms
from .models import TradingAlgorithm


class TradingAlgorithmForm(forms.ModelForm):
    class Meta:
        model = TradingAlgorithm
        fields = ['name', 'description', 'code']
