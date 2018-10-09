# Generated by Django 2.1.2 on 2018-10-06 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_ezone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='ezone',
            name='logo',
            field=models.ImageField(upload_to='home/meaculpa/Изображения/ezone.jpg', verbose_name='logo'),
        ),
    ]
