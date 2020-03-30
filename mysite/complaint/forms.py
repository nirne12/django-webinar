from django import forms
from .models import Complaint


class CreateComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = '__all__'


