from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class AboutPage(Page):
    about_img = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL
    )
    description = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('about_img'),
        FieldPanel('description'),
        FieldPanel('email')
    ]