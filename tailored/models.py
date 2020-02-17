from django.db import models

# Create your models here.
class Photographer(models.Model):
    name = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=40, default='')
    category = models.CharField(max_length=40, default='no category')
    price = models.CharField(max_length=100, default='')
    photo_url = models.TextField()

    def __str__ (self):
        return self.photo_url