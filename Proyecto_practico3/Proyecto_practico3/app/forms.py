"""
Definition of forms.
"""

from django import forms
#from django.contrib.auth.forms import AuthenticationForm
#from django.utils.translation import ugettext_lazy as _

from app.models import Videogames

class VideogameForm(forms.ModelForm):
    class Meta:
        model = Videogames
        fields = ('name',
                  'publisher',
                  'year',
                  'genre',
                  'platform',
                  'score',
                  'online',
                  'pegi'
                  )