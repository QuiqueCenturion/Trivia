# Generated by Django 2.0.13 on 2019-05-11 17:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0002_auto_20190510_1832'),
        ('accounts', '0004_auto_20190511_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayedGames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_questions', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)])),
                ('last_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Level')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ProfileUser')),
            ],
        ),
    ]