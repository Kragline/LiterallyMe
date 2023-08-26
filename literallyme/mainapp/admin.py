from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_photo', 'create_time')
    list_display_links = ('id', 'name')
    
    search_fields = ('name',)
    list_filter = ('create_time',)
    prepopulated_fields = {'slug': ('name',)}

    fields = ('name', 'bio', 'photo', 'slug', 'get_html_photo', 'create_time')
    readonly_fields = ('get_html_photo', 'create_time')

    save_on_top = True

    def get_html_photo(self, model_object):
        if model_object.photo:
            return mark_safe(f'<img src="{model_object.photo.url}" width=70">')

    get_html_photo.short_description = 'Photo'


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'poster', 'create_time', 'rating')
    list_display_links = ('id', 'title', 'rating')

    search_fields = ('title',)
    list_filter = ('create_time',)
    prepopulated_fields = {'slug': ('title',)}

    fields = ('title', 'plot', 'release_date', 'poster', 'get_html_photo',
              'trailer', 'actors', 'category', 'rating', 'slug', 'create_time')
    readonly_fields = ('get_html_photo', 'create_time')

    save_on_top = True

    def get_html_photo(self, model_object):
        if model_object.poster:
            return mark_safe(f'<img src="{model_object.poster.url}" width=70">')

    get_html_photo.short_description = 'Poster'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'movie', 'text')
    list_display_links = ('author', 'movie', 'text')


class CommentAnswerAdmin(admin.ModelAdmin):
    list_display = ('author', 'parent_comment', 'text')
    list_display_links = ('author', 'parent_comment', 'text')


admin.site.register(Actor, ActorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentAnswer, CommentAnswerAdmin)

admin.site.site_title = 'Literally Me Administration'
admin.site.site_header = 'Literally Me Administration'
