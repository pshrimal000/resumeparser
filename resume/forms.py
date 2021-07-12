from .models import ProfileDetail
from django import forms


class ProfileDetailForm(forms.ModelForm):
    class Meta:
        model=ProfileDetail
        fields="__all__"
