from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def index(request):
    actors = Actor.objects.all()

    context = {
        'actors': actors,
        'title': 'Literally me - Main'
    }

    return render(request, 'mainapp/index.html', context=context)


def add_actor(request):
    return HttpResponse('<h1>Add actor page</h1>')


def login(request):
    return HttpResponse('<h1>Login page</h1>')

def about(request):
    context = {
        'title': 'Literally me - About'
    }

    return render(request, 'mainapp/about.html', context=context)


def about_actor(request, actor_slug):
    actor = get_object_or_404(Actor, slug=actor_slug)
    context = {
        'actor': actor,
        'title': 'About ' + actor.name
    }

    return render(request, 'mainapp/about_actor.html', context=context)


def movies(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
        'title': 'Literalle me movies'
    }

    return render(request, 'mainapp/movies.html', context=context)


def about_movie(request, movie_slug):
    movie = get_object_or_404(Movie, slug=movie_slug)
    context = {
        'movie': movie,
        'title': 'About ' + movie.title
    }

    return render(request, 'mainapp/about_movie.html', context=context)


def show_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    category_pk = category.pk
    movies_category = Category.objects.get(pk=category_pk)
    movies = Movie.objects.filter(category=movies_category)

    context = {
        'movies': movies,
        'title': 'About ' + category_slug.capitalize()
    }

    return render(request, 'mainapp/show_category.html', context=context)

# works only if DEBUG in settings.py is False
# and ALLOWED_HOSTS is ['127.0.0.1'] for example
def pageNotFound(reuest, exception):
    return HttpResponseNotFound(f'<h1>Cant found that page</h1>')