from django.urls import path
from .views import *


urlpatterns = [
    path('', ActorsListView.as_view(), name='home'),
    path('add_actor/', AddActorView.as_view(), name='add_actor'),
    path('actor/<slug:actor_slug>/', AboutActorView.as_view(), name='about_actor'),
    path('actors/<slug:actor_slug>/update/', UpdateActorView.as_view(), name='update_actor'),
    path('movies/', MovieListView.as_view(), name='movies'),
    path('add_movie/', AddMovieView.as_view(), name='add_movie'),
    path('movies/<slug:movie_slug>/update/', UpdateMovieView.as_view(), name='update_movie'),
    path('movies/<slug:movie_slug>/', AboutMovieView.as_view(), name='about_movie'),
    path('search-movie', search_for_movies_view, name='movie_search'),
    path('movies/categories/<slug:category_slug>/', CategoryListView.as_view(), name='category'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('search-actor', search_for_actors_view, name='actor_search'),
]
