# Generated by Django 4.0.3 on 2023-04-07 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_aboutpage_background_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutpage',
            old_name='background_img',
            new_name='about_img',
        ),
    ]
