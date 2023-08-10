from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from .forms import *
from .utils import *


class ActorsListView(DataMixin, ListView):
    model = Actor
    template_name = 'mainapp/actor/actors_list.html'
    context_object_name = 'actors'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Literally me - Main')

        return dict(list(context.items()) + list(mixin_context.items()))

    def get_queryset(self):
        return Actor.objects.order_by('create_time')


class AboutActorView(DataMixin, DetailView):
    model = Actor
    template_name = 'mainapp/actor/about_actor.html'
    context_object_name = 'actor'
    slug_url_kwarg = 'actor_slug'  # changing default slug name to what we need

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='About ' + str(context['actor'].name))

        return dict(list(context.items()) + list(mixin_context.items()))


class AddActorView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddActorForm
    template_name = 'mainapp/actor/add_actor.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Add actor')

        return dict(list(context.items()) + list(mixin_context.items()))


class MovieListView(DataMixin, ListView):
    model = Movie
    template_name = 'mainapp/movie/movies_list.html'
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Literally me movies')

        return dict(list(context.items()) + list(mixin_context.items()))

    def get_queryset(self):
        return Movie.objects.order_by('create_time')


class AboutMovieView(DataMixin, DetailView):
    model = Movie
    template_name = 'mainapp/movie/about_movie.html'
    context_object_name = 'movie'
    slug_url_kwarg = 'movie_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='About ' + context['movie'].title)

        return dict(list(context.items()) + list(mixin_context.items()))


class AddMovieView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddMovieForm
    template_name = 'mainapp/movie/add_movie.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Add movie')

        return dict(list(context.items()) + list(mixin_context.items()))


class CategoryListView(DataMixin, ListView):
    model = Movie
    template_name = 'mainapp/category/show_category.html'
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Category ' + context['movies'][0].category.name)

        return dict(list(context.items()) + list(mixin_context.items()))

    def get_queryset(self):
        # getting clug of url from self.kwargs dictionary
        return Movie.objects.filter(category__slug=self.kwargs['category_slug']).order_by('create_time')


class AddCategoryView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddCategoryForm
    template_name = 'mainapp/category/add_category.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Add category')

        return dict(list(context.items()) + list(mixin_context.items()))


class RegisterUserView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'mainapp/user/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Registration')

        return dict(list(context.items()) + list(mixin_context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('home')


class LoginUserView(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'mainapp/user/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Login')

        return dict(list(context.items()) + list(mixin_context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


# works only if DEBUG in settings.py is False
# and ALLOWED_HOSTS is ['127.0.0.1'] for example
def page_not_found(reqest, exception):
    return HttpResponseNotFound(f'<h1>Cant found that page</h1>')
