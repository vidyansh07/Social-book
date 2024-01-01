from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Profile(models.Model):
    user  = models.ForeignKey(User, on_delete = models.CASCADE)
  
    profileimg = models.ImageField(upload_to='profile_images', default= "avatar.png")
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    