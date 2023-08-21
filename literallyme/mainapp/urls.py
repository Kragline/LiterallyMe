from django.urls import path
from .views import *


urlpatterns = [
    # Actor
    path('', ActorsListView.as_view(), name='home'),
    path('add_actor/', AddActorView.as_view(), name='add_actor'),
    path('actor/<slug:actor_slug>/', AboutActorView.as_view(), name='about_actor'),
    path('actors/<slug:actor_slug>/update/', UpdateActorView.as_view(), name='update_actor'),

    # Movie
    path('movies/', MovieListView.as_view(), name='movies'),
    path('add_movie/', AddMovieView.as_view(), name='add_movie'),
    path('movies/<slug:movie_slug>/', about_movie_view, name='about_movie'),
    path('movies/<slug:movie_slug>/update/', UpdateMovieView.as_view(), name='update_movie'),

    # Category
    path('movies/categories/<slug:category_slug>/', CategoryListView.as_view(), name='category'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),

    # Comment
    path('movies/<slug:movie_slug>/comment/update/<int:comment_id>/', UpdateCommentView.as_view(), name='update_comment'),
    path('movies/<slug:movie_slug>/comment/delete/<int:comment_id>/', DeleteCommentView.as_view(), name='delete_comment'),

    # search views
    path('search-actor', search_for_actors_view, name='actor_search'),
    path('search-movie', search_for_movies_view, name='movie_search'),
]
