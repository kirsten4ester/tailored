from django.db import models

class Photographer(models.Model):
    name = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=40, default='')
    category = models.CharField(max_length=40, default='no category')
    price = models.CharField(max_length=100, default='')
    photo_url = models.TextField(default='')
    avatar = models.TextField(default='')

    def __str__ (self):
        return self.avatar

class Shoot(models.Model):
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE, related_name='shoots')
    title = models.CharField (max_length=100, default='')
    category = models.CharField(max_length=40, default='no category')
    photo_url = models.TextField()
    image = models.TextField(null=True)

    def __str__ (self):
        return self.image

