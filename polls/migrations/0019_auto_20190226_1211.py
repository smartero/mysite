# Generated by Django 2.1.5 on 2019-02-26 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20190226_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='arr_address',
            field=models.CharField(help_text='City or district', max_length=300),
        ),
        migrations.AlterField(
            model_name='result',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='seats',
            field=models.IntegerField(help_text='Free seats available for reservation'),
        ),
    ]
