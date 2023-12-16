from django import forms

from tickets.models import Concert



class SearchForm(forms.Form):
    
    Searchtext = forms.CharField(max_length=100, label='نام کنسرت', required=False)


class ConcertForm(forms.ModelForm):
    class Meta:
        model = Concert
        fields = ['name', 'singer', 'length','poster']
