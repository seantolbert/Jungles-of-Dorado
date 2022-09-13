from django.utils.html import format_html
from django.templatetags.static import static

from wagtail.core import hooks


@hooks.register("insert_global_admin_css", order=100)
def global_admin_css():
    # adding
    return format_html('<link rel="stylesheet" href="{}">', static("css/custom.css"))
