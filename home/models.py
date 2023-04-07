from email import header
from django.db import models

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel


from blog.models import BlogPage

from gallery.models import GalleryPage


class CardBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    content = blocks.RichTextBlock()


class HomePage(Page):

    def galList(self):
        galList = GalleryPage.objects.live()
        # galList = map(lambda g: g.index(), galList)
        galList = galList.order_by('-date')
        # galList = galList.order_by('-date')[:6]
        return galList
    


    # background_img = models.ForeignKey(
    #     "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL
    # )
    # headline = models.CharField(max_length=100, blank=True, null=True)
    # sub_headline = models.CharField(max_length=200, blank=True, null=True)

    # above_posts = StreamField([
    #     ("cardblock", CardBlock()),
    #     ("extra_headline", blocks.RichTextBlock())
    #     ], blank=True, null=True)

    # below_posts = StreamField([
    #     ("cardblock", CardBlock()),
    #     ("extra_headline", blocks.RichTextBlock())
    #     ], blank=True, null=True)

    # content_panels = Page.content_panels + [
    #     ImageChooserPanel("background_img"),
    #     FieldPanel("headline"),
    #     FieldPanel("sub_headline"),
    #     StreamFieldPanel("above_posts"),
    #     StreamFieldPanel("below_posts"),
    # ]

    # def blogs(self):
    #     blogs = BlogPage.objects.live()
    #     blogs = blogs.order_by("-date")[:6]
    #     return blogs

    # def blog_index(self):
    #     blogs = BlogPage.objects.live()
    #     blog = map(lambda b: b.index(), blogs)
    #     print(blog)
    #     return blog
