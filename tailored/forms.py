from django import forms
from .models import Photographer, Category, Shoot

class SearchForm(forms.ModelForm):

    class Meta:
        model = Photographer
        fields = ('name', 'location', 'category', 'price', 'photo_url', 'avatar',)

class PhotographerForm(forms.ModelForm):

    class Meta:
        model = Photographer
        fields = ('name', 'location', 'category', 'price', 'photo_url',)

class ShootForm(forms.ModelForm):

    class Meta:
        model = Shoot
        fields = ('photographer', 'title', 'category', 'photo_url', 'image',)