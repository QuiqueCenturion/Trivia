# Generated by Django 2.0.13 on 2019-05-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190511_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='f_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='l_name',
            field=models.CharField(default='', max_length=40),
        ),
    ]