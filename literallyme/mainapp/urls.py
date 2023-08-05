from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addactor/', add_actor, name='add_actor'),
    path('login/', login, name='login'),
    path('post/<slug:actor_slug>/', about_actor, name='actor'),
    path('movies/', movies, name='movies'),
    path('movies/<slug:movie_slug>/', about_movie, name='movie_details'),
    path('movies/categories/<slug:category_slug>/', show_category, name='category')
]
