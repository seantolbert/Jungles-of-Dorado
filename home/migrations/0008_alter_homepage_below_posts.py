# Generated by Django 4.0.3 on 2022-09-26 18:33

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_homepage_above_posts_homepage_below_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='below_posts',
            field=wagtail.core.fields.StreamField([('stream_heading', wagtail.core.blocks.CharBlock()), ('stream_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('stream_image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        ),
    ]
