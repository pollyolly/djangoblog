from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
from .models import Tag, Post, Comment, Category #import model Post
import csv
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin

from django.contrib.auth.models import Permission
admin.site.register(Permission)

#from .models import Post #import model Post

#admin.site.register(Post) #Register model Post in Django Admin Panel

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
    export_as_csv.short_description = "Export Selected"
"""
class CommentInline(admin.StackedInline): #inline in Post
    model = Comment
    extra = 0
"""
@admin.register(Category) #display in admin.py
class Category(admin.ModelAdmin):
    list_display = ("category","created","updated") #show columns in django admin
    list_filter = ("category",)
    list_per_page = 10
    search_fields = ("category__startswith", )
    empty_value_display = 'None'

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ("tag","created","updated") #show columns in django admin
    list_filter = ("tag",)
    list_per_page = 10
    search_fields = ("tag__startswith", )
    empty_value_display = 'None'

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ("name","comment","created","updated")
    list_filter = ("name",)
    list_per_page = 10
    search_fields = ("name__startswith","comment__contains",)
    empty_value_display = 'None'

@admin.register(Post)
class BlogPost(ImportExportModelAdmin,ExportCsvMixin):
    list_display = ('title','post','tag_list','category_list','status','created','updated') #show columns in django admin
    list_filter = ("title",)
    list_per_page = 10
    search_fields = ('title__startswith', 'post__contains',)
    empty_value_display = 'None'
    #inlines = [CommentInline]
    readonly_fields = ["thumbnail_image"]
    filter_horizontal = ('category',) #enable filter box horizontal for many to many field
    actions = ['export_as_csv']
    date_hierarchy = 'created'
    def thumbnail_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
            url = obj.thumbnail.url,
            width = obj.thumbnail.width,
            height = obj.thumbnail.height
            )
        )
