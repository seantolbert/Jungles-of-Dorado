from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

class ProjectBlock(blocks.StructBlock):
    label = blocks.CharBlock()
    description = blocks.TextBlock()

class ProjectPage(Page):
    project = StreamField([
        ('project', ProjectBlock())
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('project')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_projects = ProjectPage.objects.live()
        context["projects"] = all_projects
        return context