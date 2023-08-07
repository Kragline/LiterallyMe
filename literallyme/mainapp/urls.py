from django.urls import path
from .views import *


urlpatterns = [
    path('', actors_list, name='home'),
    path('add_actor/', add_actor, name='add_actor'),
    path('actor/<slug:actor_slug>/', about_actor, name='about_actor'),
    path('movies/', movies_list, name='movies'),
    path('add_movie', add_movie, name='add_movie'),
    path('movies/<slug:movie_slug>/', about_movie, name='about_movie'),
    path('movies/categories/<slug:category_slug>/', show_category, name='category'),
    path('add_category', add_category, name='add_category')
]
