# Generated by Django 2.0.3 on 2018-03-31 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0046_auto_20180331_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='picture',
            new_name='image',
        ),
    ]
