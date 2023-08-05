from django.contrib import admin
from .models import *


class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'create_time')
    list_display_links = ('id', 'name')
    
    search_fields = ('name',)
    list_filter = ('create_time',)
    # sets slug automatucly
    prepopulated_fields = {'slug': ('name',)}


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'poster', 'create_time')
    list_display_links = ('id', 'title')

    search_fields = ('title',)
    list_filter = ('create_time',)
    # sets slug automatucly
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

    search_fields = ('name',)
    # sets slug automatucly
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Actor, ActorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
