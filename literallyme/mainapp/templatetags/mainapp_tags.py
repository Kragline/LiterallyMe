from django import template
from ..models import *


register = template.Library()


# simple tag, that will be used in base.html
@register.simple_tag()
def get_categories(sort=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.order_by(sort)


@register.simple_tag()
def get_movies_actors(movie):
    actors = movie.actors.all()
    cast = ''
    for actor in actors:
        cast += actor.name + ', '

    return cast.rstrip(', ')


@register.simple_tag()
def get_actors_movies(actor):
    movies = actor.movies.all()
    actor_movies = ''
    for movie in movies:
        actor_movies += movie.title + ', '

    return actor_movies.rstrip(', ')


# inclusion tag, loads categories to list_categories.html
# (didnt reated that, simple tag is better in this situation)
# @register.inclusion_tag('mainapp/list_categories.html')
# def show_categories(sort=None):
#     if not sort:
#         categories = Category.objects.all()
#     else:
#         categories = Category.objects.order_by(sort)
#     return {'categories': categories}
