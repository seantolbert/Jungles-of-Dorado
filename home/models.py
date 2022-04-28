from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

from blog.models import BlogPage
from gallery.models import GalleryPage


class HomePage(Page):
    headline = models.CharField(max_length=100, blank=True, null=True)
    sub_headline = models.CharField(max_length=200, blank=True, null=True)
    content_panels = Page.content_panels + [
        FieldPanel("headline"),
        FieldPanel("sub_headline"),
    ]   

    def blogs(self):
        blogs = BlogPage.objects.live()
        blogs = blogs.order_by("-date")[:3]
        return blogs