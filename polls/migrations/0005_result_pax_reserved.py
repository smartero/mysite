# Generated by Django 2.1.5 on 2019-02-09 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_result_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='pax_reserved',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Profile'),
        ),
    ]
