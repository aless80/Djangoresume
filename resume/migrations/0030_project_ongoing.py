# Generated by Django 2.0.2 on 2018-03-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0029_auto_20180308_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ongoing',
            field=models.BooleanField(default=False),
        ),
    ]
