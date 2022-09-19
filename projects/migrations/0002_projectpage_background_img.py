# Generated by Django 4.0.3 on 2022-09-19 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='background_img',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.image'),
        ),
    ]
