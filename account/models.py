from django.db import models

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete="CASCADE")
    phone = models.CharField(max_length = 18)
    room = models.CharField(max_length = 8)
    year_of_birth = models.CharField(max_length = 4)
    active = models.BooleanField(default = True)
    avatar = models.ImageField(upload_to = 'images/')