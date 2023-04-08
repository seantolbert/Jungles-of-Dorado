from wagtail.api.v2.views import PagesAPIViewSet
from .serializers import BlogSerializer
from .models import BlogPage


class BlogViewSet(PagesAPIViewSet):
    queryset = BlogPage.objects.live().order_by('-date')

    # serializer_class = BlogSerializer
