from django import forms
from .models import Photographer, Shoot

#modelform is built into django that lets us build a form based off of our model
class PhotographerForm(forms.ModelForm):

    class Meta:
        model = Photographer
        # this is where youre selecting all of the input forms!! 
        # this datastructure = a tupel... tupels are safer you cannot add or remove from them
        # trailing commas with tuples -- conventionally
        fields = ('name', 'location', 'category', 'price', 'photo_url',)

class ShootForm(forms.ModelForm):

    class Meta:
        model = Shoot
        fields = ('photographer', 'title', 'category', 'photo_url',)