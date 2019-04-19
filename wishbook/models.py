from django.db import models

# Create your models here.


class Wish(models.Model):
    wish_text = models.TextField()
    wish_owner = models.CharField(max_length=50)
    shown = models.BooleanField()
