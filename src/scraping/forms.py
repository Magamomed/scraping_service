from django import forms

from .models import City, Language


class FindForm(forms.Form):
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(),to_field_name="slug", required=False,
        widget=forms.Select(attrs={'class': 'mb-3'}),
        label='Cпециальность'
    )
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), to_field_name="slug", required=False,
        widget=forms.Select(attrs={'class': 'mb-3'}),
        label='Город'
    )



