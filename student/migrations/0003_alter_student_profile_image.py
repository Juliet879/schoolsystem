# Generated by Django 3.2.8 on 2021-10-14 06:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210905_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]
