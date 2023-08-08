from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *


# def actors_list(request):
#     actors = Actor.objects.all()
#
#     context = {
#         'actors': actors,
#         'title': 'Literally me - Main'
#     }
#
#     return render(request, 'mainapp/actor/actors_list.html', context=context)


class ActorsListView(ListView):
    model = Actor
    template_name = 'mainapp/actor/actors_list.html'
    context_object_name = 'actors'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Literally me - Main'

        return context


# def about_actor(request, actor_slug):
#     actor = get_object_or_404(Actor, slug=actor_slug)
#     context = {
#         'actor': actor,
#         'title': 'About ' + actor.name
#     }
#
#     return render(request, 'mainapp/actor/about_actor.html', context=context)


class AboutActorView(DetailView):
    model = Actor
    template_name = 'mainapp/actor/about_actor.html'
    context_object_name = 'actor'
    slug_url_kwarg = 'actor_slug' # changing default slug name to what we need

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About ' + str(context['actor'].name)

        return context


# def add_actor(request):
#     if request.POST:
#         form = AddActorForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddActorForm()
#
#     context = {
#         'form': form,
#         'title': 'Add actor'
#     }
#     return render(request, 'mainapp/actor/add_actor.html', context)


class AddActorView(CreateView):
    form_class = AddActorForm
    template_name = 'mainapp/actor/add_actor.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add actor'

        return context


# def movies_list(request):
#     movies = Movie.objects.all()
#     context = {
#         'movies': movies,
#         'title': 'Literalle me movies'
#     }
#
#     return render(request, 'mainapp/movie/movies_list.html', context=context)


class MovieListView(ListView):
    model = Movie
    template_name = 'mainapp/movie/movies_list.html'
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Literalle me movies'

        return context


# def about_movie(request, movie_slug):
#     movie = get_object_or_404(Movie, slug=movie_slug)
#     context = {
#         'movie': movie,
#         'title': 'About ' + movie.title
#     }
#
#     return render(request, 'mainapp/movie/about_movie.html', context=context)


class AboutMovieView(DetailView):
    model = Movie
    template_name = 'mainapp/movie/about_movie.html'
    context_object_name = 'movie'
    slug_url_kwarg = 'movie_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About ' + context['movie'].title

        return context


# def add_movie(request):
#     if request.POST:
#         form = AddMovieForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddMovieForm()
#
#     context = {
#         'form': form,
#         'title': 'Add movie'
#     }
#
#     return render(request, 'mainapp/movie/add_movie.html', context=context)


class AddMovieView(CreateView):
    form_class = AddMovieForm
    template_name = 'mainapp/movie/add_movie.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add movie'

        return context


# def show_category(request, category_slug):
#     category = Category.objects.get(slug=category_slug)
#     category_pk = category.pk
#     movies_category = Category.objects.get(pk=category_pk)
#     movies = Movie.objects.filter(category=movies_category)
#
#     if len(movies) == 0:
#         raise Http404()
#
#     context = {
#         'movies': movies,
#         'title': 'About ' + movies[0].category.name
#     }
#
#     return render(request, 'mainapp/category/show_category.html', context=context)


class CategoryListView(ListView):
    model = Movie
    template_name = 'mainapp/category/show_category.html'
    context_object_name = 'movies'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category ' + str(context['movies'][0].category.name)

        return context

    def get_queryset(self):
        # category field (which is basicly the link to category model) in movies + slug field in categories = category__slug
        # show_category filtering code will work too, but need to repleace category_slug with self.kwargs['category_slug']
        return Movie.objects.filter(category__slug=self.kwargs['category_slug']) # getting clug of url from self.kwargs dictionary


# def add_category(request):
#     if request.POST:
#         form = AddCategoryForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddCategoryForm()
#
#     context = {
#         'form': form,
#         'title': 'Add category'
#     }
#
#     return render(request, 'mainapp/category/add_category.html', context=context)


class AddCategoryView(CreateView):
    form_class = AddCategoryForm
    template_name = 'mainapp/category/add_category.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add category'

        return context


# works only if DEBUG in settings.py is False
# and ALLOWED_HOSTS is ['127.0.0.1'] for example
def pageNotFound(reuest, exception):
    return HttpResponseNotFound(f'<h1>Cant found that page</h1>')