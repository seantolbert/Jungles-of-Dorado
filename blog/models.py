from django.db import models
from django.utils import timezone

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

# class ImageBlock(blocks.StructBlock):
#     image = ImageChooserBlock()  
#     caption = blocks.CharBlock(classname="stream__img-caption", required=False)

#     class Meta:
#         icon = "image/picture"
#         admin_text = mark_safe("<b>Image Block</b>")
#         label = "Image Block"

class BlogPage(Page):
    date = models.DateField(default=timezone.now, blank=True, null=True)

    description = models.CharField(max_length=255, blank=True, null=True)

    main_image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL
    )

    main_image_excerpt = models.CharField(max_length=300, blank=True, null=True)

    body = StreamField(
        [
            ('image_block', blocks.StructBlock([
                ('image', ImageChooserBlock()),
                ('caption', blocks.CharBlock())
            ])),
            ("heading", blocks.CharBlock()),
            ("content", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
        ],
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("description"),
        ImageChooserPanel("main_image"),
        FieldPanel("main_image_excerpt"),
        StreamFieldPanel("body"),
    ]


class BlogIndexPage(Page):
    def blogs(self):
        blogs = BlogPage.objects.live()
        blogs = blogs.order_by("-date")
        return blogs
