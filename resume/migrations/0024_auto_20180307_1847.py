# Generated by Django 2.0.2 on 2018-03-07 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0023_auto_20180306_0959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='achievement',
            options={'ordering': ['order', 'id'], 'verbose_name_plural': '06. Achievements'},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-end_date', 'id'], 'verbose_name_plural': '03. Education'},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-end_date', 'id'], 'verbose_name_plural': '04. Jobs'},
        ),
        migrations.AlterModelOptions(
            name='jobaccomplishment',
            options={'ordering': ['order', 'id'], 'verbose_name_plural': '05. Job Accomplishments'},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['level', 'order'], 'verbose_name_plural': '12. Languages'},
        ),
        migrations.AlterModelOptions(
            name='overview',
            options={'verbose_name_plural': '01. Overview'},
        ),
        migrations.AlterModelOptions(
            name='personalinfo',
            options={'verbose_name_plural': '02. Personal Info'},
        ),
        migrations.AlterModelOptions(
            name='programmingarea',
            options={'ordering': ['order', 'name'], 'verbose_name_plural': '10. Programming areas'},
        ),
        migrations.AlterModelOptions(
            name='programminglanguage',
            options={'ordering': ['order', 'id'], 'verbose_name_plural': '11. Programming languages'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['order', 'id'], 'verbose_name_plural': '13. Projects'},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['-year', 'order'], 'verbose_name_plural': '07. Publications'},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['order', 'id'], 'verbose_name_plural': '09. Skills'},
        ),
        migrations.AlterModelOptions(
            name='skillset',
            options={'ordering': ['id'], 'verbose_name_plural': '08. Skillsets'},
        ),
        migrations.AlterField(
            model_name='skillset',
            name='name',
            field=models.TextField(),
        ),
    ]
