from django.db import models

class carousel(models.Model):
    name = models.CharField(max_length=199)
    image = models.ImageField
    content = models.TextField