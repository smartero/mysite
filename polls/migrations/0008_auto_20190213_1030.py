# Generated by Django 2.1.5 on 2019-02-13 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20190209_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='dep_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='seats',
            field=models.IntegerField(),
        ),
    ]