from django.contrib import admin

# Register your models here. title

from .models import *

class Top10CartoonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tittle', 'time_crete', 'photo', 'is_published')
    list_display_links = ('id', 'tittle')
    search_fields = ('tittle', 'content')


admin.site.register(Top10Cartoons, Top10CartoonsAdmin)
