# Generated by Django 4.0.3 on 2022-09-30 13:23

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_homepage_below_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='above_posts',
            field=wagtail.core.fields.StreamField([('cardblock', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock())])), ('extra_headline', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='below_posts',
            field=wagtail.core.fields.StreamField([('cardblock', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock())])), ('extra_headline', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        ),
    ]
