# Generated by Django 4.0.3 on 2023-04-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerypage',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
