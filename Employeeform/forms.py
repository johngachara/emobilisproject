from .models import Employee
from django import forms
class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'date_of_birth':forms.DateInput(attrs={'type':'date'}),
            'email':forms.EmailInput(attrs={'type':'email'})
        }
