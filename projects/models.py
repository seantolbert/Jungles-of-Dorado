from wagtail.core import blocks
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class ProjectBlock(blocks.StructBlock):
    label = blocks.CharBlock()
    description = blocks.TextBlock()

class ProjectPage(Page):
    background_img = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL
    )
    project = StreamField([
        ('project', ProjectBlock())
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('background_img'),
        StreamFieldPanel('project')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_projects = ProjectPage.objects.live()
        context["projects"] = all_projects
        return context