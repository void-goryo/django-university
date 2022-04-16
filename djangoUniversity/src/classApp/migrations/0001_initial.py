# Generated by Django 4.0.3 on 2022-04-16 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('courseNumber', models.IntegerField(default='', max_length=4)),
                ('instructorName', models.CharField(default='', max_length=50)),
                ('duration', models.FloatField(default='', max_length=2)),
            ],
        ),
    ]
