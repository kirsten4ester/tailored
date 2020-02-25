from django.contrib import admin
from .models import Photographer, Category, Shoot

admin.site.register(Photographer)
admin.site.register(Category)
admin.site.register(Shoot)