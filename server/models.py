from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    courses = models.TextField(blank=True, null=True)
    target = models.TextField(blank=True, null=True)
    study = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username