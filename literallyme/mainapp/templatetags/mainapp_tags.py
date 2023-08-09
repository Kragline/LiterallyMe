from django import template
from ..models import *


register = template.Library()


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
