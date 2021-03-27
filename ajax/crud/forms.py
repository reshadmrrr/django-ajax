from django import forms
from django.forms import widgets
from .models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ["university_id", "name", "semester", "phone_number"]
        widgets = {
            "university_id": forms.TextInput(
                attrs={"class": "form-control", "id": "university_id-input"}
            ),
            "name": forms.TextInput(
                attrs={"class": "form-control", "id": "name-input"}
            ),
            "semester": forms.TextInput(
                attrs={"class": "form-control", "id": "semester-input"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control", "id": "phone_number-input"}
            ),
        }
