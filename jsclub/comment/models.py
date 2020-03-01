# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from jsclub.confession import Confession

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    confession = models.ForeignKey(Confession, on_delete = models.CASCADE)