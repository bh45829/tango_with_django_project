from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile
# Register your models here.


class PageInline(admin.TabularInline):
    model = Page
    extra = 3


class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'category', 'url']
    list_display = ('title', 'category', 'url')
    list_filter = ['category']
    search_fields = ['title']


admin.site.register(Page, PageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'views', 'likes', 'slug']
    inlines = [PageInline]
    list_display = ('name', 'views', 'likes', 'slug')
    list_filter = ['views']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

admin.site.register(UserProfile)
