# Generated by Django 2.1.2 on 2018-10-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_auto_20181006_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='contacts',
            name='type',
            field=models.CharField(choices=[('PHONE', 'phone'), ('EMAIL', 'email'), ('FACEBOOK', 'facebook')], default='PHONE', max_length=20),
        ),
    ]