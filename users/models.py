from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default='guest_user.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
