# Generated by Django 2.1.5 on 2019-02-04 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_car', models.CharField(max_length=20)),
                ('your_model', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='/avatar_pics/default.jpg', upload_to='avatar_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('dep_address', models.CharField(max_length=100)),
                ('dep_date', models.DateField(default=django.utils.timezone.now)),
                ('arr_address', models.CharField(max_length=100)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('pax', models.IntegerField(default=1)),
                ('created_date', models.DateField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='polls.Car')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
