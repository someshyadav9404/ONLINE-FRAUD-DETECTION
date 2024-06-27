from django.db import models

class students(models.Model):
    name = models.CharField(max_length=199)