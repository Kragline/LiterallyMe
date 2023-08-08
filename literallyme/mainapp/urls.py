from django.urls import path
from .views import *


urlpatterns = [
    path('', ActorsListView.as_view(), name='home'),
    path('add_actor/', AddActorView.as_view(), name='add_actor'),
    path('actor/<slug:actor_slug>/', AboutActorView.as_view(), name='about_actor'),
    path('movies/', MovieListView.as_view(), name='movies'),
    path('add_movie', AddMovieView.as_view(), name='add_movie'),
    path('movies/<slug:movie_slug>/', AboutMovieView.as_view(), name='about_movie'),
    path('movies/categories/<slug:category_slug>/', CategoryListView.as_view(), name='category'),
    path('add_category', AddCategoryView.as_view(), name='add_category')
]
