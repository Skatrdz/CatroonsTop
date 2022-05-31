from django.contrib import admin

# Register your models here. title

from .models import *

class Top10CartoonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_crete', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')




admin.site.register(Film, Top10CartoonsAdmin)
admin.site.register(Category)
