from django import forms
from . models import MissingMark

class MissingMarkForm(forms.ModelForm):
    class Meta:
        model = MissingMark
        fields = ("__all__")