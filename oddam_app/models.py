from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Institution(models.Model):
    TYPES = (
        ('F', 'fundacja'),
        ('O', 'organizacja pozarządowa'),
        ('Z', 'zbiórka lokalna'),
    )
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    type = models.CharField(max_length=1, choices=TYPES, default='F')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.name}"


class Donation(models.Model):
    quantity = models.IntegerField()
    institution = models.ForeignKey(Institution, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=120)
    user = models.OneToOneField(User, null=True, default=True, on_delete=models.SET_NULL)
