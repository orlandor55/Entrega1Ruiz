# Generated by Django 3.2.9 on 2022-04-03 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='age',
            field=models.PositiveIntegerField(default=1, verbose_name='Edad'),
        ),
        migrations.AddField(
            model_name='familiar',
            name='birthday',
            field=models.DateField(default=datetime.date.today),
        ),
    ]