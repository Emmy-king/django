from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='images',default='image/d3d4c2c0-8976-4c9f-888e-3e548d0fca14-PhotoRoom.png-PhotoRoom.png', blank=True, null=True)
    def __str__(self):
        return self.user.username