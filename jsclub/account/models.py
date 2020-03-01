from django.db import models

import os
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete="CASCADE")
    phone = models.CharField(max_length = 18)
    room = models.CharField(max_length = 8)
    dob = models.DateTimeField(default = timezone.datetime.now())
    active = models.BooleanField(default = True)
    avatar = models.ImageField(upload_to = 'images/', default = os.path.join(settings.STATIC_ROOT, 'avatar.png'))