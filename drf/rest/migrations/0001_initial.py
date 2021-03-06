# Generated by Django 2.1.2 on 2018-10-30 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Ветки',
                'verbose_name_plural': 'Ветки',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('imgpath', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PHONE', 'phone'), ('EMAIL', 'email'), ('FACEBOOK', 'facebook')], default='PHONE', max_length=20)),
                ('value', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=15)),
                ('description', models.CharField(max_length=255)),
                ('logo', models.CharField(blank=True, default='logo.jpeg', max_length=255, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rest.Category')),
            ],
            options={
                'verbose_name': ('English Zone',),
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.AddField(
            model_name='contacts',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='rest.Course'),
        ),
        migrations.AddField(
            model_name='branches',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='rest.Course'),
        ),
    ]
