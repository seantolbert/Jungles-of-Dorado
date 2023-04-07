from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class GalleryPage(Page):
    date = models.DateField(blank=True, null=True)

    gallery_photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    link = models.URLField(blank=True, null=True)

    description = models.CharField(max_length=500, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('gallery_photo'),
        FieldPanel('description'),
        FieldPanel('link')
    ]

class GalleryIndexPage(Page):
    
    def posts(self):
        posts = GalleryPage.objects.live()
        posts = posts.order_by('-date')
        return posts