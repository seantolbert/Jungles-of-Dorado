from django.db import models
from django.utils import timezone

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import TaggedItemBase

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )

class BlogPage(Page):

    template = 'blog/blog_page.html'

    date = models.DateField(default=timezone.now, blank=True, null=True)

    description = models.CharField(max_length=255, blank=True, null=True)

    main_image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL
    )

    main_image_excerpt = models.CharField(max_length=300, blank=True, null=True)

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

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
        FieldPanel("tags"),
        ImageChooserPanel("main_image"),
        FieldPanel("main_image_excerpt"),
        StreamFieldPanel("body"),
    ]




class BlogIndexPage(Page):
    def blogs(self):
        blogs = BlogPage.objects.live().order_by('-date')
        return blogs
    
    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     all_posts = BlogPage.objects.live().order_by("-date")
    #     # if request.GET.get('tags', None):
    #     #     tags = request.GET.get('tags')
    #     #     all_posts = all_posts.filter(tags__slug__in=[tags])
    #     context["blogs"] = all_posts
    #     return context
