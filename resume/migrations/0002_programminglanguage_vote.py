# Generated by Django 2.0.2 on 2018-03-03 16:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programminglanguage',
            name='vote',
            field=models.IntegerField(blank=True, help_text='Kill level 1 to 5', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]