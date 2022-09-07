# Generated by Django 4.0.3 on 2022-09-06 19:27

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='projectpage',
            name='label',
        ),
        migrations.AddField(
            model_name='projectpage',
            name='project',
            field=wagtail.core.fields.StreamField([('project_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock())]))], blank=True, null=True),
        ),
    ]
