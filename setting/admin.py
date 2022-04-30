from django.contrib import admin
from .models import Setting, SocialMedia
# Register your models here.

class SocialMediaInline(admin.StackedInline): #inline in Post
    model = SocialMedia
    extra = 0
@admin.register(Setting)
class Setting(admin.ModelAdmin):
    list_display = ("site_title","site_slogan","site_description",) #show columns in django admin
    list_filter = ("site_title",)
    list_per_page = 1
    search_fields = ("site_title__startswith", )
    empty_value_display = 'None'
    inlines = [SocialMediaInline]

"""
@admin.register(PostStatus)
class PostStatus(admin.ModelAdmin):
        list_display = ("status",)
"""
