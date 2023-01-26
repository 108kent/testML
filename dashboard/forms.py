from django import forms
from .models import Data


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'sex', 'age', 'year_in_germany']