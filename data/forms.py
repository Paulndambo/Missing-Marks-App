from django import forms
from . models import MissingMark, Student

year_choices = (
    ("First Year", "First Year"),
    ("Second Year", "Second Year"),
    ("Third Year", "Third Year"),
    ("Fourth Year", "Fourth Year"),
    ("Fifth Year", "Fifth Year"),
)

class MissingMarkForm(forms.ModelForm):
    class Meta:
        model = MissingMark
        fields = ("__all__")

        widgets = {
            'student': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'username', 'type': 'hidden'}),
            'unit': forms.Select(attrs = {'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'lecturer': forms.Select(attrs={'class': 'form-control'}),
            'year_of_study': forms.Select(choices=year_choices, attrs={'class': 'form-control'}),
        }

class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("__all__")

        widgets = {
            'registration_number': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'username', 'type': 'hidden'}),
            'programme': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }
