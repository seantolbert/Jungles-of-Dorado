# Generated by Django 4.0.3 on 2022-09-26 17:56

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_background_homepage_background_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='above_posts',
            field=wagtail.core.fields.StreamField([('top_content', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('imageTwo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock())]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='below_posts',
            field=wagtail.core.fields.StreamField([('bottom_content', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('imageTwo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock())]))], blank=True, null=True),
        ),
    ]
