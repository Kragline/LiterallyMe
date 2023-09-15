from django.db.models import Count
from .models import *


class DataMixin:
    paginate_by = 9

    @classmethod
    def get_categories(cls):
        return Category.objects.annotate(movies_count=Count('movies'))  # creating new column called movies_count

    def get_user_context(self, **kwargs):
        categories = self.get_categories()

        context = kwargs
        context['categories'] = categories

        return context
