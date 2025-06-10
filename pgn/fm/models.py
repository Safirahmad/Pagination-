from django.db import models
from tinymce.models import HTMLField

class forms(models.Model):
    user_name = models.CharField(max_length=20 , default='ahmad') 
    user_email = models.CharField(max_length=30)
    user_phone=models.CharField(max_length=12)
    user_message = HTMLField()


# Create your models here.
