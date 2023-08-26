from django.db.models import Count
from .models import *


menu = [
    {'title': 'Actors', 'url_name': 'actors'},
    {'title': 'Add actor', 'url_name': 'add_actor'},
    {'title': 'Add category', 'url_name': 'add_category'},
    {'title': 'Add movie', 'url_name': 'add_movie'}
]


class DataMixin:
    paginate_by = 6

    @classmethod
    def get_categories(cls):
        return Category.objects.annotate(movies_count=Count('movies'))  # creating new column called movies_count

    def get_user_context(self, **kwargs):
        categories = self.get_categories()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated or not self.request.user.is_superuser:
            user_menu = [user_menu[0]]

        context = kwargs
        context['menu'] = user_menu
        context['categories'] = categories

        return context
