from django import forms
from .models import UserDetails

class UserForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = '__all__'