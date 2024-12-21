from django.db import models
from cloudinary.models import CloudinaryField

class UserInfo(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)  # Sử dụng CloudinaryField
    date = models.DateTimeField(auto_now_add=True)
    courses = models.TextField(blank=True, null=True)
    target = models.TextField(blank=True, null=True)
    study = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username