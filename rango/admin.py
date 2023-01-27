from django.contrib import admin
from rango.models import Category, Page

# Register your models here.

# admin.site.register(Category)
admin.site.register(Page)


class PageInline(admin.TabularInline):
    model = Page
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'views', 'likes']
    inlines = [PageInline]
    list_display = ('name', 'views', 'likes')
    list_filter = ['views']
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)
