from django.db import models
from django.utils import timezone

class Ezone(models.Model):
    name = models.CharField(default=None,
        max_length=15)
    description = models.CharField(
        max_length=255
    )
    category = models.TextField(default=None,
        max_length=100
        )
    logo = models.ImageField(null=True)
    def __str__(self):
        return self.category

class Contacts(models.Model):
    TYPE=(
        ('PHONE','phone'),
        ('EMAIL','email'),
        ('FACEBOOK','facebook'),
    )
    type = models.CharField(
        max_length=20,
        choices=TYPE,
        default='PHONE'
    )
    value = models.CharField(
        max_length=100
    )
    ezone = models.ForeignKey(
        Ezone,
        on_delete=models.CASCADE,
        related_name='contacts'

    )
    def __str__(self):
        return self.type

class Branches(models.Model):
    address = models.CharField(
        max_length=255
    )
    latitude = models.CharField(
        max_length=255
    )
    longitude = models.CharField(
        max_length=255
    )
    ezone = models.ForeignKey(Ezone,
        on_delete=models.CASCADE,
        related_name='branches'
    )
    def __str__(self):
        return self.address
  