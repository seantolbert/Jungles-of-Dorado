from wagtail.api.v2.serializers import PageSerializer
from .models import BlogPage
from wagtail.images.api.fields import ImageRenditionField


class BlogSerializer(PageSerializer):

    main_image = ImageRenditionField("original")

    class Meta:
        model = BlogPage
        fields = (
            "title",
            "body",
            "description",
            "main_image",
            "main_image_excerpt",
            "tags",
        )
