from django import forms
from data.models import Lecturer

class CreateLecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ("__all__")

        widgets = {
            'registration_number': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'username', 'type': 'hidden'}),
            'programme': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }
