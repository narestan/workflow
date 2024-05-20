# reqmat/forms.py

from django import forms
from .models import ProfitRequest, GlassRequest, OtherRequest

class ProfitRequestForm(forms.ModelForm):
    class Meta:
        model = ProfitRequest
        fields = ['department', 'description', 'materials', 'profit_estimate']

class GlassRequestForm(forms.ModelForm):
    class Meta:
        model = GlassRequest
        fields = ['department', 'description', 'materials', 'dimensions']

class OtherRequestForm(forms.ModelForm):
    class Meta:
        model = OtherRequest
        fields = ['department', 'description', 'materials', 'details']
