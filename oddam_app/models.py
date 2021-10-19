from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)


class Institution(models.Model):
    TYPES = (
        ('F', 'fundacja'),
        ('O', 'organizacja pozarządowa'),
        ('Z', 'zbiórka lokalna'),
    )
    name = models.CharField(max_length=50)
    description = models.TextField
    type = models.CharField(max_length=1, choices=TYPES, default='F')
    categories = models.ManyToManyField(Category)
