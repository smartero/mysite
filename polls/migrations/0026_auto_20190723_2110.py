# Generated by Django 2.1.5 on 2019-07-23 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_auto_20190723_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='car',
        ),
        migrations.AddField(
            model_name='result',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.Car'),
        ),
    ]