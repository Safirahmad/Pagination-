from django.db import models
from tinymce.models import HTMLField
class card(models.Model):
    car_title = models.CharField(max_length=23)
    car_desc = HTMLField()
    car_line = models.CharField(max_length= 200)

class newcar(models.Model):
    car_new_title = models.CharField(max_length=12)
    car_new_des = models.CharField(max_length=500)

# Create your models here.
