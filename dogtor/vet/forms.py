from django import forms

from .models import PetOwner

class OwnerForm(forms.ModelForm):
    Class Meta:
        model: PetOwner
        fields = ["first_name", "last_name", "address", "email", "phone"]
        widgets = {
            "email": forms. 
        }