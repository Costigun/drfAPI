from django.db import models
from django.utils import timezone

class Tea(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    king = models.CharField(
        max_length=25,
        default=None,
    )
    dateborn = models.DateTimeField(
        default=timezone.now
    )
    text = models.TextField(
        max_length=250,
        blank=True
    )
    print(123)
def born(self):
    self.dateborn = timezone.now()
    self.save()
    

def __str__(self):
    return self.king

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