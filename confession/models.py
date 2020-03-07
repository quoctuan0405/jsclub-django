from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Confession(models.Model):
    title = models.CharField(max_length = 45)
    body = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__ (self):
    	return self.title