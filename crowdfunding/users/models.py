from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image = models.URLField(max_length=300, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')
    bio = models.TextField(default="Write bio here.")

    def __str__(self):
        return self.username
