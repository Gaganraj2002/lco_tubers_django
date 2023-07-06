from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html
# Register your models here.


class YTAdmin(admin.ModelAdmin):
    def pic(self, object):
        return format_html("<img src={} width =40 />".format(object.photo.url))

    list_display = ("id", "pic", "name", "subs_count", "is_featured")
    search_fields = ("camera_type", "name")
    list_filter = ("camera_type", "name")
    list_display_links = ("id", "name")
    list_editable = ("is_featured",)


admin.site.register(Youtuber, YTAdmin)
