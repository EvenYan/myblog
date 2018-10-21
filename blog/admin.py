# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from blog.models import Post, Category, Tag


class PostModelAdmin(admin.ModelAdmin):
    # list_display = ('__str__',)
    # list_display_links = ()
    # list_filter = ()
    # list_select_related = False
    # list_per_page = 100
    # list_max_show_all = 200
    # list_editable = ()
    # search_fields = ()
    # date_hierarchy = None
    # save_as = False
    # save_as_continue = True
    # save_on_top = False
    # preserve_filters = True
    # inlines = []
    list_display = ('id', 'title', 'created_time')
    list_per_page = 10
    search_fields = ('id',)
    # fields = ("title", "created_time", "modified_time", "excerpt")
    # fieldsets = (('基本信息', {'fields': ('title', 'body')}), ("详细信息", {"fields": ("created_time", "modified_time", "excerpt")}))
    # list_filter = ("title", 'views')


admin.site.register(Post, PostModelAdmin)
admin.site.register(Category)
admin.site.register(Tag)