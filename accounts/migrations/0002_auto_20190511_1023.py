# Generated by Django 2.0.13 on 2019-05-11 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
    ]
