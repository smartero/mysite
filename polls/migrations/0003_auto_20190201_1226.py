# Generated by Django 2.1.5 on 2019-02-01 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20190131_2204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='resort',
            new_name='arr_adress',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='dep_city',
            new_name='dep_adress',
        ),
        migrations.RemoveField(
            model_name='result',
            name='baggage',
        ),
        migrations.RemoveField(
            model_name='result',
            name='boots',
        ),
    ]
