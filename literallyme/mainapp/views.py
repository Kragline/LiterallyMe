from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *


def actors_list(request):
    actors = Actor.objects.all()

    context = {
        'actors': actors,
        'title': 'Literally me - Main'
    }

    return render(request, 'mainapp/actor/actors_list.html', context=context)


def about_actor(request, actor_slug):
    actor = get_object_or_404(Actor, slug=actor_slug)
    context = {
        'actor': actor,
        'title': 'About ' + actor.name
    }

    return render(request, 'mainapp/actor/about_actor.html', context=context)


def add_actor(request):
    if request.POST:
        form = AddActorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddActorForm()

    context = {
        'form': form,
        'title': 'Add actor'
    }
    return render(request, 'mainapp/actor/add_actor.html', context)


def movies_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
        'title': 'Literalle me movies'
    }

    return render(request, 'mainapp/movie/movies_list.html', context=context)


def about_movie(request, movie_slug):
    movie = get_object_or_404(Movie, slug=movie_slug)
    context = {
        'movie': movie,
        'title': 'About ' + movie.title
    }

    return render(request, 'mainapp/movie/about_movie.html', context=context)


def add_movie(request):
    if request.POST:
        form = AddMovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddMovieForm()

    context = {
        'form': form,
        'title': 'Add movie'
    }

    return render(request, 'mainapp/movie/add_movie.html', context=context)


def show_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    category_pk = category.pk
    movies_category = Category.objects.get(pk=category_pk)
    movies = Movie.objects.filter(category=movies_category)

    context = {
        'movies': movies,
        'title': 'About ' + category_slug.capitalize()
    }

    return render(request, 'mainapp/category/show_category.html', context=context)


def add_category(request):
    if request.POST:
        form = AddCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddCategoryForm()

    context = {
        'form': form,
        'title': 'Add category'
    }

    return render(request, 'mainapp/category/add_category.html', context=context)


# works only if DEBUG in settings.py is False
# and ALLOWED_HOSTS is ['127.0.0.1'] for example
def pageNotFound(reuest, exception):
    return HttpResponseNotFound(f'<h1>Cant found that page</h1>')