# Generated by Django 2.1.5 on 2019-02-26 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20190225_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='comment',
            field=models.CharField(blank=True, help_text='Place any additional info that you consider important (what music you like to listen in car, smoking/non-smoking, like to chat or prefer sray silent, etc)', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='dep_address',
            field=models.CharField(help_text='Chhose city or district', max_length=300),
        ),
        migrations.AlterField(
            model_name='result',
            name='dep_date',
            field=models.DateField(),
        ),
    ]