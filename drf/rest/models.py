from django.db import models
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(max_length=30)
    imgpath = models.CharField(max_length=255)

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Категория'



class Course(models.Model):
    name = models.CharField(default=None, max_length=15)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    logo = models.CharField(null=True,default='logo.jpeg',max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'English Zone',
        verbose_name_plural = "Курсы"


class Contacts(models.Model):
    TYPE = (
        ('PHONE', 'phone'),
        ('EMAIL', 'email'),
        ('FACEBOOK', 'facebook'),
    )
    type = models.CharField(max_length=20,choices=TYPE,default='PHONE')
    value = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='contacts',null=True, blank=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = "Контакты"


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
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='branches',blank=True,null=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Ветки"
        verbose_name_plural = "Ветки"
